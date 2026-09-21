# Domain Vocabulary for Power Electronics Papers

## Core Technical Terms

- power conversion stage
- switching network
- passive filter
- duty ratio
- conversion ratio
- steady-state operating point
- periodic steady state
- continuous conduction mode
- discontinuous conduction mode
- small-signal model
- averaged model
- control-to-output dynamics
- line disturbance rejection
- load transient response
- output-voltage regulation
- current ripple
- voltage ripple
- switching loss
- conduction loss
- magnetic core loss
- thermal stress
- electromagnetic interference
- power density
- conversion efficiency
- soft-switching operation
- zero-voltage switching
- zero-current switching

## Modeling Language

- The converter is analyzed under the small-ripple approximation.
- The inductor volt-second balance yields the steady-state conversion ratio.
- The capacitor charge balance determines the average output-current relationship.
- The averaged model captures the low-frequency dynamics of the switching converter.
- The small-signal transfer function reveals the dominant poles and zeros that constrain compensation design.
- Parasitic resistance introduces damping and modifies the converter efficiency profile.

## Control Language

- The compensator is designed to achieve adequate phase margin while maintaining fast transient response.
- The loop bandwidth is selected below the switching frequency to preserve the validity of the averaged model.
- The proposed controller improves load-step recovery without increasing steady-state ripple.
- The control law regulates the output voltage over a wide input-voltage range.
- The closed-loop response is evaluated under line disturbances and abrupt load transitions.

## Hardware and Experimental Language

- A laboratory prototype is implemented to validate the theoretical analysis.
- The measured waveforms confirm the predicted switching sequence.
- The efficiency is reported across the full load range to capture light-load and rated-load behavior.
- Thermal measurements are used to verify that the semiconductor junction temperature remains within the safe operating region.
- The converter layout is designed to minimize high-di/dt loop area and reduce conducted emissions.

## Comparison Language

- Compared with the baseline converter, the proposed design reduces conduction loss at high load.
- The improvement is most pronounced under wide-input operation.
- The tradeoff is an increase in component count and control complexity.
- The method is complementary to device-level efficiency improvements.
- The observed discrepancy between analysis and measurement is mainly attributed to parasitic inductance and nonideal switching transitions.
