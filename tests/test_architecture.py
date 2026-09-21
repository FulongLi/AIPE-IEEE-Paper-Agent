"""Behavioral regression tests; run with python -m unittest discover -s tests -v."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from venue_profiles import document_class, filesystem_path, list_venues, load_profile, strip_comments


def module(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


create = module("create-manuscript")
latex = module("check-latex")
indexer = module("build-reference-index")
packager = module("package-release")
VENUES = ("ieee-access", "ieee-conference", "ieee-ojcsys", "ieee-ojpel", "ieee-tai", "ieee-transactions")


def run_script(script: Path, *args, cwd: Path | None = None, expected: int = 0):
    process = subprocess.run([sys.executable, "-X", "utf8", str(script), *map(str, args)],
                             cwd=cwd or ROOT, capture_output=True, text=True, encoding="utf-8")
    if process.returncode != expected:
        raise AssertionError(f"{script.name} returned {process.returncode}\n{process.stdout}\n{process.stderr}")
    return process


class VenueTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.output = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def test_all_profiles_parse_and_match_real_entries(self):
        self.assertEqual(tuple(list_venues()), VENUES)
        for venue in VENUES:
            with self.subTest(venue=venue):
                profile = load_profile(venue)
                template = ROOT / profile["template"]["path"]
                entry = template / profile["template"]["entry"]
                self.assertTrue(entry.is_file())
                self.assertTrue((template / (profile["document_class"]["name"] + ".cls")).is_file())

    def test_all_venues_initialize_and_keep_support_assets(self):
        for venue in VENUES:
            with self.subTest(venue=venue):
                workspace = create.create_workspace(self.output, venue, "Verified Title", venue)
                self.assertEqual(latex.audit(workspace), [])
                main = (workspace / "main.tex").read_text(encoding="utf-8")
                self.assertIn(r"\title{Verified Title", main)
                for directory in create.DIRECTORIES:
                    self.assertTrue((workspace / directory).is_dir())
                for filename in create.SECTION_FILES:
                    self.assertTrue((workspace / "sections" / filename).is_file())
                self.assertEqual(len(list(workspace.rglob("*.tex"))), 8)
                self.assertNotIn(r"\cite{", strip_comments(main))
                self.assertNotIn(r"\begin{thebibliography}", main)
                self.assertNotIn(r"\begin{abstract}", (workspace / "sections/00-abstract.tex").read_text())
                run_script(ROOT / "scripts/check-citations.py", workspace, "--write-audit")

    def test_transactions_and_conference_differ(self):
        for venue, expected in (("ieee-transactions", ("IEEEtran", ["lettersize", "journal"])),
                                ("ieee-conference", ("IEEEtran", ["conference"]))):
            workspace = create.create_workspace(self.output, venue, "Title", venue)
            self.assertEqual(document_class((workspace / "main.tex").read_text()), expected)

    def test_access_preserves_front_matter_and_order(self):
        workspace = create.create_workspace(self.output, "access", "Access title", "ieee-access")
        text = (workspace / "main.tex").read_text()
        self.assertEqual(document_class(text), ("ieeeaccess", []))
        for command in (r"\author{\uppercase", r"\authorrefmark{1}", r"\address[1]",
                        r"\corresp{", r"\tfootnote{", r"\history{", r"\doi{", r"\titlepgskip=-21pt", r"\EOD"):
            self.assertIn(command, text)
        self.assertLess(text.index(r"\begin{abstract}"), text.index(r"\maketitle"))
        self.assertLess(text.index(r"\EOD"), text.index(r"\end{document}"))
        self.assertNotIn("10.1109/ACCESS.2024.0429000", text)

    def test_open_journals_and_tai_keep_special_elements(self):
        expected = {"ieee-ojpel": [r"\def\OJlogo", r"\affil{", r"\authorrefmark", r"\receiveddate{"],
                    "ieee-ojcsys": [r"\editor{", r"\sptitle{", r"\affilmark{1}"],
                    "ieee-tai": [r"\begin{IEEEImpStatement}", r"\end{IEEEImpStatement}"]}
        for venue, commands in expected.items():
            with self.subTest(venue=venue):
                workspace = create.create_workspace(self.output, venue, "Title", venue)
                text = (workspace / "main.tex").read_text()
                for command in commands:
                    self.assertIn(command, text)
                self.assertNotIn("92\\%", text)  # TAI's illustrative result must not enter a new paper.

    def test_profile_rejects_escaping_paths_and_class_mismatch(self):
        target = self.output / "venues" / "ieee-conference"
        shutil.copytree(ROOT / "venues/ieee-conference", target)
        path = target / "profile.json"
        profile = json.loads(path.read_text())
        for value in ("../outside", "C:/outside", "/outside"):
            changed = dict(profile, template=dict(profile["template"], path=value))
            path.write_text(json.dumps(changed))
            with self.assertRaises(ValueError):
                load_profile("ieee-conference", self.output)
        profile["document_class"]["options"] = ["journal"]
        path.write_text(json.dumps(profile))
        with self.assertRaises(ValueError):
            load_profile("ieee-conference", self.output)

    def test_title_is_plain_text_and_existing_workspace_is_protected(self):
        workspace = create.create_workspace(self.output, "safe", "A & B_50% #1 {test}")
        original = (workspace / "main.tex").read_bytes()
        self.assertIn(r"\title{A \& B\_50\% \#1 \{test\}", original.decode())
        with self.assertRaises(FileExistsError):
            create.create_workspace(self.output, "safe", "Another title")
        self.assertEqual((workspace / "main.tex").read_bytes(), original)

    def test_invalid_inputs_do_not_create_a_workspace(self):
        for kwargs in ({"venue": "unknown"}, {"domain": "not-installed"}):
            with self.assertRaises(ValueError):
                create.create_workspace(self.output, "invalid", "Title", **kwargs)
        self.assertFalse((self.output / "manuscripts").exists())

    def test_domain_selection_does_not_insert_scientific_content(self):
        generic = create.create_workspace(self.output, "generic", "Title", "ieee-ojpel")
        domain = create.create_workspace(self.output, "domain", "Title", "ieee-ojpel", domain="power-electronics")
        self.assertEqual((generic / "main.tex").read_bytes(), (domain / "main.tex").read_bytes())
        self.assertTrue((domain / "notes/domain.md").is_file())
        self.assertFalse((generic / "notes/domain.md").exists())
        self.assertEqual((generic / "refs/references.bib").read_bytes(), (domain / "refs/references.bib").read_bytes())

    def test_unused_sample_image_can_be_removed_but_required_logo_cannot(self):
        workspace = create.create_workspace(self.output, "logo", "Title", "ieee-access")
        (workspace / "fig1.png").unlink()
        self.assertEqual(latex.audit(workspace), [])
        (workspace / "logo.png").unlink()
        self.assertTrue(any("logo.png" in error for error in latex.audit(workspace)))

    def test_static_audit_detects_absolute_missing_paths_and_changed_class(self):
        workspace = create.create_workspace(self.output, "negative", "Title")
        main = workspace / "main.tex"
        main.write_text(main.read_text() + r"\input{C:/private/test}" + "\n" + r"\input{sections/missing}")
        self.assertTrue(any("non-portable" in e for e in latex.audit(workspace)))
        self.assertTrue(any("missing input" in e for e in latex.audit(workspace)))
        (workspace / "IEEEtran.cls").write_text("changed")
        self.assertTrue(any("modified template asset" in e for e in latex.audit(workspace)))

    def test_cli_works_from_unrelated_directory_and_explains_old_flag(self):
        result = run_script(ROOT / "scripts/create-manuscript.py", "cli", "--venue", "ieee-access",
                            "--root", self.output, cwd=self.output)
        workspace = self.output / "manuscripts" / "cli"
        self.assertTrue(workspace.is_dir())
        self.assertIn(str(workspace.resolve()), result.stdout)
        error = run_script(ROOT / "scripts/create-manuscript.py", "old", "--template", "unused",
                           cwd=self.output, expected=2)
        self.assertIn("--venue", error.stderr)


class ReferenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def test_citation_success_failure_comments_duplicates_and_manual_notes(self):
        (self.root / "main.tex").write_text("% " + r"\cite{commented}" + "\n" + r"\cite[see][p. 1]{fixture}")
        (self.root / "refs.bib").write_text('@article{fixture, title={Unit test fixture}, year={2000}}\n')
        (self.root / "notes").mkdir()
        manual = self.root / "notes/citation-verification.md"
        manual.write_text("Manual source review must survive regeneration.")
        run_script(ROOT / "scripts/check-citations.py", self.root, "--write-audit")
        self.assertEqual(manual.read_text(), "Manual source review must survive regeneration.")
        with (self.root / "main.tex").open("a") as stream:
            stream.write("\n" + r"\cite{missing}")
        run_script(ROOT / "scripts/check-citations.py", self.root, expected=1)
        (self.root / "main.tex").write_text(r"\cite{fixture}")
        with (self.root / "refs.bib").open("a") as stream:
            stream.write('@article{fixture, title={Duplicate test fixture}}\n')
        result = run_script(ROOT / "scripts/check-citations.py", self.root, "--write-audit", expected=1)
        self.assertIn("duplicate bib keys: 1", result.stdout)
        self.assertIn("Duplicate Citation Keys", (self.root / "notes/citation-audit.md").read_text())

    def test_reference_index_tracks_sources_duplicates_and_metadata_status(self):
        # Synthetic parser fixtures, never exported as manuscript references.
        (self.root / "first.bib").write_text('@article{fixture, title={Nested {Test} Title}, author={A and B}, year={2000}, url={https://example.com}}\n')
        (self.root / "second.bib").write_text('@book{fixture, title={Duplicate fixture}}\n')
        output = self.root / "output/index.json"
        run_script(ROOT / "scripts/build-reference-index.py", "--ref-dir", self.root, "--output", output)
        data = json.loads(output.read_text())
        self.assertEqual(data["record_count"], 2)
        self.assertEqual(data["duplicate_key_count"], 1)
        self.assertEqual(data["records"][0]["source_file"], "first.bib")
        self.assertEqual(data["records"][0]["verification_status"], "url-present")
        self.assertEqual(data["records"][1]["verification_status"], "needs-verification")

    def test_existing_library_rebuild_preserves_records(self):
        before = json.loads((ROOT / "PE_IEEE_reference/references-index.json").read_text(encoding="utf-8"))
        output = self.root / "index.json"
        run_script(ROOT / "scripts/build-reference-index.py", "--output", output, cwd=self.root)
        after = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(before["records"], after["records"])
        self.assertEqual(before["duplicate_keys"], after["duplicate_keys"])
        self.assertGreater(after["record_count"], 0)


class ArchitectureTests(unittest.TestCase):
    def test_original_template_assets_preserved(self):
        checksums = json.loads((ROOT / "tests/fixtures/template-checksums.json").read_text())
        for name, expected in checksums.items():
            with self.subTest(asset=name):
                path = ROOT / name
                data = path.read_bytes()
                if path.suffix.lower() in {".tex", ".cls", ".bst", ".sty", ".fd", ".map", ".txt"} or path.name == "README":
                    data = data.replace(b"\r\n", b"\n")
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected)

    def test_one_canonical_instruction_tree(self):
        self.assertFalse((ROOT / "workflows").exists())
        self.assertFalse((ROOT / "skills").exists())
        self.assertTrue((ROOT / "core/SKILL.md").is_file())
        for path in (ROOT / "core").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for match in re.findall(r"\x60((?:core|domains|artifacts)/[a-zA-Z0-9_./-]+\.md)\x60", text):
                self.assertTrue((ROOT / match).is_file(), f"{path}: {match}")

    def test_no_stale_removed_asset_paths(self):
        # Construct historical strings so the test itself isn't an obsolete reference.
        stale = ("IEEE paper" + " Template/", "knowledge-base/" + "power-electronics-foundations",
                 "skills/" + "ieee-paper-latex-writing/references")
        paths = [ROOT / name for name in ("README.md", "AGENTS.md", "INSTALL.md", ".gitignore")]
        for directory in ("core", "domains", "artifacts", "scripts"):
            paths += [p for p in (ROOT / directory).rglob("*") if p.suffix in {".md", ".py"}]
        for path in paths:
            for old in stale:
                self.assertNotIn(old, path.read_text(encoding="utf-8"), str(path))


class PackagingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(dir=filesystem_path(Path(tempfile.gettempdir())))
        cls.output = Path(cls.temp.name)
        cls.archives = packager.build_release(cls.output / "full")

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_every_archive_extracts_and_runs_all_venues_from_elsewhere(self):
        for number, archive in enumerate(self.archives):
            with self.subTest(package=archive.name):
                unpacked = self.output / f"unpacked-{number}"
                with zipfile.ZipFile(archive) as contents:
                    self.assertIsNone(contents.testzip())
                    for private in ("raw-mineru-output", "private-fulltext-cache", "__pycache__"):
                        self.assertFalse(any(private in Path(name).parts for name in contents.namelist()))
                    contents.extractall(unpacked)
                skill_files = list(unpacked.rglob("SKILL.md"))
                self.assertEqual(len(skill_files), 1)
                skill = skill_files[0].parent
                self.assertTrue((skill / "assets/PE_IEEE_reference/references-index.json").is_file())
                manifest = json.loads((skill / "generated-sources.json").read_text())
                expected_sources = {p.relative_to(ROOT).as_posix() for p in (ROOT / "core").rglob("*.md")}
                self.assertEqual({item["source"] for item in manifest["instructions"]}, expected_sources)
                for item in manifest["instructions"]:
                    source = ROOT / item["source"]
                    generated = skill / item["target"]
                    self.assertEqual(generated.read_text(encoding="utf-8"),
                                     packager.render_instruction(source.read_text(encoding="utf-8")))
                    self.assertEqual(hashlib.sha256(generated.read_bytes()).hexdigest(), item["generated_sha256"])
                for venue in VENUES:
                    output = self.output / f"output-{number}"
                    run_script(skill / "scripts/create-manuscript.py", venue, "--venue", venue, "--root", output, cwd=self.output)
                    workspace = output / "manuscripts" / venue
                    run_script(skill / "scripts/check-latex.py", workspace, cwd=self.output)
                    run_script(skill / "scripts/check-citations.py", workspace, "--write-audit", cwd=self.output)
                run_script(skill / "scripts/build-reference-index.py", "--output", self.output / f"packaged-index-{number}.json", cwd=self.output)
                for private in ("raw-mineru-output", "private-fulltext-cache"):
                    self.assertFalse(list(unpacked.rglob(private)))

    def test_generic_package_needs_no_domain_or_library(self):
        archives = packager.build_release(self.output / "generic", ["ieee-transactions"], include_domain=False)
        self.assertEqual(len(archives), 3)
        skill = self.output / "generic/codex-skill/ieee-paper-latex-writing"
        self.assertFalse((skill / "assets/domains").exists())
        self.assertFalse((skill / "assets/PE_IEEE_reference").exists())
        self.assertEqual(list_venues(skill / "assets"), ["ieee-transactions"])
        output = self.output / "generic-output"
        run_script(skill / "scripts/create-manuscript.py", "generic", "--venue", "ieee-transactions", "--root", output, cwd=self.output)
        run_script(skill / "scripts/check-latex.py", output / "manuscripts/generic", cwd=self.output)

    def test_private_caches_are_excluded_even_when_present(self):
        directory = ROOT / "domains/power-electronics/knowledge"
        excluded = packager.IGNORE(str(directory), ["raw-mineru-output", "private-fulltext-cache", "workspace", "concept-map.md"])
        self.assertEqual(set(excluded), {"raw-mineru-output", "private-fulltext-cache", "workspace"})


if __name__ == "__main__":
    unittest.main()
