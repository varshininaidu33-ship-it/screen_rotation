"""
================================================================================
Screen Rotation as Orthogonal Transformation
B.Tech 1st-Year Mathematics Mini-Project
================================================================================
"""

import math

def rotation_matrix(theta_deg):
    """Computes 2D rotation matrix Q(theta)"""
    rad = math.radians(theta_deg)
    c = math.cos(rad)
    s = math.sin(rad)
    if abs(c) < 1e-12: c = 0.0
    if abs(s) < 1e-12: s = 0.0
    return [[round(c, 4), round(-s, 4)],
            [round(s, 4), round(c, 4)]]

def rotate_point(x, y, theta_deg):
    """P' = Q * P"""
    Q = rotation_matrix(theta_deg)
    x_rot = Q[0][0] * x + Q[0][1] * y
    y_rot = Q[1][0] * x + Q[1][1] * y
    return round(x_rot, 4), round(y_rot, 4)

def calculate_determinant(Q):
    """det(Q) = ad - bc"""
    return round(Q[0][0] * Q[1][1] - Q[0][1] * Q[1][0], 4)

def verify_orthogonality(Q):
    """Verifies Q^T * Q == I"""
    # Q^T
    QT = [[Q[0][0], Q[1][0]],
          [Q[0][1], Q[1][1]]]
    # QT * Q
    QTQ = [
        [round(QT[0][0]*Q[0][0] + QT[0][1]*Q[1][0], 4), round(QT[0][0]*Q[0][1] + QT[0][1]*Q[1][1], 4)],
        [round(QT[1][0]*Q[0][0] + QT[1][1]*Q[1][0], 4), round(QT[1][0]*Q[0][1] + QT[1][1]*Q[1][1], 4)]
    ]
    is_ortho = (QTQ[0][0] == 1.0 and QTQ[0][1] == 0.0 and QTQ[1][0] == 0.0 and QTQ[1][1] == 1.0)
    return is_ortho, QT, QTQ

def calculate_distance(point):
    """||v|| = sqrt(x^2 + y^2)"""
    return round(math.sqrt(point[0]**2 + point[1]**2), 4)

def compare_distances(p1, p2):
    """Compares ||P|| with ||P'||"""
    d1 = calculate_distance(p1)
    d2 = calculate_distance(p2)
    diff = round(abs(d1 - d2), 6)
    return d1, d2, diff, diff < 1e-4

def run_demonstration(x=2.0, y=3.0, theta=90.0):
    Q = rotation_matrix(theta)
    P_rot = rotate_point(x, y, theta)
    det_val = calculate_determinant(Q)
    is_ortho, QT, QTQ = verify_orthogonality(Q)
    d_orig, d_rot, diff, dist_pres = compare_distances((x, y), P_rot)

    print("=" * 65)
    print("  SCREEN ROTATION AS ORTHOGONAL TRANSFORMATION (MATHEMATICS)")
    print("=" * 65)
    print(f"Original Point P          : ({x}, {y})")
    print(f"Rotation Angle theta      : {theta} deg")
    print(f"Rotation Matrix Q({theta}°):")
    print(f"   [{Q[0][0]:6.2f}  {Q[0][1]:6.2f}]")
    print(f"   [{Q[1][0]:6.2f}  {Q[1][1]:6.2f}]")
    print(f"Transformed Point P'      : ({P_rot[0]}, {P_rot[1]})")
    print("-" * 65)
    print("Transpose Matrix Q^T      :")
    print(f"   [{QT[0][0]:6.2f}  {QT[0][1]:6.2f}]")
    print(f"   [{QT[1][0]:6.2f}  {QT[1][1]:6.2f}]")
    print("Product Q^T * Q           :")
    print(f"   [{QTQ[0][0]:6.2f}  {QTQ[0][1]:6.2f}]")
    print(f"   [{QTQ[1][0]:6.2f}  {QTQ[1][1]:6.2f}]")
    print(f"Determinant det(Q)        : {det_val}")
    print("-" * 65)
    print(f"Original Distance ||P||   : {d_orig} units")
    print(f"Rotated Distance ||P'||  : {d_rot} units")
    print(f"Distance Difference       : {diff} units")
    print("-" * 65)
    print(f"STATUS: Q^T * Q == I?     : {'YES (Identity Matrix)' if is_ortho else 'NO'}")
    print(f"STATUS: Orthogonal?       : {'The transformation is orthogonal.' if is_ortho else 'Not orthogonal.'}")
    print(f"STATUS: Distance Check    : {'Distance is preserved.' if dist_pres else 'Distance changed.'}")
    print("=" * 65)

if __name__ == "__main__":
    print("\n--- TEST CASE: WORKED EXAMPLE (P=(2,3), theta=90 deg) ---")
    run_demonstration(2.0, 3.0, 90.0)

    print("\n--- TEST CASE: 180 DEGREE ROTATION ---")
    run_demonstration(2.0, 3.0, 180.0)

    print("\n--- TEST CASE: 270 DEGREE ROTATION ---")
    run_demonstration(2.0, 3.0, 270.0)
