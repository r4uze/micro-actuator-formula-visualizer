# Micro-Actuator Formula Visualizer

[中文](README.md) | [English](README.en.md)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Plotly](https://img.shields.io/badge/Plotly-5.18%2B-5e4fa2)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Try It Online

👉 **[Launch App](https://micro-actuator-formula-visualizer.streamlit.app/)**

No Python, Git, VS Code, or dependency installation is required. Just
open the app in your browser.

## Overview

This app helps beginners understand the most fundamental formula in
micro-actuator design: **how much does a cantilever beam bend** when you
push on it?

Enter beam dimensions, choose a material stiffness, and set the applied
force — the tip deflection updates instantly on an interactive chart.
No prior MEMS knowledge needed. If you understand high-school physics,
you are ready.

**The current version (v0.1) covers only cantilever beam tip deflection.**
More modules are planned for future releases.

## Features

- Direct numeric input for 5 physical parameters
- Real-time deflection calculation
- Automatic SI unit conversion (inputs in μm, μN, GPa; calculation in m, N, Pa)
- Force vs. tip deflection Plotly line chart
- Cantilever beam schematic diagram (fixed end, free end, applied force)
- LaTeX-rendered formula display
- Symbol reference table with units
- English / Chinese language switching
- Manual validation with translated error messages

## Formula

Cantilever beam tip deflection under a point load at the free end:

```
δ = F · L³ / (3 · E · I)
```

The moment of inertia for a rectangular cross-section:

```
I = w · t³ / 12
```

| Symbol | Meaning | Unit |
|---|---|---|
| δ | Tip deflection | μm |
| F | Applied force | μN |
| L | Beam length | μm |
| w | Beam width | μm |
| t | Beam thickness | μm |
| E | Young's modulus | GPa |
| I | Moment of inertia | m⁴ (SI) / μm⁴ (MEMS-scale) |

All calculations use SI units internally. Input values in μm, GPa, and
μN are converted automatically. The moment of inertia is computed in m⁴
but also shown in μm⁴ for an intuitive MEMS-scale reading.

## Screenshot

![App Screenshot](assets/screenshot.png)

## Model Assumptions

- **Rectangular cross-section** — the beam has a uniform rectangular profile.
- **Small deformation** — deflection is small relative to beam length.
- **Linear elastic behavior** — material obeys Hooke's law, no plastic deformation.

## Limitations

This is a simplified educational model and is **not a replacement for
Finite Element Method (FEM) simulation**. It does **not** account for:

- Nonlinear deformation (large-deflection effects)
- Damping (viscous or structural)
- Dynamic response
- Resonance
- Time-dependent loading

## Roadmap

The current version (v0.1) covers only cantilever beam tip deflection.
Planned modules for future releases:

| Module | Description |
|---|---|
| Beam stiffness | Spring constant k = F / δ |
| Resonant frequency | Natural frequency of micro-beams |
| Material presets | Quick-select common MEMS materials |
| Piezoelectric actuation | Piezoelectric extension and force |
| Magnetic micro-actuation | Lorentz force and magnetic torque |

Contributions and ideas are welcome.

## Author

Created by **r4uze**.
