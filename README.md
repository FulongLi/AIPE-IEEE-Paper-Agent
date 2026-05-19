# IEEE Paper Agent

一个用于撰写、整理和审查 IEEE 风格科研论文的 LaTeX 模板与写作 Skill 仓库。

这个仓库的目标很简单：让第一次打开它的人可以快速找到合适的 IEEE 模板，并用配套的论文写作方法，把研究内容整理成更像可投稿论文的结构。

## 这个仓库做什么

- 收集常用 IEEE LaTeX 模板，包括 conference、Transactions/journal、IEEE Access、TAI、OJCSYS、OJPEL 等方向。
- 提供一个可复用的 Codex Skill：`ieee-paper-latex-writing`，用于指导 IEEE 论文写作、LaTeX 修改、投稿前检查和审稿意见回复。
- 把“怎么写好 IEEE 论文”的经验拆成可执行流程：论文故事线、Introduction、Related Work、Method、Experiments、Figures/Tables、LaTeX submission checklist。

## 仓库结构

```text
IEEE-Paper-Agent/
├── IEEE paper Template/
│   ├── IEEE-conference-template-062824/
│   ├── Conference-LaTeX-template_10-17-19/
│   ├── IEEE-Transactions-LaTeX2e-templates-and-instructions/
│   ├── ACCESS_latex_template_20240429/
│   ├── TAI_LaTex_Template/
│   ├── OJCSYS_template_Latex/
│   ├── IEEE-ojpel-latex-template/
│   └── Transactions_win_or_mac_LaTeX2e_style_file/
└── skills/
    └── ieee-paper-latex-writing/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
```

## 如何使用 LaTeX 模板

1. 根据目标 venue 选择模板：
   - IEEE conference：优先看 `IEEE paper Template/IEEE-conference-template-062824/`
   - IEEE Transactions / journal：优先看 `IEEE paper Template/IEEE-Transactions-LaTeX2e-templates-and-instructions/`
   - IEEE Access：看 `IEEE paper Template/ACCESS_latex_template_20240429/`
   - TAI / OJCSYS / OJPEL：使用对应命名的模板目录

2. 复制对应模板目录，作为你的论文工作目录。

3. 在复制后的目录里修改 `.tex` 文件、图片和 BibTeX 文件。不要直接改官方 `.cls` 文件，除非投稿要求明确要求。

4. 使用本地 LaTeX 环境编译，例如：

```bash
latexmk -pdf main.tex
```

如果模板文件名不是 `main.tex`，请替换成对应 `.tex` 文件名。

## 如何使用写作 Skill

Skill 目录位于：

```text
skills/ieee-paper-latex-writing/
```

它适合这些任务：

- 从研究想法生成 IEEE paper outline
- 改写 abstract、introduction、related work、method、experiment section
- 检查论文贡献点是否清晰
- 审查 LaTeX 文件是否符合 IEEE 投稿习惯
- 检查图、表、公式、引用和参考文献
- 整理 reviewer comments 和 rebuttal / response letter

在 Codex 中可以这样使用：

```text
Use the skill at skills/ieee-paper-latex-writing to review my IEEE paper draft.
```

或者：

```text
Use ieee-paper-latex-writing to help me rewrite the abstract and introduction for an IEEE Transactions paper.
```

## Skill 里的核心资料

- `SKILL.md`：主工作流，说明什么时候使用这个 skill，以及整体写作和 LaTeX 审查流程。
- `references/writing-playbook.md`：IEEE 科研论文写作方法，包括标题、摘要、Introduction、Related Work、Methods、Experiments、图表和语气。
- `references/latex-submission-checklist.md`：IEEE LaTeX 投稿前检查清单。
- `references/reviewer-response.md`：审稿意见回复和 revision workflow。

## 推荐工作流

1. 先选目标 IEEE venue 和模板。
2. 用 Skill 梳理论文主线：
   - 研究问题是什么？
   - 当前方法缺口是什么？
   - 你的核心方法是什么？
   - 你的贡献点是什么？
   - 哪些实验或理论结果支撑这些贡献？
3. 写出 outline，再写 abstract 和 introduction。
4. 填充 method、experiment、related work、conclusion。
5. 编译 PDF，并用 LaTeX checklist 检查格式、引用、图表、公式和页面限制。
6. 投稿前进行一次 publication-readiness review。

## 适合谁

- 正在写 IEEE conference paper 的学生或研究者
- 准备 IEEE Transactions / journal 投稿的作者
- 想把 LaTeX 论文模板、写作流程和投稿检查流程标准化的团队
- 想用 AI agent 辅助科研写作、重写和审稿回复的人

## 注意事项

- 本仓库提供模板和写作流程，不替代目标会议或期刊的最新 author guidelines。
- 投稿前请始终检查目标 venue 官网的 page limit、匿名要求、copyright、bibliography style 和 supplementary material 规则。
- 不要为了压页数随意修改 IEEE 官方 class、页边距、字体或行距。
- 写作 Skill 不会自动生成真实实验结果、引用或数据；所有 scientific claims 都必须由你的实验、理论或可信文献支撑。
