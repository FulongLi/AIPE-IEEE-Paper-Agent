# Chapter 19: Digital Control of Switched-Mode Power Converters

## Retrieval Tags

digital control, sampling, quantization, PWM update, delay, discrete-time compensator

## Core Ideas

- Digital control replaces continuous analog compensation with sampled measurement, computation, and pulse-width modulation updates.
- Sampling, computational delay, quantization, and zero-order-hold behavior affect stability and transient response.
- Digital implementation enables programmability, adaptive control, communication, and complex algorithms, but requires careful timing analysis.

## Useful IEEE Language

- "The digital controller is designed by accounting for sampling delay, computation latency, and PWM update behavior."
- "Discrete-time implementation enables flexible control features while introducing quantization and delay constraints."

## Formula / Model Index

| Topic | What It Is Used For | Local Source Pointer |
| --- | --- | --- |
| Sampling delay | Digital-loop stability analysis | Verify in Chapter 19 |
| Discrete compensator | Digital controller realization | Verify in Chapter 19 |
| Quantization effect | Resolution and limit-cycle assessment | Verify in Chapter 19 |

## Paper-Writing Use

Use this note when writing about DSP/MCU/FPGA control, adaptive algorithms, model predictive control, or digital PWM implementation.

## Local Source Pointers

- Official chapter title: Digital Control of Switched-Mode Power Converters.
- Verify discrete-time modeling details locally.
