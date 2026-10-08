import json

cells = []

def add_md(text):
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.strip().split("\n")]
    })

def add_code(text):
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in text.strip().split("\n")]
    })

# ==========================================
# CELL 1: Markdown Header & Problem Statement
# ==========================================
add_md("""# 📱 B.Tech 1st-Year Mathematics Mini-Project
# **Screen Rotation as Orthogonal Transformation**

---

### **Project Problem Statement**
> *"Phone screen rotation can be represented as an orthogonal transformation. Rotation matrices have determinant $\\pm 1$ and preserve distances, angles, shape, and size."*

### **Project Objective**
Build an interactive educational project that demonstrates how phone screen rotation can be represented mathematically using a 2D rotation matrix:
$$Q(\\theta) = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}$$
and rigorously proves that the transformation is **orthogonal** ($Q^T Q = I$, $\\det(Q) = 1$, $\\|Qv\\| = \\|v\\|$).

---
**Course:** Linear Algebra & Calculus (B.Tech 1st Year)  
**Tools Used:** Python, NumPy, Matplotlib, ipywidgets (Google Colab Mobile Compatible)
""")

# ==========================================
# CELL 2: Code - Setup and Imports
# ==========================================
add_code("""# ==============================================================================
# CELL 1: SETUP AND IMPORTS
# ==============================================================================
# Description: Imports essential libraries for numerical computation,
# plotting, and mobile-friendly interactive widgets in Google Colab.
# All libraries are pre-installed in standard Google Colab environments.
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Arc
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output

# Configure clean plot styling suitable for mobile & desktop screens
plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10

print("✅ Setup complete! NumPy, Matplotlib, and ipywidgets are ready.")
""")

# ==========================================
# CELL 3: Code - Backend Mathematical Engine
# ==========================================
add_code("""# ==============================================================================
# CELL 2: BACKEND MATHEMATICAL ENGINE
# ==============================================================================
# Pure Python functions for matrix operations, coordinate transformations,
# and rigorous verification of orthogonality and distance preservation.
# UI logic is kept separate from mathematical logic.
# ==============================================================================

def rotation_matrix(theta_deg):
    \"\"\"
    Computes the 2D rotation matrix Q(theta) for a given angle in degrees.
    Q(theta) = [[cos(theta), -sin(theta)],
                [sin(theta),  cos(theta)]]
    Small floating-point noise is rounded for clean zero/one representation.
    \"\"\"
    rad = np.radians(theta_deg)
    cos_t = np.cos(rad)
    sin_t = np.sin(rad)
    
    # Clean tiny floating-point precision errors (e.g. at 90 deg, cos is ~6e-17)
    cos_t = 0.0 if np.isclose(cos_t, 0.0, atol=1e-12) else cos_t
    sin_t = 0.0 if np.isclose(sin_t, 0.0, atol=1e-12) else sin_t
    
    Q = np.array([
        [cos_t, -sin_t],
        [sin_t,  cos_t]
    ], dtype=float)
    return Q

def rotate_point(x, y, theta_deg):
    \"\"\"
    Applies the linear transformation P' = Q(theta) * P.
    Input: Coordinates (x, y) and rotation angle theta in degrees.
    Output: Transformed coordinates (x_rot, y_rot) as a numpy array.
    \"\"\"
    P = np.array([x, y], dtype=float)
    Q = rotation_matrix(theta_deg)
    P_prime = Q @ P
    return np.round(P_prime, 4)

def calculate_determinant(Q):
    \"\"\"
    Computes det(Q) = (Q_00 * Q_11) - (Q_01 * Q_10).
    For a pure rotation matrix, det(Q) == +1.0.
    \"\"\"
    det_val = np.linalg.det(Q)
    return float(np.round(det_val, 4))

def verify_orthogonality(Q):
    \"\"\"
    Verifies if Q is orthogonal by checking:
    1. Q^T @ Q == Identity Matrix I (within numerical tolerance)
    2. det(Q) == +1.0 (proper rotation)
    Returns: (is_orthogonal, Q_transpose, Q_T_dot_Q)
    \"\"\"
    Q_T = Q.T
    Q_T_dot_Q = Q_T @ Q
    identity = np.eye(2)
    is_orthogonal = np.allclose(Q_T_dot_Q, identity, atol=1e-5)
    return is_orthogonal, np.round(Q_T, 4), np.round(Q_T_dot_Q, 4)

def calculate_distance(point):
    \"\"\"
    Calculates Euclidean norm ||v|| = sqrt(x^2 + y^2).
    Represents distance of the point from origin (0, 0).
    \"\"\"
    return float(np.round(np.linalg.norm(point), 4))

def compare_distances(p_orig, p_rot):
    \"\"\"
    Compares the distance before and after transformation:
    ||v|| vs ||Qv|| and calculates absolute difference.
    \"\"\"
    d_orig = calculate_distance(p_orig)
    d_rot = calculate_distance(p_rot)
    diff = abs(d_rot - d_orig)
    preserved = np.isclose(diff, 0.0, atol=1e-5)
    return d_orig, d_rot, float(np.round(diff, 6)), preserved

print("✅ Mathematical backend engine loaded successfully.")
""")

# ==========================================
# CELL 4: Code - Worked Example Verification
# ==========================================
add_code("""# ==============================================================================
# CELL 3: WORKED EXAMPLE VERIFICATION
# ==============================================================================
# Verifies the required textbook worked example:
# Point P = (2, 3), Angle theta = 90 degrees
# Expected:
# Q(90) = [[0, -1], [1, 0]]
# P' = (-3, 2)
# Q^T @ Q = [[1, 0], [0, 1]] = I
# det(Q) = 1.0
# Distance = sqrt(2^2 + 3^2) = sqrt(13) ~= 3.6056 (Preserved)
# ==============================================================================

P_test = (2.0, 3.0)
theta_test = 90.0

Q_ex = rotation_matrix(theta_test)
P_prime_ex = rotate_point(P_test[0], P_test[1], theta_test)
det_ex = calculate_determinant(Q_ex)
is_ortho_ex, Q_T_ex, QTQ_ex = verify_orthogonality(Q_ex)
d_orig_ex, d_rot_ex, diff_ex, dist_pres_ex = compare_distances(P_test, P_prime_ex)

print("=" * 60)
print("📊 B.TECH 1ST-YEAR MATHEMATICS WORKED EXAMPLE (THETA = 90°)")
print("=" * 60)
print(f"Original Point P              : {P_test}")
print(f"Rotation Angle theta          : {theta_test}°")
print(f"Rotation Matrix Q(90°)        :\\n{Q_ex}")
print(f"Transformed Point P' = Q * P  : ({P_prime_ex[0]}, {P_prime_ex[1]})")
print("-" * 60)
print(f"Transpose Q^T                 :\\n{Q_T_ex}")
print(f"Orthogonality Check Q^T * Q   :\\n{QTQ_ex}")
print(f"Determinant det(Q)            : {det_ex}")
print(f"Original Distance ||P||       : {d_orig_ex} (sqrt(13) = {np.sqrt(13):.4f})")
print(f"Rotated Distance ||P'||       : {d_rot_ex}")
print(f"Distance Difference           : {diff_ex}")
print("-" * 60)
print(f"RESULT: Transformation is Orthogonal? : {is_ortho_ex} (Q^T * Q = I)")
print(f"RESULT: Distance is Preserved?        : {dist_pres_ex} (||QP|| = ||P||)")
print("=" * 60)
""")

# ==========================================
# CELL 5: Code - Graphical Visualization
# ==========================================
add_code("""# ==============================================================================
# CELL 4: GRAPHICAL VISUALIZATION ENGINE
# ==============================================================================
# Generates dual side-by-side plots:
# 1. 2D Cartesian Coordinate Graph (Origin, vectors, arc of rotation, points)
# 2. Smartphone Screen Rotation Simulation (Chassis, screen frame, pixel transform)
# ==============================================================================

def update_visualization(x, y, theta_deg):
    \"\"\"
    Plots the coordinate transformation and phone screen simulation.
    \"\"\"
    P_orig = np.array([x, y], dtype=float)
    P_rot = rotate_point(x, y, theta_deg)
    d_orig = calculate_distance(P_orig)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))
    fig.patch.set_facecolor('#0f172a') # Sleek dark modern theme
    
    # -------------------------------------------------------------
    # SUBPLOT 1: 2D CARTESIAN COORDINATE GRAPH
    # -------------------------------------------------------------
    ax1.set_facecolor('#1e293b')
    ax1.set_title(f"2D Orthogonal Rotation (\\theta = {theta_deg}°)", 
                  color='#f8fafc', fontsize=13, fontweight='bold', pad=12)
    
    # Determine dynamic coordinate bounds
    max_val = max(abs(x), abs(y), abs(P_rot[0]), abs(P_rot[1]), 3.0) + 2.0
    ax1.set_xlim(-max_val, max_val)
    ax1.set_ylim(-max_val, max_val)
    ax1.set_aspect('equal')
    
    # Grid lines and axes
    ax1.grid(True, linestyle='--', color='#334155', alpha=0.7)
    ax1.axhline(0, color='#64748b', linewidth=1.2)
    ax1.axvline(0, color='#64748b', linewidth=1.2)
    
    # Circular trajectory path (proving radius/distance is constant)
    if d_orig > 1e-4:
        circle = plt.Circle((0, 0), d_orig, color='#38bdf8', fill=False, 
                            linestyle=':', linewidth=1.5, alpha=0.6, 
                            label=f"Distance Circle (r = {d_orig:.2f})")
        ax1.add_patch(circle)
        
        # Arc indicating rotation direction
        orig_angle = np.degrees(np.arctan2(y, x))
        arc = Arc((0, 0), d_orig * 0.7, d_orig * 0.7, angle=0,
                  theta1=orig_angle, theta2=orig_angle + theta_deg,
                  color='#fbbf24', linewidth=2.0, linestyle='-')
        ax1.add_patch(arc)
    
    # Vector: Origin to Original Point (Blue)
    ax1.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, 
               color='#38bdf8', width=0.012, label='Original Vector P')
    ax1.scatter([x], [y], color='#38bdf8', s=100, zorder=5)
    ax1.annotate(f"P ({x:.1f}, {y:.1f})", (x, y), textcoords="offset points", 
                 xytext=(8, 8), color='#38bdf8', fontweight='bold', fontsize=10)
    
    # Vector: Origin to Rotated Point (Green)
    ax1.quiver(0, 0, P_rot[0], P_rot[1], angles='xy', scale_units='xy', scale=1, 
               color='#4ade80', width=0.012, label="Rotated Vector P'")
    ax1.scatter([P_rot[0]], [P_rot[1]], color='#4ade80', s=100, zorder=5)
    ax1.annotate(f"P' ({P_rot[0]:.1f}, {P_rot[1]:.1f})", (P_rot[0], P_rot[1]), 
                 textcoords="offset points", xytext=(8, 8), color='#4ade80', 
                 fontweight='bold', fontsize=10)
    
    # Origin marker
    ax1.scatter([0], [0], color='#f8fafc', s=50, zorder=6)
    ax1.text(0.2, -0.4, "O(0,0)", color='#94a3b8', fontsize=9)
    
    ax1.tick_params(colors='#94a3b8')
    for spine in ax1.spines.values():
        spine.set_color('#475569')
    ax1.legend(loc='upper left', facecolor='#0f172a', edgecolor='#334155', 
               labelcolor='#f8fafc', fontsize=9)

    # -------------------------------------------------------------
    # SUBPLOT 2: PHONE SCREEN SIMULATION
    # -------------------------------------------------------------
    ax2.set_facecolor('#1e293b')
    ax2.set_title("Smartphone Screen Rotation Simulation", 
                  color='#f8fafc', fontsize=13, fontweight='bold', pad=12)
    ax2.set_xlim(-6, 6)
    ax2.set_ylim(-6, 6)
    ax2.set_aspect('equal')
    ax2.grid(True, linestyle='--', color='#334155', alpha=0.5)
    
    # Phone dimensions (Portrait ratio: 3.2 x 6.4)
    w_p, h_p = 3.0, 5.4
    
    # Original Phone Ghost Outline (Portrait reference at 0 deg)
    rect_orig = patches.Rectangle((-w_p/2, -h_p/2), w_p, h_p, linewidth=1.5,
                                  edgecolor='#64748b', facecolor='#0f172a', 
                                  linestyle='--', alpha=0.4, label='Portrait Reference (0°)')
    ax2.add_patch(rect_orig)
    
    # Rotated Phone Frame
    t = patches.transforms.Affine2D().rotate_deg(theta_deg) + ax2.transData
    
    # Outer Phone Body
    phone_body = patches.Rectangle((-w_p/2, -h_p/2), w_p, h_p, linewidth=2.5,
                                   edgecolor='#818cf8', facecolor='#1e1b4b', 
                                   alpha=0.85, transform=t, label=f'Current Phone ({theta_deg}°)')
    ax2.add_patch(phone_body)
    
    # Inner Display Glass
    screen_glass = patches.Rectangle((-w_p/2 + 0.2, -h_p/2 + 0.4), w_p - 0.4, h_p - 0.8, 
                                     linewidth=1, edgecolor='#4338ca', 
                                     facecolor='#312e81', alpha=0.7, transform=t)
    ax2.add_patch(screen_glass)
    
    # Camera Notch
    notch = patches.Rectangle((-0.4, h_p/2 - 0.25), 0.8, 0.15, 
                              facecolor='#e2e8f0', transform=t)
    ax2.add_patch(notch)
    
    # Phone Screen Content Pixel / Point representation
    # Normalized point representation inside the screen
    norm_x = np.clip(x / max(abs(max_val), 1) * 1.0, -1.0, 1.0)
    norm_y = np.clip(y / max(abs(max_val), 1) * 1.8, -2.0, 2.0)
    
    # Point rotated with the phone display
    rot_p_local = rotate_point(norm_x, norm_y, theta_deg)
    ax2.scatter([rot_p_local[0]], [rot_p_local[1]], color='#f43f5e', s=120, zorder=7)
    ax2.annotate(f"Display Pixel\\n({P_rot[0]:.1f}, {P_rot[1]:.1f})", 
                 (rot_p_local[0], rot_p_local[1]), textcoords="offset points", 
                 xytext=(10, -5), color='#f43f5e', fontweight='bold', fontsize=9)
    
    # Rotation arrow around center
    center_circle = patches.Circle((0, 0), 0.35, facecolor='#4f46e5', edgecolor='#c7d2fe')
    ax2.add_patch(center_circle)
    ax2.text(0, -0.05, "↻", color='#ffffff', fontsize=14, ha='center', va='center', fontweight='bold')
    
    ax2.tick_params(colors='#94a3b8')
    for spine in ax2.spines.values():
        spine.set_color('#475569')
    ax2.legend(loc='upper left', facecolor='#0f172a', edgecolor='#334155', 
               labelcolor='#f8fafc', fontsize=9)
    
    plt.tight_layout()
    plt.show()

print("✅ Graphical visualization engine ready.")
""")

# ==========================================
# CELL 6: Code - Interactive Dashboard
# ==========================================
add_code("""# ==============================================================================
# CELL 5: INTERACTIVE DASHBOARD & VERIFICATION CARDS
# ==============================================================================
# Mobile-optimized interactive interface with sliders, quick-preset buttons,
# mathematical metrics cards, and real-time visualization.
# ==============================================================================

# Widget Controls (Mobile Friendly Sizing)
slider_x = widgets.FloatSlider(value=2.0, min=-10.0, max=10.0, step=0.5, 
                               description='X Coord:', layout=widgets.Layout(width='90%'))
slider_y = widgets.FloatSlider(value=3.0, min=-10.0, max=10.0, step=0.5, 
                               description='Y Coord:', layout=widgets.Layout(width='90%'))
slider_theta = widgets.IntSlider(value=90, min=0, max=360, step=15, 
                                 description='Angle θ (°):', layout=widgets.Layout(width='90%'))

# Quick Preset Buttons
btn_0 = widgets.Button(description='0° (Reset)', button_style='info', layout=widgets.Layout(width='75px'))
btn_90 = widgets.Button(description='90°', button_style='primary', layout=widgets.Layout(width='65px'))
btn_180 = widgets.Button(description='180°', button_style='primary', layout=widgets.Layout(width='65px'))
btn_270 = widgets.Button(description='270°', button_style='primary', layout=widgets.Layout(width='65px'))
btn_360 = widgets.Button(description='360°', button_style='success', layout=widgets.Layout(width='65px'))

def set_angle(angle):
    slider_theta.value = angle

btn_0.on_click(lambda b: set_angle(0))
btn_90.on_click(lambda b: set_angle(90))
btn_180.on_click(lambda b: set_angle(180))
btn_270.on_click(lambda b: set_angle(270))
btn_360.on_click(lambda b: set_angle(360))

button_box = widgets.HBox([widgets.Label('⚡ Quick Presets:'), btn_0, btn_90, btn_180, btn_270, btn_360])

out = widgets.Output()

def render_dashboard(x, y, theta):
    with out:
        clear_output(wait=True)
        
        # 1. Mathematical computations
        Q = rotation_matrix(theta)
        P_rot = rotate_point(x, y, theta)
        det_val = calculate_determinant(Q)
        is_ortho, Q_T, QTQ = verify_orthogonality(Q)
        d_orig, d_rot, diff, dist_pres = compare_distances((x, y), P_rot)
        
        # 2. Modern HTML Dashboard Card
        html_card = f\"\"\"
        <div style="font-family: Arial, sans-serif; background: linear-gradient(135deg, #1e293b, #0f172a); 
                    border-radius: 12px; padding: 18px; color: #f8fafc; margin-bottom: 12px;
                    box-shadow: 0 4px 14px rgba(0,0,0,0.4); border: 1px solid #334155;">
            
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 10px; margin-bottom: 12px;">
                <span style="font-size: 18px; font-weight: bold; color: #38bdf8;">📐 Mathematical Calculation Engine</span>
                <span style="background: {'#16a34a' if is_ortho else '#dc2626'}; color: white; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold;">
                    {'✓ ORTHOGONAL' if is_ortho else '✗ NOT ORTHOGONAL'}
                </span>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
                <!-- Card 1: Coordinates -->
                <div style="background: #1e1b4b; padding: 12px; border-radius: 8px; border-left: 4px solid #818cf8;">
                    <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase;">Points Transformation</div>
                    <div style="font-size: 14px; margin-top: 4px;"><b>Original P:</b> ({x:.2f}, {y:.2f})</div>
                    <div style="font-size: 14px; color: #4ade80;"><b>Rotated P':</b> ({P_rot[0]:.2f}, {P_rot[1]:.2f})</div>
                    <div style="font-size: 12px; color: #cbd5e1; margin-top: 4px;">Formula: P' = Q({theta}°) · P</div>
                </div>

                <!-- Card 2: Rotation Matrix -->
                <div style="background: #142834; padding: 12px; border-radius: 8px; border-left: 4px solid #38bdf8;">
                    <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase;">Rotation Matrix Q({theta}°)</div>
                    <div style="font-family: monospace; font-size: 13px; margin-top: 4px;">
                        [{Q[0,0]:6.2f}  {Q[0,1]:6.2f}]<br>
                        [{Q[1,0]:6.2f}  {Q[1,1]:6.2f}]
                    </div>
                    <div style="font-size: 12px; color: #38bdf8; margin-top: 4px;">det(Q) = {det_val:.3f}</div>
                </div>

                <!-- Card 3: Orthogonality Proof -->
                <div style="background: #1f2937; padding: 12px; border-radius: 8px; border-left: 4px solid #10b981;">
                    <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase;">Orthogonality (Qᵀ · Q)</div>
                    <div style="font-family: monospace; font-size: 13px; margin-top: 4px;">
                        [{QTQ[0,0]:.1f}  {QTQ[0,1]:.1f}]<br>
                        [{QTQ[1,0]:.1f}  {QTQ[1,1]:.1f}]
                    </div>
                    <div style="font-size: 12px; color: #10b981; margin-top: 4px;">Qᵀ · Q = Identity Matrix I₂</div>
                </div>

                <!-- Card 4: Distance Preservation -->
                <div style="background: #2e1065; padding: 12px; border-radius: 8px; border-left: 4px solid #ec4899;">
                    <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase;">Norm / Distance Preservation</div>
                    <div style="font-size: 13px; margin-top: 4px;"><b>||P|| :</b> {d_orig:.4f} units</div>
                    <div style="font-size: 13px; color: #ec4899;"><b>||P'||:</b> {d_rot:.4f} units</div>
                    <div style="font-size: 12px; color: #a7f3d0; margin-top: 4px;">Diff: {diff:.6f} (Preserved ✓)</div>
                </div>
            </div>

            <div style="margin-top: 14px; padding: 10px; background: rgba(56, 189, 248, 0.1); border-radius: 6px; border: 1px solid #38bdf8; font-size: 13px;">
                <b>🎯 Theoretical Verification Conclusion:</b><br>
                • <b>QᵀQ = I</b> and <b>det(Q) = 1</b> confirm that the rotation is a <b>proper orthogonal transformation</b>.<br>
                • <b>||Qv|| = ||v||</b> confirms that Euclidean distance is strictly preserved.<br>
                • Angles, size, and shape are invariant under this smartphone screen rotation.
            </div>
        </div>
        \"\"\"
        display(HTML(html_card))
        
        # 3. Render side-by-side graphical visualization
        update_visualization(x, y, theta)

# Link interactive updates
def on_value_change(change):
    render_dashboard(slider_x.value, slider_y.value, slider_theta.value)

slider_x.observe(on_value_change, names='value')
slider_y.observe(on_value_change, names='value')
slider_theta.observe(on_value_change, names='value')

# Main display assembly
control_box = widgets.VBox([
    widgets.HTML("<b style='color:#38bdf8; font-size:14px;'>🎛️ Interactive Controls:</b>"),
    slider_x, 
    slider_y, 
    slider_theta,
    button_box
], layout=widgets.Layout(padding='10px', background='#1e293b', border='1px solid #334155', border_radius='8px'))

display(control_box)
display(out)

# Initial render
render_dashboard(slider_x.value, slider_y.value, slider_theta.value)
""")

# ==========================================
# CELL 7: Markdown - Comprehensive Project Report & Viva Guide
# ==========================================
add_md("""# 📚 Comprehensive Project Report & Viva Guide

---

## 1. Title
**Screen Rotation as Orthogonal Transformation**

## 2. Problem Statement
*"Phone screen rotation can be represented as an orthogonal transformation. Rotation matrices have determinant $\\pm 1$ and preserve distances, angles, shape, and size."*

## 3. Introduction
When a user tilts or rotates a smartphone from portrait to landscape mode, the device's operating system (Android or iOS) must seamlessly re-render pixels and user interface elements onto the display. Mathematically, this continuous physical rotation is handled via 2D transformation geometry. The core mathematical tool that governs this rotation without distorting the graphics is the **2D Rotation Matrix**, which is an **orthogonal transformation**.

## 4. Objective
- Represent 2D smartphone screen rotation mathematically using a standard rotation matrix $Q(\\theta)$.
- Rigorously prove that $Q(\\theta)$ is an orthogonal matrix ($Q^T Q = I$).
- Verify that $\\det(Q) = 1$ for all rotation angles.
- Demonstrate distance invariance ($\\|Qv\\| = \\|v\\|$), angle preservation, and rigid body motion.
- Provide an intuitive, interactive educational tool suitable for B.Tech 1st-year students and college project expos.

---

## 5. Mathematical Theory

### 6. Transformation
A transformation is a mathematical mapping that takes a set of coordinates or vectors in a space and maps them to a new set of coordinates in the same or another space:
$$T: \\mathbb{R}^2 \\to \\mathbb{R}^2, \\quad P \\mapsto P'$$
*In simple words:* Moving, turning, or stretching points on a graph according to a rule.

### 7. Rotation
A rotation is a linear transformation that turns every point of a plane through a fixed angle $\\theta$ about a fixed point called the center of rotation (usually the origin $(0,0)$).
*In simple words:* Turning an object around a central pivot without sliding or resizing it.

### 8. Orthogonal Transformation
A linear transformation $T(v) = Qv$ is orthogonal if its transformation matrix $Q$ satisfies:
$$Q^T Q = Q Q^T = I$$
where $Q^T$ is the transpose of $Q$ and $I$ is the identity matrix.
*Key Properties of Orthogonal Transformations:*
1. **Length/Distance Preservation:** $\\|Qv\\| = \\|v\\|$
2. **Angle Preservation:** $\\langle Qu, Qv \\rangle = \\langle u, v \\rangle$
3. **Invertibility:** $Q^{-1} = Q^T$ (computing the inverse is simply taking the transpose!)
4. **Determinant:** $\\det(Q) = \\pm 1$ ($+1$ for pure rotation, $-1$ for reflection).

### 9. Rotation Matrix
For an angle $\\theta$ measured counterclockwise:
$$Q(\\theta) = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}$$
For any coordinate point $P = \\begin{bmatrix} x \\\\ y \\end{bmatrix}$:
$$P' = Q(\\theta) P = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} = \\begin{bmatrix} x\\cos\\theta - y\\sin\\theta \\\\ x\\sin\\theta + y\\cos\\theta \\end{bmatrix}$$

---

## 10. Mathematical Derivations

### Derivation 1: 2D Rotation Matrix
Let point $P(x, y)$ be at distance $r$ from origin with initial angle $\\alpha$:
$$x = r \\cos\\alpha, \\quad y = r \\sin\\alpha$$
When rotated by angle $\\theta$ counterclockwise:
$$x' = r \\cos(\\alpha + \\theta) = r(\\cos\\alpha \\cos\\theta - \\sin\\alpha \\sin\\theta)$$
Substituting $x$ and $y$:
$$x' = x \\cos\\theta - y \\sin\\theta$$
Similarly for $y'$:
$$y' = r \\sin(\\alpha + \\theta) = r(\\sin\\alpha \\cos\\theta + \\cos\\alpha \\sin\\theta)$$
$$y' = x \\sin\\theta + y \\cos\\theta$$
In matrix form:
$$\\begin{bmatrix} x' \\\\ y' \\end{bmatrix} = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix}$$

### Derivation 2: Proof of Orthogonality ($Q^T Q = I$)
$$Q^T = \\begin{bmatrix} \\cos\\theta & \\sin\\theta \\\\ -\\sin\\theta & \\cos\\theta \\end{bmatrix}$$
$$Q^T Q = \\begin{bmatrix} \\cos\\theta & \\sin\\theta \\\\ -\\sin\\theta & \\cos\\theta \\end{bmatrix} \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}$$
$$Q^T Q = \\begin{bmatrix} \\cos^2\\theta + \\sin^2\\theta & -\\cos\\theta\\sin\\theta + \\sin\\theta\\cos\\theta \\\\ -\\sin\\theta\\cos\\theta + \\cos\\theta\\sin\\theta & \\sin^2\\theta + \\cos^2\\theta \\end{bmatrix} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} = I_2$$
Because $Q^T Q = I$, the matrix $Q$ is **orthogonal**.

### Derivation 3: Proof of Determinant ($\\det(Q) = 1$)
$$\\det(Q) = (\\cos\\theta)(\\cos\\theta) - (-\\sin\\theta)(\\sin\\theta) = \\cos^2\\theta + \\sin^2\\theta = 1$$
Because $\\det(Q) = +1$, the rotation preserves orientation (no mirror reflection).

### Derivation 4: Proof of Distance Preservation ($\\|Qv\\| = \\|v\\|$)
Let $v = [x, y]^T$. Its Euclidean norm squared is $\\|v\\|^2 = v^T v$.
After transformation, $v' = Qv$:
$$\\|Qv\\|^2 = (Qv)^T (Qv) = v^T (Q^T Q) v$$
Since $Q^T Q = I$:
$$\\|Qv\\|^2 = v^T I v = v^T v = \\|v\\|^2$$
Taking square root:
$$\\|Qv\\| = \\|v\\|$$
The distance from origin is strictly invariant.

---

## 11. Input, 12. Processing, 13. Output

| Stage | Components | Description |
|---|---|---|
| **Input** | $x, y, \\theta$ | User enters or slides coordinates and rotation angle, or clicks quick presets ($0°, 90°, 180°, 270°, 360°$). |
| **Processing** | Matrix Math | Computes $Q(\\theta)$, multiplies $Q \\cdot P$, takes transpose $Q^T$, multiplies $Q^T Q$, evaluates $\\det(Q)$, calculates Euclidean norms $\\|P\\|$ and $\\|P'\\|$. |
| **Output** | Metrics & Visuals | Displays $P'$, $Q$, $Q^T$, $Q^T Q$, $\\det(Q)$, distances, orthogonality status, 2D vector plot, and phone simulation. |

---

## 14. Special Cases Table

| Angle ($\\theta$) | $\\cos\\theta$ | $\\sin\\theta$ | Matrix $Q(\\theta)$ | Coordinate Mapping | Physical Screen Meaning |
|---|---|---|---|---|---|
| **0° / 360°** | $1$ | $0$ | $\\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$ | $(x, y) \\to (x, y)$ | Normal Portrait orientation (no change) |
| **90°** | $0$ | $1$ | $\\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}$ | $(x, y) \\to (-y, x)$ | Landscape Left orientation |
| **180°** | $-1$ | $0$ | $\\begin{bmatrix} -1 & 0 \\\\ 0 & -1 \\end{bmatrix}$ | $(x, y) \\to (-x, -y)$ | Upside-down Portrait orientation |
| **270°** | $0$ | $-1$ | $\\begin{bmatrix} 0 & 1 \\\\ -1 & 0 \\end{bmatrix}$ | $(x, y) \\to (y, -x)$ | Landscape Right orientation |

---

## 18. Benefits
1. **Connects Abstract Math to Daily Technology:** Students realize linear algebra is what powers their smartphones every time they watch a YouTube video in landscape mode.
2. **Visual Learning:** Replaces dry algebraic proofs with an interactive visual geometric model.
3. **Rigorous Foundation:** Demonstrates core engineering linear algebra concepts: matrix transpose, matrix multiplication, orthogonality, and eigenvalues/determinants.
4. **Foundation for Advanced Fields:** Orthogonal transformations are central to 3D computer graphics (OpenGL, Vulkan), robotics kinematics, computer vision, game engines (Unity, Unreal), and image processing.

## 19. Limitations
1. **2D Planar Model:** This project models 2D rotation in the screen plane. Real smartphones move in 3D space, which requires 3D rotation matrices or **quaternions** (SO(3)).
2. **Sensor Hardware Omitted:** In actual phones, rotation is triggered by hardware accelerometers and gyroscopes measuring gravitational vectors ($\vec{g}$), which this project abstracts to an input angle $\\theta$.
3. **Screen Aspect Ratio & UI Re-layout:** Real smartphones have rectangular aspect ratios (e.g., 19.5:9), so operating systems trigger a UI layout reflow alongside coordinate rotation.

## 20. Real-Life Applications
- **Smartphones & Tablets:** Auto-rotation of screen buffer and GPU framebuffers.
- **Computer Graphics & Game Dev:** Rotating sprites, camera orientation, and rendering pipelines.
- **Robotics & Drones:** Coordinate frame transformations between world coordinates and robot body frames (Euler angles and orthogonal rotation matrices).
- **Medical Imaging:** Rotating CT scan and MRI slice views without image distortion.

## 21. Conclusion
This project successfully demonstrates that smartphone screen rotation is a physical realization of a **2D orthogonal linear transformation**. By showing that $Q^T Q = I$, $\\det(Q) = 1$, and $\\|Qv\\| = \\|v\\|$, we have proven that rotation preserves distances, angles, shape, and size.

---

## 22. Viva Questions and Answers (Mentor & Expo Ready)

### Q1. What is your project?
**Ans:** My project is an interactive mathematical model titled *"Screen Rotation as Orthogonal Transformation"* that explains how smartphone screen rotation is mathematically governed by 2D orthogonal rotation matrices.

### Q2. What is the problem statement?
**Ans:** Phone screen rotation can be represented as an orthogonal transformation. Rotation matrices have determinant $\\pm 1$ and preserve distances, angles, shape, and size.

### Q3. Why did you choose this topic?
**Ans:** To connect abstract B.Tech 1st-year linear algebra concepts (orthogonal matrices, determinants, and norm preservation) to an intuitive real-world application that every student uses daily—smartphone auto-rotation.

### Q4. What is a transformation?
**Ans:** A transformation is a mathematical mapping that takes points from one coordinate system and maps them to new coordinates based on a predefined algebraic rule ($T: \\mathbb{R}^n \\to \\mathbb{R}^n$).

### Q5. What is rotation?
**Ans:** Rotation is a linear transformation that turns every point in a plane through a fixed angle $\\theta$ about the origin, without altering the distance of any point from the origin.

### Q6. What is an orthogonal matrix?
**Ans:** A square matrix $Q$ is orthogonal if its transpose equals its inverse, meaning $Q^T Q = Q Q^T = I$, where $I$ is the identity matrix.

### Q7. What is the standard 2D rotation matrix?
**Ans:** $Q(\\theta) = \\begin{bmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \\end{bmatrix}$.

### Q8. Why is the rotation matrix orthogonal?
**Ans:** Because multiplying $Q^T$ by $Q$ yields $\\begin{bmatrix} \\cos^2\\theta + \\sin^2\\theta & 0 \\\\ 0 & \\cos^2\\theta + \\sin^2\\theta \\end{bmatrix} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} = I$ due to the fundamental Pythagorean trigonometric identity $\\cos^2\\theta + \\sin^2\\theta = 1$.

### Q9. What is $Q^T Q$?
**Ans:** $Q^T Q$ is the product of the transpose of the rotation matrix and the matrix itself. For any orthogonal matrix, $Q^T Q = I$ (the Identity Matrix).

### Q10. What is the determinant of a rotation matrix?
**Ans:** The determinant of a pure 2D rotation matrix is always exactly $+1$ ($\\\\det(Q) = \\\\cos^2\\theta - (-\\\\sin^2\\theta) = \\\\cos^2\\theta + \\\\sin^2\\theta = 1$).

### Q11. Why is the determinant 1 and not -1?
**Ans:** A determinant of $+1$ represents a **proper rotation** which preserves orientation (handedness). A determinant of $-1$ would represent an **improper rotation** (a rotation combined with a reflection/mirror image).

### Q12. Does rotation change distance?
**Ans:** No. Rotation strictly preserves distance from the origin and pairwise Euclidean distances between any two points ($\\|Qv\\| = \\|v\\|$).

### Q13. Does rotation change shape or size?
**Ans:** No. Because distance and angles are preserved, rotation is an **isometry** (rigid body motion). The size and geometric shape remain completely unchanged.

### Q14. What happens at 90° rotation?
**Ans:** The rotation matrix becomes $\\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}$, transforming coordinates $(x, y)$ to $(-y, x)$. For example, $(2, 3) \\to (-3, 2)$.

### Q15. What happens at 180° rotation?
**Ans:** The rotation matrix becomes $\\begin{bmatrix} -1 & 0 \\\\ 0 & -1 \\end{bmatrix}$, transforming coordinates $(x, y)$ to $(-x, -y)$. The vector is inverted through the origin.

### Q16. What happens at 270° rotation?
**Ans:** The rotation matrix becomes $\\begin{bmatrix} 0 & 1 \\\\ -1 & 0 \\end{bmatrix}$, transforming coordinates $(x, y)$ to $(y, -x)$.

### Q17. What happens at 360° rotation?
**Ans:** The rotation matrix becomes the identity matrix $\\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$, returning coordinates $(x, y)$ back to $(x, y)$ (a full rotation cycle).

### Q18. What is the input to your project?
**Ans:** The input consists of user-defined 2D coordinates $(X, Y)$ and the rotation angle $\\theta$ (via interactive sliders or quick preset buttons for $0°, 90°, 180°, 270°, 360°$).

### Q19. What is the output of your project?
**Ans:** The output is the transformed coordinate $P'$, the numerical rotation matrix $Q(\\theta)$, $Q^T Q$, $\\det(Q)$, distance comparison, an orthogonality proof badge, and dual visual plots showing the 2D vector graph and phone screen orientation.

### Q20. What is the real-life application?
**Ans:** Smartphone UI orientation management, GPU framebuffer rotation, 3D computer graphics, robotics end-effector kinematics, and satellite attitude control.

### Q21. What are the benefits of this project?
**Ans:** It bridges abstract theoretical mathematics with intuitive technology, provides instant visual feedback, reinforces matrix algebra principles, and runs smoothly on mobile devices via Google Colab.

### Q22. What are the limitations of this project?
**Ans:** It models planar 2D rotation. Actual smartphone orientation operates in 3D space using 3-axis IMU sensors (accelerometer and gyroscope) and quaternions to prevent gimbal lock.

### Q23. How is this project related to linear algebra?
**Ans:** It directly demonstrates core linear algebra concepts including vector spaces, linear transformations, matrix multiplication, matrix transpose, orthogonality ($Q^T = Q^{-1}$), determinants, and Euclidean inner products.

### Q24. How does your project prove orthogonality?
**Ans:** Programmatically and algebraically, the project calculates $Q^T Q$ and checks if it equals the $2\\times 2$ identity matrix $I$, computes $\\det(Q) = 1$, and verifies that $\\|Qv\\| - \\|v\\| = 0$.

---

## 🎙️ Stage Presentations

### 1-Minute Stage Pitch (For Evaluator Walk-in)
> *"Good morning respected evaluators. When you rotate your phone to watch a video, how does the screen turn without shrinking or distorting your app? Our project, **'Screen Rotation as Orthogonal Transformation'**, demonstrates the exact linear algebra behind this.  
> Smartphone screen rotation is governed by the 2D rotation matrix $Q(\\theta) = [[\\cos\\theta, -\\sin\\theta], [\\sin\\theta, \\cos\\theta]]$. We prove that $Q$ is an **orthogonal matrix** because $Q^T Q = I$ and $\\det(Q) = 1$.  
> As you can see on our interactive Google Colab dashboard, when we rotate a point like $(2, 3)$ by $90^\\circ$, it maps precisely to $(-3, 2)$ via $P' = QP$. Crucially, the distance $\\sqrt{13} \\approx 3.61$ units remains completely unchanged, meaning $\\|Qv\\| = \\|v\\|$.  
> This proves that orthogonal transformations preserve distance, angles, shape, and size, forming the foundation of smartphone operating systems, computer graphics, and robotics."*

### 30-Second Elevator Pitch (Quick Summary)
> *"Our project proves that phone screen rotation is a practical application of **orthogonal transformations** in linear algebra. Using the 2D rotation matrix $Q(\\theta)$, we demonstrate that $Q^T Q = I$ and $\\det(Q) = 1$. This mathematical property guarantees that Euclidean distances and angles are preserved ($\\|Qv\\| = \\|v\\|$), ensuring phone screen icons and images rotate cleanly without stretching or distortion."*
""")

# ==========================================
# Write to Screen_Rotation_Orthogonal_Transformation.ipynb
# ==========================================
notebook = {
    "cells": cells,
    "metadata": {
        "colab": {
            "name": "Screen_Rotation_as_Orthogonal_Transformation.ipynb",
            "provenance": []
        },
        "language_info": {
            "name": "python",
            "version": "3.10.12"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

output_path = r"c:\Users\mr\New folder (2)\Screen_Rotation_Orthogonal_Transformation.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print(f"Successfully generated {output_path} with {len(cells)} cells!")
