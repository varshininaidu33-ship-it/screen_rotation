# 📱 Screen Rotation as Orthogonal Transformation
### B.Tech 1st-Year Mathematics Mini-Project • Linear Algebra & Analytical Geometry

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

---

## 📌 Project Problem Statement
> *"Phone screen rotation can be represented as an orthogonal transformation. Rotation matrices have determinant $\pm 1$ and preserve distances, angles, shape, and size."*

## 🎯 Project Objective
Build an interactive educational engineering mathematics project that demonstrates how smartphone screen rotation is modeled using the standard 2D rotation matrix:
$$Q(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
and rigorously proves that the transformation is **orthogonal** ($Q^T Q = I$, $\det(Q) = 1$, $\|Qv\| = \|v\|$).

---

## ✨ Features
- 🎛️ **Interactive Transformation Lab:** Real-time sliders for coordinates $(X, Y)$ and angle $\theta \in [0^\circ, 360^\circ]$.
- ⚡ **Screen Orientation Presets:** Instant testing for $0^\circ$ (Portrait), $90^\circ$ (Landscape L), $180^\circ$ (Inverted), $270^\circ$ (Landscape R), and $360^\circ$ (Full Cycle).
- 📐 **Dynamic Matrix Cards:** Live updates of $Q(\theta)$, $Q^T$, verification product $Q^T Q = I_2$, $\det(Q) = 1$, and Euclidean distance checks.
- 📈 **2D Cartesian Coordinate Graph:** Visualizes vectors $P$ and $P'$ alongside the circular distance-invariant trajectory ($r = \|P\|$).
- 📱 **Smartphone Simulation:** Real-time rotating phone chassis illustrating rigid display buffer rotation without distortion.
- 📝 **Worked Example Calculator:** Verifies $P = (2, 3)$ at $\theta = 90^\circ \implies P' = (-3, 2)$.
- 🎓 **Viva Voce & Expo Guide:** Complete 24 mentor questions and concise answers with search & category filters.
- 🎙️ **Stage Presentations:** Rehearsal-ready 1-minute and 30-second presentation scripts.
- 💻 **Google Colab Notebook:** Optimized for execution directly on mobile phones.

---

## 📐 Mathematical Derivations & Proofs

### 1. 2D Rotation Matrix Derivation
For point $P(x, y)$ at distance $r$ with angle $\alpha$:
$$x = r\cos\alpha, \quad y = r\sin\alpha$$
Rotating by angle $\theta$:
$$x' = r\cos(\alpha + \theta) = x\cos\theta - y\sin\theta$$
$$y' = r\sin(\alpha + \theta) = x\sin\theta + y\cos\theta$$
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} \implies P' = Q(\theta)P$$

### 2. Proof of Orthogonality ($Q^T Q = I$)
$$Q^T = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}$$
$$Q^T Q = \begin{bmatrix} \cos^2\theta + \sin^2\theta & -\cos\theta\sin\theta + \sin\theta\cos\theta \\ -\sin\theta\cos\theta + \cos\theta\sin\theta & \sin^2\theta + \cos^2\theta \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2$$

### 3. Proof of Determinant ($\det(Q) = 1$)
$$\det(Q) = (\cos\theta)(\cos\theta) - (-\sin\theta)(\sin\theta) = \cos^2\theta + \sin^2\theta = 1$$
*(Confirms proper rotation without reflection).*

### 4. Proof of Distance Preservation ($\|Qv\| = \|v\|$)
$$\|Qv\|^2 = (Qv)^T(Qv) = v^T(Q^TQ)v = v^TIv = v^Tv = \|v\|^2 \implies \|Qv\| = \|v\|$$
*(Confirms Euclidean distances and screen aspect ratios are invariant).*

---

## 📊 Special Cases Reference

| Angle ($\theta$) | $\cos\theta$ | $\sin\theta$ | Rotation Matrix $Q(\theta)$ | Transformation | Screen Orientation |
|---|---|---|---|---|---|
| **0°** | $1$ | $0$ | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ | $(x, y) \to (x, y)$ | Standard Portrait |
| **90°** | $0$ | $1$ | $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ | $(x, y) \to (-y, x)$ | Landscape Left |
| **180°** | $-1$ | $0$ | $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ | $(x, y) \to (-x, -y)$ | Inverted Portrait |
| **270°** | $0$ | $-1$ | $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$ | $(x, y) \to (y, -x)$ | Landscape Right |
| **360°** | $1$ | $0$ | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ | $(x, y) \to (x, y)$ | Full Cycle Return |

---

## 🚀 How to Run

### 1. Interactive Web Application
Start a local server or double-click `start_project.bat`:
```bash
python -m http.server 8000
```
Open **[http://localhost:8000](http://localhost:8000)** in any browser.

### 2. Google Colab (Mobile Friendly)
1. Open [Google Colab](https://colab.research.google.com).
2. Upload `Screen_Rotation_Orthogonal_Transformation.ipynb`.
3. Tap **Runtime > Run All**.

### 3. Standalone Python Terminal Script
```bash
python standalone_app.py
```

---

## 📂 Project Structure
```
├── index.html                                   # Interactive Web Dashboard
├── style.css                                    # Glassmorphism Dark Theme Styles
├── app.js                                       # Linear Algebra Engine & Canvas Graph
├── start_project.bat                            # 1-Click Windows Launcher
├── Screen_Rotation_Orthogonal_Transformation.ipynb # Google Colab Notebook
├── PROJECT_REPORT_AND_VIVA.md                   # Complete 22-Section Project Report & Viva Q&A
├── standalone_app.py                            # Standalone Python Verification Script
├── generate_notebook.py                         # Colab Notebook Generator
└── README.md                                    # Project Documentation
```

---

## 🎓 Viva Voce Highlights
- **What is an orthogonal matrix?** A matrix where $Q^T = Q^{-1}$, meaning $Q^T Q = I$.
- **Why is $\det(Q) = 1$?** $+1$ represents a proper rotation that preserves geometric orientation, unlike $-1$ which indicates reflection.
- **Does screen rotation distort icons?** No, because orthogonal transformations preserve distances ($\|Qv\| = \|v\|$) and angles ($\langle Qu, Qv \rangle = \langle u, v \rangle$).

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
