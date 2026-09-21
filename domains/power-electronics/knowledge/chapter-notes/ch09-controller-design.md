# Chapter 9: Controller Design

## Retrieval Tags

feedback control, loop gain, compensator, phase margin, crossover frequency, transient response

## Core Ideas

- Controller design shapes loop gain to achieve stable regulation, disturbance rejection, and acceptable transient response.
- Compensation design must account for converter poles, zeros, right-half-plane zeros when present, sensor dynamics, and modulation gain.
- Stability margins and bandwidth selection connect frequency-domain design to time-domain performance.

## Useful IEEE Language

- "The compensator is designed to achieve sufficient phase margin while maintaining the desired closed-loop bandwidth."
- "The crossover frequency is selected to balance transient response, noise sensitivity, and modeling validity."

## Formula / Model Index

| Topic | What It Is Used For | Local Source Pointer |
| --- | --- | --- |
| Loop gain | Stability and performance assessment | Verify in Chapter 9 |
| Phase margin | Robustness metric | Verify in Chapter 9 |
| Compensator poles and zeros | Frequency-response shaping | Verify in Chapter 9 |

## Paper-Writing Use

Use this note when writing control design, stability analysis, or experimental transient-response sections.

## Local Source Pointers

- Official chapter title: Controller Design.
- Verify compensation procedure locally before citing.
