# B.Tech 1st-Year Mathematics Mini-Project
# Screen Rotation as Orthogonal Transformation

---

## 1. Title
**Screen Rotation as Orthogonal Transformation**

## 2. Problem Statement
> *"Phone screen rotation can be represented as an orthogonal transformation. Rotation matrices have determinant $\pm 1$ and preserve distances, angles, shape, and size."*

## 3. Introduction
When a user tilts a smartphone from portrait to landscape mode, the device's operating system (Android or iOS) must re-render the graphical interface so that images and controls stay right-side up. Mathematically, this continuous physical motion is executed as a 2D linear transformation. The cornerstone mathematical tool that guarantees pixels and UI elements rotate without stretching, skewing, or shrinking is the **2D Rotation Matrix**, which represents an **orthogonal transformation**.

## 4. Objective
The objective of this project is to build an interactive educational project that:
1. Demonstrates how phone screen rotation is modeled using the standard 2D rotation matrix:
   $$Q(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
2. Proves mathematically and computationally that $Q(\theta)$ is an **orthogonal matrix** ($Q^T Q = I$).
3. Verifies that $\det(Q) = 1$ for pure rotation without reflection.
4. Demonstrates norm and distance preservation ($\|Qv\| = \|v\|$), angle preservation, shape preservation, and size preservation.
5. Provides an interactive, mobile-friendly Google Colab environment with sliders, preset buttons ($0°, 90°, 180°, 270°, 360°$), dynamic vector graphing, and phone screen simulation.

---

## 5. Mathematical Theory

### 6. Transformation
A transformation in linear algebra is an operation that maps an input vector or point $P \in \mathbb{R}^2$ to an output point $P' \in \mathbb{R}^2$ via a matrix multiplication $P' = T(P)$.
- *Simple English:* A mathematical rule that moves points on a plane to new positions.

### 7. Rotation
A rotation is a linear transformation in which every point in the plane rotates around a fixed point (the center of rotation, here the origin $(0, 0)$) by a specified angle $\theta$.
- *Simple English:* Turning an object around a pivot point without altering its size or shape.

### 8. Orthogonal Transformation
A linear transformation represented by a square matrix $Q$ is called **orthogonal** if:
$$Q^T Q = Q Q^T = I$$
where $Q^T$ is the matrix transpose and $I$ is the identity matrix.
- *Simple English:* A matrix whose transpose is equal to its inverse ($Q^{-1} = Q^T$). Multiplying a vector by an orthogonal matrix rotates or reflects it, but never stretches, squashes, or distorts it.

### 9. Rotation Matrix
For a counterclockwise rotation angle $\theta$, the 2D rotation matrix is defined as:
$$Q(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
For any coordinate vector $P = \begin{bmatrix} x \\ y \end{bmatrix}$:
$$P' = Q(\theta)P = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x\cos\theta - y\sin\theta \\ x\sin\theta + y\cos\theta \end{bmatrix}$$

---

## 10. Mathematical Derivations

### Derivation 1: Derivation of the 2D Rotation Matrix
Consider a point $P(x, y)$ located at distance $r$ from the origin, making an angle $\alpha$ with the positive $X$-axis:
$$x = r \cos\alpha, \quad y = r \sin\alpha$$
When the point is rotated counterclockwise about the origin by an angle $\theta$, its distance $r$ remains unchanged, but its total angle becomes $(\alpha + \theta)$.
Let the new coordinates be $(x', y')$:
$$x' = r \cos(\alpha + \theta)$$
$$y' = r \sin(\alpha + \theta)$$
Using trigonometric angle addition formulas:
$$\cos(\alpha + \theta) = \cos\alpha \cos\theta - \sin\alpha \sin\theta$$
$$\sin(\alpha + \theta) = \sin\alpha \cos\theta + \cos\alpha \sin\theta$$
Substituting $r \cos\alpha = x$ and $r \sin\alpha = y$:
$$x' = (r \cos\alpha)\cos\theta - (r \sin\alpha)\sin\theta = x\cos\theta - y\sin\theta$$
$$y' = (r \sin\alpha)\cos\theta + (r \cos\alpha)\sin\theta = x\sin\theta + y\cos\theta$$
Expressing this system of linear equations in matrix form:
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
Thus, $Q(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$.

---

### Derivation 2: Proof of Orthogonality ($Q^T Q = I$)
To test orthogonality, take the transpose of $Q(\theta)$:
$$Q^T = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix}$$
Now multiply $Q^T$ by $Q$:
$$Q^T Q = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
Performing matrix multiplication:
$$[Q^T Q]_{11} = (\cos\theta)(\cos\theta) + (\sin\theta)(\sin\theta) = \cos^2\theta + \sin^2\theta = 1$$
$$[Q^T Q]_{12} = (\cos\theta)(-\sin\theta) + (\sin\theta)(\cos\theta) = -\cos\theta\sin\theta + \sin\theta\cos\theta = 0$$
$$[Q^T Q]_{21} = (-\sin\theta)(\cos\theta) + (\cos\theta)(\sin\theta) = -\sin\theta\cos\theta + \cos\theta\sin\theta = 0$$
$$[Q^T Q]_{22} = (-\sin\theta)(-\sin\theta) + (\cos\theta)(\cos\theta) = \sin^2\theta + \cos^2\theta = 1$$
$$Q^T Q = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2$$
**Conclusion:** Since $Q^T Q = I$, $Q(\theta)$ is strictly an orthogonal matrix for any angle $\theta$.

---

### Derivation 3: Proof of Determinant ($\det(Q) = 1$)
The determinant of a $2 \times 2$ matrix $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ is $ad - bc$:
$$\det(Q) = (\cos\theta)(\cos\theta) - (-\sin\theta)(\sin\theta)$$
$$\det(Q) = \cos^2\theta - (-\sin^2\theta) = \cos^2\theta + \sin^2\theta = 1$$
**Conclusion:** $\det(Q) = +1$ proves this is a **proper orthogonal transformation** (rigid rotation without reflection).

---

### Derivation 4: Proof of Distance (Norm) Preservation ($\|Qv\| = \|v\|$)
Let $v = \begin{bmatrix} x \\ y \end{bmatrix}$ be any vector in $\mathbb{R}^2$.
Its squared Euclidean norm is:
$$\|v\|^2 = v^T v = x^2 + y^2$$
After transformation, $v' = Qv$:
$$\|Qv\|^2 = (Qv)^T (Qv) = v^T Q^T Q v$$
Since $Q^T Q = I$:
$$\|Qv\|^2 = v^T I v = v^T v = \|v\|^2$$
Taking square roots on both sides:
$$\|Qv\| = \|v\|$$
**Conclusion:** The distance of the point from the origin before rotation is identical to the distance after rotation.

---

### Derivation 5: Proof of Angle Preservation ($\langle Qu, Qv \rangle = \langle u, v \rangle$)
For any two vectors $u, v \in \mathbb{R}^2$:
$$\langle Qu, Qv \rangle = (Qu)^T (Qv) = u^T Q^T Q v = u^T I v = u^T v = \langle u, v \rangle$$
Because the dot product and vector norms are both preserved:
$$\cos(\phi') = \frac{\langle Qu, Qv \rangle}{\|Qu\| \|Qv\|} = \frac{\langle u, v \rangle}{\|u\| \|v\|} = \cos(\phi) \implies \phi' = \phi$$
**Conclusion:** All angles between features, icons, and lines are preserved.

---

## 11. Project Inputs
1. **X Coordinate:** Horizontal position of the original point $P$.
2. **Y Coordinate:** Vertical position of the original point $P$.
3. **Rotation Angle ($\theta$):** Rotation angle in degrees ($0^\circ \le \theta \le 360^\circ$).
4. **Quick Buttons:** Fast presets for $0^\circ, 90^\circ, 180^\circ, 270^\circ, 360^\circ$.

## 12. Processing
1. Compute $\cos\theta$ and $\sin\theta$ and build rotation matrix $Q(\theta)$.
2. Calculate transformed point $P' = Q(\theta)P$.
3. Compute matrix transpose $Q^T$ and matrix product $Q^T Q$.
4. Evaluate $\det(Q) = \cos^2\theta + \sin^2\theta$.
5. Compute norms $\|P\| = \sqrt{x^2+y^2}$ and $\|P'\| = \sqrt{(x')^2+(y')^2}$.
6. Compare difference $\|P'\| - \|P\|$ and verify orthogonality.

## 13. Project Outputs
- Original Coordinates: $P(x, y)$
- Rotation Matrix: $Q(\theta)$
- Transformed Coordinates: $P'(x', y')$
- Transpose Matrix: $Q^T$
- Verification Product: $Q^T Q = I$
- Determinant: $\det(Q) = 1.000$
- Distance Check: $\|P\|$, $\|P'\|$, $\Delta d = 0.000$
- Status Badge: *"The transformation is orthogonal. Distance is preserved."*
- Dynamic 2D Cartesian Graph & Smartphone Chassis Simulation.

---

## 14. Special Cases Table

| Angle ($\theta$) | $\cos\theta$ | $\sin\theta$ | Matrix $Q(\theta)$ | Transformation $(x, y) \to$ | Smartphone Orientation |
|---|---|---|---|---|---|
| **0°** | $1$ | $0$ | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ | $(x, y)$ | Portrait Standard |
| **90°** | $0$ | $1$ | $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ | $(-y, x)$ | Landscape (Left tilt) |
| **180°** | $-1$ | $0$ | $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$ | $(-x, -y)$ | Inverted Portrait |
| **270°** | $0$ | $-1$ | $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$ | $(y, -x)$ | Landscape (Right tilt) |
| **360°** | $1$ | $0$ | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ | $(x, y)$ | Full Cycle Return |

---

## 15. Worked Example (Step-by-Step)

### Given:
- Point: $P = (2, 3) \implies P = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$
- Angle: $\theta = 90^\circ$

### Step 1: Form Rotation Matrix
$$\cos(90^\circ) = 0, \quad \sin(90^\circ) = 1$$
$$Q(90^\circ) = \begin{bmatrix} \cos(90^\circ) & -\sin(90^\circ) \\ \sin(90^\circ) & \cos(90^\circ) \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$

### Step 2: Compute Transformed Point $P'$
$$P' = Q(90^\circ) P = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
$$x' = (0)(2) + (-1)(3) = 0 - 3 = -3$$
$$y' = (1)(2) + (0)(3) = 2 + 0 = 2$$
$$P' = \begin{bmatrix} -3 \\ 2 \end{bmatrix} \implies P' = (-3, 2)$$

### Step 3: Verify Orthogonality ($Q^T Q = I$)
$$Q^T = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$$
$$Q^T Q = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} (0)(0)+(1)(1) & (0)(-1)+(1)(0) \\ (-1)(0)+(0)(1) & (-1)(-1)+(0)(0) \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I_2 \quad \text{(Verified!)}$$

### Step 4: Verify Determinant
$$\det(Q) = (0)(0) - (-1)(1) = 0 - (-1) = 1 \quad \text{(Verified!)}$$

### Step 5: Distance Comparison
- Distance before rotation:
  $$\|P\| = \sqrt{2^2 + 3^2} = \sqrt{4 + 9} = \sqrt{13} \approx 3.6056$$
- Distance after rotation:
  $$\|P'\| = \sqrt{(-3)^2 + 2^2} = \sqrt{9 + 4} = \sqrt{13} \approx 3.6056$$
- Difference:
  $$\|P'\| - \|P\| = 3.6056 - 3.6056 = 0.0000 \quad \text{(Distance strictly preserved!)}$$

---

## 16. Interactive Demonstration & 17. Visualizations
The project features two synchronized visualizations:
1. **2D Cartesian Coordinate Graph:**
   - Displays coordinate axes $X$ and $Y$ with origin $O(0,0)$.
   - Plots original vector $P$ in sky-blue and rotated vector $P'$ in emerald-green.
   - Draws a dotted reference circle of radius $r = \|P\|$ to show the trajectory is circular.
   - Draws a golden arc showing the rotation direction and angle $\theta$.
2. **Smartphone Screen Simulation:**
   - Renders a smartphone chassis with screen glass and camera notch.
   - Shows the original portrait orientation (dashed outline).
   - Shows the dynamically rotated smartphone body at angle $\theta$.
   - Displays a target pixel on the screen tracking the exact coordinate transformation.

---

## 18. Benefits
1. **Practical Connection:** Bridges abstract linear algebra theorems with daily consumer technology.
2. **Geometric Intuition:** Allows students to visually grasp what "orthogonal matrix" and "norm preservation" mean geometrically.
3. **Foundation for Engineering Careers:** Rotation matrices are the building blocks of 3D games, robotics forward/inverse kinematics, drone orientation control, and computer vision.
4. **Mobile Accessible:** Fully operational on smartphone screens via Google Colab without requiring a computer.

## 19. Limitations
1. **2D Planar Model:** Considers rotation solely in the display plane ($Z$-axis rotation). Full physical phone orientation in 3D space uses 3D rotation matrices or **quaternions** in $SO(3)$.
2. **Sensor Layer Abstraction:** In real smartphones, rotation triggers via an IMU sensor (accelerometer + gyroscope) sensing the gravity vector. The project directly takes $\theta$ as mathematical input.
3. **Aspect Ratio Reflow:** Real smartphones have rectangular aspect ratios (e.g. 19.5:9), so operating systems trigger a responsive UI re-layout alongside coordinate transformation.

## 20. Real-Life Applications
- **Smartphones & Tablets:** Display orientation rotation (Android SurfaceFlinger / iOS Quartz Compositor).
- **Computer Graphics:** 2D/3D sprite rotation, camera rotation, and shader vertex transforms.
- **Robotics & Drones:** Coordinate transformations between robot body frame and inertial world frame.
- **Medical Imaging:** Rotating CT and MRI slices for multi-angle diagnostic visualization.
- **Computer Vision:** Image augmentation via random rotations during neural network training.

## 21. Conclusion
The project conclusively proves that smartphone screen rotation is governed by a **2D orthogonal transformation**. The mathematical verification confirms $Q^T Q = I$, $\det(Q) = 1$, and $\|Qv\| = \|v\|$, establishing that rotation preserves distance, angles, shape, and size.

---

## 22. Comprehensive Viva Questions & Answers (24 Questions)

### Q1. What is your project?
**Ans:** My project is an interactive educational tool titled *"Screen Rotation as Orthogonal Transformation"* that models smartphone screen rotation using 2D rotation matrices and proves that the transformation is orthogonal.

### Q2. What is the problem statement?
**Ans:** *"Phone screen rotation can be represented as an orthogonal transformation. Rotation matrices have determinant $\pm 1$ and preserve distances, angles, shape, and size."*

### Q3. Why did you choose this topic?
**Ans:** To demonstrate how 1st-year B.Tech linear algebra concepts—such as orthogonal matrices, determinants, and norm preservation—are practically applied in everyday smartphone display technology.

### Q4. What is a transformation?
**Ans:** A transformation is a mathematical mapping $T: \mathbb{R}^n \to \mathbb{R}^n$ that takes points from one coordinate system and converts them into new coordinates according to a specific mathematical rule.

### Q5. What is rotation?
**Ans:** Rotation is a linear transformation that turns every point in a plane through a fixed angle $\theta$ around a fixed pivot point (the origin), without changing any distance from the pivot.

### Q6. What is an orthogonal matrix?
**Ans:** A square matrix $Q$ is orthogonal if its transpose equals its inverse ($Q^T = Q^{-1}$), which means $Q^T Q = Q Q^T = I$ (the identity matrix).

### Q7. What is the standard 2D rotation matrix?
**Ans:**
$$Q(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

### Q8. Why is the rotation matrix orthogonal?
**Ans:** Because when we compute $Q^T Q$, the diagonal elements simplify to $\cos^2\theta + \sin^2\theta = 1$ and the off-diagonal elements cancel out to $0$, yielding the identity matrix $I$.

### Q9. What is $Q^T Q$?
**Ans:** $Q^T Q$ is the product of the transpose of the matrix and itself. For any orthogonal matrix, $Q^T Q$ is always the Identity Matrix $I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$.

### Q10. What is the determinant of a rotation matrix?
**Ans:** The determinant is always $+1$:
$$\det(Q) = (\cos\theta)(\cos\theta) - (-\sin\theta)(\sin\theta) = \cos^2\theta + \sin^2\theta = 1$$

### Q11. Why is the determinant 1 and not -1?
**Ans:** A determinant of $+1$ represents a **proper rotation** (preserves orientation and handedness). A determinant of $-1$ represents an **improper rotation** (a rotation combined with a reflection/mirror flip).

### Q12. Does rotation change distance?
**Ans:** No. Rotation strictly preserves distances from the origin and pairwise distances between any points ($\|Qv\| = \|v\|$).

### Q13. Does rotation change shape or size?
**Ans:** No. Because distances and angles are preserved, rotation is an **isometry** (rigid body motion). The object's shape and size remain completely unchanged.

### Q14. What happens at 90° rotation?
**Ans:** The matrix becomes $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$, transforming coordinates $(x, y) \to (-y, x)$. For example, $(2, 3) \to (-3, 2)$.

### Q15. What happens at 180° rotation?
**Ans:** The matrix becomes $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$, transforming coordinates $(x, y) \to (-x, -y)$ (vector inversion through origin).

### Q16. What happens at 270° rotation?
**Ans:** The matrix becomes $\begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$, transforming coordinates $(x, y) \to (y, -x)$.

### Q17. What happens at 360° rotation?
**Ans:** The matrix returns to the identity matrix $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$, returning coordinates $(x, y) \to (x, y)$ (a full rotation).

### Q18. What is the input to your project?
**Ans:** The original coordinates $(x, y)$ and the rotation angle $\theta$ in degrees (via sliders and preset buttons for $0°, 90°, 180°, 270°, 360°$).

### Q19. What is the output of your project?
**Ans:** The transformed coordinates $P'$, rotation matrix $Q$, $Q^T$, $Q^T Q$, determinant $\det(Q)$, distances before/after, orthogonality check, and visual plots of the vectors and rotating phone screen.

### Q20. What is the real-life application?
**Ans:** Smartphone screen auto-rotation, video game camera controls, GPU graphics rendering pipelines, robotics kinematics, and computer vision image augmentation.

### Q21. What are the benefits of this project?
**Ans:** It makes abstract linear algebra intuitive and visual, reinforces matrix multiplication and orthogonality, and runs directly on mobile phones in Google Colab.

### Q22. What are the limitations of this project?
**Ans:** It is a 2D planar rotation model. Real phones rotate in 3D space, requiring 3D rotation matrices or quaternions, and rely on accelerometer/gyroscope sensors.

### Q23. How is this project related to linear algebra?
**Ans:** It demonstrates core linear algebra concepts: linear transformations, vector spaces, matrix transpose, matrix multiplication, orthogonal matrices, Euclidean norms, and determinants.

### Q24. How does your project prove orthogonality?
**Ans:** It computes $Q^T Q$ and checks if it equals $I_2$, evaluates $\det(Q) = 1$, and numerically verifies that $\|Qv\| - \|v\| = 0$.

---

## 🎙️ Stage Presentations

### 1-Minute Stage Pitch (For Project Expo)
> *"Good morning respected judges and faculty. When you rotate your smartphone to watch a video, how does the screen turn smoothly without distorting, stretching, or shrinking your app?  
> Our project, **'Screen Rotation as Orthogonal Transformation'**, demonstrates the exact linear algebra powering this feature.  
> Smartphone screen rotation is governed by the 2D rotation matrix:  
> $Q(\theta) = [[\cos\theta, -\sin\theta], [\sin\theta, \cos\theta]]$.  
> We prove that this matrix is **orthogonal** because $Q^T Q = I$ and $\det(Q) = 1$.  
> For example, rotating point $(2, 3)$ by $90^\circ$ maps it to $(-3, 2)$. The distance $\sqrt{13} \approx 3.61$ remains identical before and after rotation.  
> This proves that orthogonal transformations preserve distance, angles, shape, and size—making them indispensable in mobile operating systems, computer graphics, and robotics."*

### 30-Second Elevator Pitch
> *"Our project proves that smartphone screen rotation is a direct application of **orthogonal transformations** in linear algebra. Using the 2D rotation matrix $Q(\theta)$, we prove that $Q^T Q = I$ and $\det(Q) = 1$. This property guarantees that Euclidean distance and angles are strictly preserved ($\|Qv\| = \|v\|$), ensuring that screen icons and graphics rotate without distortion or loss of shape."*
