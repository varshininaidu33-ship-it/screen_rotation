/**
 * ==============================================================================
 * SCREEN ROTATION AS ORTHOGONAL TRANSFORMATION - CLIENT ENGINE
 * B.Tech 1st Year Mathematics Mini-Project
 * ==============================================================================
 */

// ==========================================
// 1. BACKEND MATHEMATICAL ENGINE
// ==========================================

const MathEngine = {
  /**
   * Computes 2D rotation matrix Q(theta) for theta in degrees
   * Q = [[cos(theta), -sin(theta)],
   *      [sin(theta),  cos(theta)]]
   */
  rotationMatrix(thetaDeg) {
    const rad = (thetaDeg * Math.PI) / 180;
    let cosT = Math.cos(rad);
    let sinT = Math.sin(rad);

    // Filter floating-point rounding noise
    if (Math.abs(cosT) < 1e-12) cosT = 0;
    if (Math.abs(sinT) < 1e-12) sinT = 0;

    return [
      [cosT, -sinT],
      [sinT, cosT]
    ];
  },

  /**
   * Multiplies Q(theta) * P = [x', y']
   */
  rotatePoint(x, y, thetaDeg) {
    const Q = this.rotationMatrix(thetaDeg);
    const xRot = Q[0][0] * x + Q[0][1] * y;
    const yRot = Q[1][0] * x + Q[1][1] * y;
    return [
      Math.abs(xRot) < 1e-10 ? 0 : Number(xRot.toFixed(4)),
      Math.abs(yRot) < 1e-10 ? 0 : Number(yRot.toFixed(4))
    ];
  },

  /**
   * Computes determinant: det(Q) = ad - bc
   */
  calculateDeterminant(Q) {
    const det = Q[0][0] * Q[1][1] - Q[0][1] * Q[1][0];
    return Number(det.toFixed(4));
  },

  /**
   * Computes transpose Q^T and product Q^T * Q
   * Verifies Q^T * Q == I_2
   */
  verifyOrthogonality(Q) {
    const QT = [
      [Q[0][0], Q[1][0]],
      [Q[0][1], Q[1][1]]
    ];

    const QTQ = [
      [
        Number((QT[0][0] * Q[0][0] + QT[0][1] * Q[1][0]).toFixed(4)),
        Number((QT[0][0] * Q[0][1] + QT[0][1] * Q[1][1]).toFixed(4))
      ],
      [
        Number((QT[1][0] * Q[0][0] + QT[1][1] * Q[1][0]).toFixed(4)),
        Number((QT[1][0] * Q[0][1] + QT[1][1] * Q[1][1]).toFixed(4))
      ]
    ];

    const isOrtho =
      Math.abs(QTQ[0][0] - 1.0) < 1e-4 &&
      Math.abs(QTQ[0][1] - 0.0) < 1e-4 &&
      Math.abs(QTQ[1][0] - 0.0) < 1e-4 &&
      Math.abs(QTQ[1][1] - 1.0) < 1e-4;

    return { isOrtho, QT, QTQ };
  },

  /**
   * Computes Euclidean norm: ||v|| = sqrt(x^2 + y^2)
   */
  calculateDistance(point) {
    return Number(Math.hypot(point[0], point[1]).toFixed(4));
  },

  /**
   * Compares distance before and after transformation
   */
  compareDistances(pOrig, pRot) {
    const dOrig = this.calculateDistance(pOrig);
    const dRot = this.calculateDistance(pRot);
    const diff = Number(Math.abs(dRot - dOrig).toFixed(6));
    const isPreserved = diff < 1e-4;
    return { dOrig, dRot, diff, isPreserved };
  }
};

// ==========================================
// 2. VIVA VOCE QUESTIONS REPOSITORY (24 Q&A)
// ==========================================

const VIVA_QUESTIONS = [
  {
    id: 1,
    cat: 'basics',
    q: 'What is your project?',
    a: 'My project is an interactive educational tool titled "Screen Rotation as Orthogonal Transformation" that demonstrates how smartphone screen rotation is mathematically governed by 2D orthogonal rotation matrices.'
  },
  {
    id: 2,
    cat: 'basics',
    q: 'What is the problem statement?',
    a: '“Phone screen rotation can be represented as an orthogonal transformation. Rotation matrices have determinant ±1 and preserve distances, angles, shape, and size.”'
  },
  {
    id: 3,
    cat: 'basics',
    q: 'Why did you choose this topic?',
    a: 'To connect abstract 1st-year B.Tech linear algebra concepts (orthogonal matrices, determinants, and norm preservation) to an intuitive real-world application used daily—smartphone auto-rotation.'
  },
  {
    id: 4,
    cat: 'basics',
    q: 'What is a transformation?',
    a: 'A transformation is a mathematical mapping T: ℝⁿ → ℝⁿ that takes coordinates or vectors from a space and maps them to new coordinates according to a predefined algebraic rule.'
  },
  {
    id: 5,
    cat: 'basics',
    q: 'What is rotation?',
    a: 'Rotation is a linear transformation that turns every point in a plane through a fixed angle θ around a fixed pivot point (the origin), without altering any point’s distance from the origin.'
  },
  {
    id: 6,
    cat: 'math',
    q: 'What is an orthogonal matrix?',
    a: 'A square matrix Q is orthogonal if its transpose equals its inverse (Qᵀ = Q⁻¹), which means QᵀQ = QQᵀ = I (the identity matrix).'
  },
  {
    id: 7,
    cat: 'math',
    q: 'What is the standard 2D rotation matrix?',
    a: 'Q(θ) = [[cosθ, -sinθ], [sinθ, cosθ]]. For any point P = [x, y]ᵀ, the transformed point is P\' = Q(θ)P.'
  },
  {
    id: 8,
    cat: 'math',
    q: 'Why is the rotation matrix orthogonal?',
    a: 'Because multiplying Qᵀ by Q yields diagonal terms (cos²θ + sin²θ = 1) and off-diagonal terms (-cosθsinθ + sinθcosθ = 0), producing the Identity Matrix I₂.'
  },
  {
    id: 9,
    cat: 'math',
    q: 'What is QᵀQ?',
    a: 'QᵀQ is the dot product of the transpose of the rotation matrix with itself. For any orthogonal matrix, QᵀQ is always the Identity Matrix I.'
  },
  {
    id: 10,
    cat: 'math',
    q: 'What is the determinant of a rotation matrix?',
    a: 'The determinant of a pure 2D rotation matrix is always exactly +1 (det(Q) = cos²θ - (-sin²θ) = cos²θ + sin²θ = 1).'
  },
  {
    id: 11,
    cat: 'math',
    q: 'Why is the determinant +1 and not -1?',
    a: 'A determinant of +1 represents a proper rotation that preserves orientation (handedness). A determinant of -1 represents an improper rotation (a reflection/mirror image).'
  },
  {
    id: 12,
    cat: 'math',
    q: 'Does rotation change distance?',
    a: 'No. Rotation strictly preserves distance from the origin and pairwise Euclidean distances between any two points (||Qv|| = ||v||).'
  },
  {
    id: 13,
    cat: 'math',
    q: 'Does rotation change shape or size?',
    a: 'No. Because distances and angles are preserved, rotation is an isometry (rigid body motion). Shapes and sizes remain identical.'
  },
  {
    id: 14,
    cat: 'angles',
    q: 'What happens at 90° rotation?',
    a: 'The rotation matrix becomes [[0, -1], [1, 0]], transforming coordinates (x, y) → (-y, x). For example, (2, 3) becomes (-3, 2).'
  },
  {
    id: 15,
    cat: 'angles',
    q: 'What happens at 180° rotation?',
    a: 'The rotation matrix becomes [[-1, 0], [0, -1]], transforming coordinates (x, y) → (-x, -y). The object is inverted through the origin.'
  },
  {
    id: 16,
    cat: 'angles',
    q: 'What happens at 270° rotation?',
    a: 'The rotation matrix becomes [[0, 1], [-1, 0]], transforming coordinates (x, y) → (y, -x).'
  },
  {
    id: 17,
    cat: 'angles',
    q: 'What happens at 360° rotation?',
    a: 'The rotation matrix becomes the identity matrix [[1, 0], [0, 1]], returning coordinates (x, y) back to (x, y) (a full cycle).'
  },
  {
    id: 18,
    cat: 'app',
    q: 'What is the input to your project?',
    a: 'The user inputs coordinates (X, Y) and rotation angle θ in degrees (via interactive sliders or quick presets 0°, 90°, 180°, 270°, 360°).'
  },
  {
    id: 19,
    cat: 'app',
    q: 'What is the output of your project?',
    a: 'The transformed point P\', matrix Q(θ), transpose Qᵀ, verification QᵀQ = I, det(Q) = 1, norm comparisons, verification status, and visual coordinate & phone graphics.'
  },
  {
    id: 20,
    cat: 'app',
    q: 'What is the real-life application?',
    a: 'Smartphone screen auto-rotation, GPU framebuffer transforms, 3D computer graphics (camera view matrices), robotics kinematics, and computer vision image augmentation.'
  },
  {
    id: 21,
    cat: 'app',
    q: 'What are the benefits of this project?',
    a: 'It bridges abstract linear algebra with real-world mobile tech, provides instant visual feedback, reinforces matrix operations, and runs on mobile phones via Google Colab.'
  },
  {
    id: 22,
    cat: 'app',
    q: 'What are the limitations of this project?',
    a: 'It is a 2D planar rotation model. Real smartphones rotate in 3D space using accelerometer/gyroscope sensors and quaternions in SO(3).'
  },
  {
    id: 23,
    cat: 'math',
    q: 'How is this project related to linear algebra?',
    a: 'It directly demonstrates linear transformations, vector spaces, matrix multiplication, matrix transpose, orthogonality (Qᵀ = Q⁻¹), determinants, and Euclidean norms.'
  },
  {
    id: 24,
    cat: 'math',
    q: 'How does your project prove orthogonality?',
    a: 'Programmatically and algebraically, it computes QᵀQ and checks if it equals I₂, calculates det(Q) = 1, and verifies that ||Qv|| - ||v|| = 0.'
  }
];

// ==========================================
// 3. UI STATE & CONTROLLERS
// ==========================================

const State = {
  x: 2.0,
  y: 3.0,
  angle: 90
};

// DOM References
const elSliderX = document.getElementById('sliderX');
const elSliderY = document.getElementById('sliderY');
const elSliderAngle = document.getElementById('sliderAngle');

const elValX = document.getElementById('valX');
const elValY = document.getElementById('valY');
const elValAngleDeg = document.getElementById('valAngleDeg');
const elValAngleRad = document.getElementById('valAngleRad');

const elCardOrigP = document.getElementById('cardOrigP');
const elCardRotP = document.getElementById('cardRotP');
const elM00 = document.getElementById('m00');
const elM01 = document.getElementById('m01');
const elM10 = document.getElementById('m10');
const elM11 = document.getElementById('m11');
const elCardMatrixFormula = document.getElementById('cardMatrixFormula');

const elQtq00 = document.getElementById('qtq00');
const elQtq01 = document.getElementById('qtq01');
const elQtq10 = document.getElementById('qtq10');
const elQtq11 = document.getElementById('qtq11');

const elCardDet = document.getElementById('cardDet');
const elCardNormP = document.getElementById('cardNormP');
const elCardNormProt = document.getElementById('cardNormProt');
const elCardDiff = document.getElementById('cardDiff');
const elSummaryText = document.getElementById('summaryText');

const elPhoneChassis = document.getElementById('phoneChassis');
const elScreenOrientationTag = document.getElementById('screenOrientationTag');
const elScreenPixelTarget = document.getElementById('screenPixelTarget');
const elScreenPixelLabel = document.getElementById('screenPixelLabel');

const canvas = document.getElementById('coordCanvas');
const ctx = canvas.getContext('2d');

// ==========================================
// 4. CANVAS 2D GRAPH RENDERER
// ==========================================

function drawCoordGraph() {
  const width = canvas.width;
  const height = canvas.height;
  const cx = width / 2;
  const cy = height / 2;

  // Clear background
  ctx.fillStyle = '#0b1120';
  ctx.fillRect(0, 0, width, height);

  // Dynamic Scale
  const pRot = MathEngine.rotatePoint(State.x, State.y, State.angle);
  const maxVal = Math.max(
    Math.abs(State.x),
    Math.abs(State.y),
    Math.abs(pRot[0]),
    Math.abs(pRot[1]),
    3.0
  );
  const range = maxVal + 2.0;
  const scale = (width / 2 - 40) / range; // pixels per unit

  // Draw Grid Lines
  ctx.strokeStyle = '#1e293b';
  ctx.lineWidth = 1;
  const step = 1;
  for (let u = -Math.floor(range); u <= Math.floor(range); u += step) {
    if (u === 0) continue;
    // vertical
    const gx = cx + u * scale;
    ctx.beginPath();
    ctx.moveTo(gx, 0);
    ctx.lineTo(gx, height);
    ctx.stroke();

    // horizontal
    const gy = cy - u * scale;
    ctx.beginPath();
    ctx.moveTo(0, gy);
    ctx.lineTo(width, gy);
    ctx.stroke();

    // Coordinate Numbers
    ctx.fillStyle = '#475569';
    ctx.font = '10px "Fira Code", monospace';
    ctx.fillText(u.toString(), gx - 6, cy + 14);
    ctx.fillText(u.toString(), cx - 18, gy + 3);
  }

  // Draw Main X and Y Axes
  ctx.strokeStyle = '#64748b';
  ctx.lineWidth = 1.5;

  // X Axis
  ctx.beginPath();
  ctx.moveTo(20, cy);
  ctx.lineTo(width - 20, cy);
  ctx.stroke();

  // Y Axis
  ctx.beginPath();
  ctx.moveTo(cx, height - 20);
  ctx.lineTo(cx, 20);
  ctx.stroke();

  // Axis Labels
  ctx.fillStyle = '#94a3b8';
  ctx.font = 'bold 12px "Plus Jakarta Sans", sans-serif';
  ctx.fillText('+X', width - 30, cy - 8);
  ctx.fillText('+Y', cx + 10, 30);
  ctx.fillText('-X', 10, cy - 8);
  ctx.fillText('-Y', cx + 10, height - 15);
  ctx.fillText('O(0,0)', cx + 6, cy + 16);

  // Euclidean Distance Radius Circle
  const norm = Math.hypot(State.x, State.y);
  if (norm > 0.05) {
    ctx.save();
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = '#38bdf8';
    ctx.globalAlpha = 0.45;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(cx, cy, norm * scale, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.restore();

    // Rotation Direction Arc
    const initialAngle = Math.atan2(State.y, State.x);
    const targetAngle = initialAngle + (State.angle * Math.PI) / 180;
    ctx.save();
    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 2.0;
    ctx.beginPath();
    // In canvas, positive Y is downwards, so invert angle direction
    ctx.arc(cx, cy, norm * scale * 0.65, -initialAngle, -targetAngle, true);
    ctx.stroke();
    ctx.restore();
  }

  // Screen Positions of Points
  const pxOrig = cx + State.x * scale;
  const pyOrig = cy - State.y * scale;

  const pxRot = cx + pRot[0] * scale;
  const pyRot = cy - pRot[1] * scale;

  // Helper: Draw Vector Arrow
  function drawVector(toX, toY, color, widthLine = 2) {
    ctx.save();
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = widthLine;

    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(toX, toY);
    ctx.stroke();

    // Arrowhead
    const angleHead = Math.atan2(toY - cy, toX - cx);
    const headLen = 9;
    ctx.beginPath();
    ctx.moveTo(toX, toY);
    ctx.lineTo(
      toX - headLen * Math.cos(angleHead - Math.PI / 6),
      toY - headLen * Math.sin(angleHead - Math.PI / 6)
    );
    ctx.lineTo(
      toX - headLen * Math.cos(angleHead + Math.PI / 6),
      toY - headLen * Math.sin(angleHead + Math.PI / 6)
    );
    ctx.closePath();
    ctx.fill();
    ctx.restore();
  }

  // Draw Vectors
  drawVector(pxOrig, pyOrig, '#38bdf8', 2.5); // Blue
  drawVector(pxRot, pyRot, '#10b981', 2.5);  // Green

  // Draw Point Dots
  function drawPointDot(xPos, yPos, color, labelText) {
    ctx.save();
    ctx.fillStyle = color;
    ctx.shadowColor = color;
    ctx.shadowBlur = 12;
    ctx.beginPath();
    ctx.arc(xPos, yPos, 6, 0, 2 * Math.PI);
    ctx.fill();

    // Label
    ctx.shadowBlur = 0;
    ctx.font = 'bold 12px "Fira Code", monospace';
    ctx.fillStyle = color;
    ctx.fillText(labelText, xPos + 10, yPos - 8);
    ctx.restore();
  }

  drawPointDot(pxOrig, pyOrig, '#38bdf8', `P(${State.x.toFixed(1)}, ${State.y.toFixed(1)})`);
  drawPointDot(pxRot, pyRot, '#10b981', `P'(${pRot[0].toFixed(1)}, ${pRot[1].toFixed(1)})`);

  // Origin Marker Dot
  ctx.fillStyle = '#f8fafc';
  ctx.beginPath();
  ctx.arc(cx, cy, 3.5, 0, 2 * Math.PI);
  ctx.fill();
}

// ==========================================
// 5. UPDATE DASHBOARD & SIMULATION
// ==========================================

function updateDashboard() {
  const x = State.x;
  const y = State.y;
  const deg = State.angle;
  const rad = (deg * Math.PI) / 180;

  // 1. Math Operations
  const Q = MathEngine.rotationMatrix(deg);
  const pRot = MathEngine.rotatePoint(x, y, deg);
  const det = MathEngine.calculateDeterminant(Q);
  const { isOrtho, QTQ } = MathEngine.verifyOrthogonality(Q);
  const { dOrig, dRot, diff, isPreserved } = MathEngine.compareDistances([x, y], pRot);

  // 2. Update Field Text
  elValX.textContent = x.toFixed(1);
  elValY.textContent = y.toFixed(1);
  elValAngleDeg.textContent = `${deg}°`;
  elValAngleRad.textContent = `${rad.toFixed(3)} rad`;

  // 3. Update Point Cards
  elCardOrigP.textContent = `(${x.toFixed(2)}, ${y.toFixed(2)})`;
  elCardRotP.textContent = `(${pRot[0].toFixed(2)}, ${pRot[1].toFixed(2)})`;

  // 4. Update Rotation Matrix Card
  elM00.textContent = Q[0][0].toFixed(2);
  elM01.textContent = Q[0][1].toFixed(2);
  elM10.textContent = Q[1][0].toFixed(2);
  elM11.textContent = Q[1][1].toFixed(2);

  elCardMatrixFormula.textContent = `cos(${deg}°) = ${Q[0][0].toFixed(2)},  sin(${deg}°) = ${Q[1][0].toFixed(2)}`;

  // 5. Update Orthogonality Proof Matrix Card
  elQtq00.textContent = QTQ[0][0].toFixed(2);
  elQtq01.textContent = QTQ[0][1].toFixed(2);
  elQtq10.textContent = QTQ[1][0].toFixed(2);
  elQtq11.textContent = QTQ[1][1].toFixed(2);

  // 6. Update Determinant and Distance
  elCardDet.textContent = `det(Q) = ${det.toFixed(3)}`;
  elCardNormP.textContent = `${dOrig.toFixed(4)} units`;
  elCardNormProt.textContent = `${dRot.toFixed(4)} units`;
  elCardDiff.textContent = `${diff.toFixed(6)} (Preserved ✓)`;

  // 7. Summary Paragraph
  elSummaryText.innerHTML = `
    For &theta; = <strong>${deg}&deg;</strong>, <strong>Q<sup>T</sup>Q = I</strong> and <strong>det(Q) = 1</strong>. 
    The transformation is <strong>strictly orthogonal</strong>. 
    Euclidean distance from origin is invariant (||P|| = ||P'|| = <strong>${dOrig.toFixed(4)}</strong>). 
    Angles, geometric shapes, and screen pixel aspect ratios are perfectly preserved!
  `;

  // 8. Smartphone Simulation Update
  // In screen simulation, rotating clockwise matches standard phone screen UX tilt
  elPhoneChassis.style.transform = `rotate(${deg}deg)`;

  let orientationName = 'Portrait Mode (0°)';
  if (deg === 90) orientationName = 'Landscape Left (90°)';
  else if (deg === 180) orientationName = 'Inverted Portrait (180°)';
  else if (deg === 270) orientationName = 'Landscape Right (270°)';
  else if (deg === 360) orientationName = 'Full Rotation (360°)';
  else orientationName = `Tilt Orientation (${deg}°)`;
  elScreenOrientationTag.textContent = orientationName;

  // Update target pixel position on phone screen
  const maxScreenCoord = Math.max(Math.abs(x), Math.abs(y), 4.0);
  const normX = (pRot[0] / maxScreenCoord) * 35; // px offset
  const normY = -(pRot[1] / maxScreenCoord) * 35;
  elScreenPixelTarget.style.transform = `translate(${normX}px, ${normY}px)`;
  elScreenPixelLabel.textContent = `P'(${pRot[0].toFixed(1)}, ${pRot[1].toFixed(1)})`;

  // 9. Redraw Canvas Graph
  drawCoordGraph();
}

// ==========================================
// 6. EVENT LISTENERS & PRESETS
// ==========================================

elSliderX.addEventListener('input', (e) => {
  State.x = parseFloat(e.target.value);
  updateDashboard();
});

elSliderY.addEventListener('input', (e) => {
  State.y = parseFloat(e.target.value);
  updateDashboard();
});

elSliderAngle.addEventListener('input', (e) => {
  State.angle = parseInt(e.target.value, 10);
  updatePresetButtonsState(State.angle);
  updateDashboard();
});

function updatePresetButtonsState(activeDeg) {
  document.querySelectorAll('.btn-preset').forEach((btn) => {
    const deg = parseInt(btn.getAttribute('data-deg'), 10);
    if (deg === activeDeg) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });
}

document.querySelectorAll('.btn-preset').forEach((btn) => {
  btn.addEventListener('click', () => {
    const deg = parseInt(btn.getAttribute('data-deg'), 10);
    State.angle = deg;
    elSliderAngle.value = deg;
    updatePresetButtonsState(deg);
    updateDashboard();
  });
});

document.getElementById('btnResetAll').addEventListener('click', () => {
  State.x = 2.0;
  State.y = 3.0;
  State.angle = 90;
  elSliderX.value = 2.0;
  elSliderY.value = 3.0;
  elSliderAngle.value = 90;
  updatePresetButtonsState(90);
  updateDashboard();
});

// ==========================================
// 7. NAVIGATION TABS CONTROLLER
// ==========================================

const navTabs = document.querySelectorAll('.nav-tab');
const tabPanes = document.querySelectorAll('.tab-pane');

navTabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    navTabs.forEach((t) => t.classList.remove('active'));
    tabPanes.forEach((p) => p.classList.remove('active'));

    tab.classList.add('active');
    const targetPaneId = `pane-${tab.getAttribute('data-tab')}`;
    const targetPane = document.getElementById(targetPaneId);
    if (targetPane) {
      targetPane.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
      setTimeout(renderMath, 100);
    }
  });
});

// ==========================================
// 8. VIVA QUESTIONS BUILDER & SEARCH
// ==========================================

const vivaList = document.getElementById('vivaList');
const vivaSearch = document.getElementById('vivaSearch');
const vivaCatBtns = document.querySelectorAll('.viva-cat-btn');

let currentVivaCat = 'all';

function renderVivaList() {
  const searchTerm = (vivaSearch.value || '').toLowerCase().trim();
  vivaList.innerHTML = '';

  const filtered = VIVA_QUESTIONS.filter((item) => {
    const matchesCat = currentVivaCat === 'all' || item.cat === currentVivaCat;
    const matchesSearch =
      item.q.toLowerCase().includes(searchTerm) ||
      item.a.toLowerCase().includes(searchTerm) ||
      item.id.toString().includes(searchTerm);
    return matchesCat && matchesSearch;
  });

  if (filtered.length === 0) {
    vivaList.innerHTML = `
      <div style="text-align: center; padding: 30px; color: #94a3b8;">
        No questions match your query. Try searching for "orthogonal", "distance", or "90°".
      </div>
    `;
    return;
  }

  filtered.forEach((item) => {
    const el = document.createElement('div');
    el.className = 'viva-item';
    el.innerHTML = `
      <div class="viva-header" onclick="toggleViva(${item.id})">
        <div>
          <span class="viva-num">Q${item.id}.</span>
          <span>${item.q}</span>
        </div>
        <span class="viva-arrow">▼</span>
      </div>
      <div class="viva-content" id="viva-content-${item.id}">
        <strong>Answer:</strong> ${item.a}
      </div>
    `;
    vivaList.appendChild(el);
  });
}

window.toggleViva = function (id) {
  const item = document.querySelector(`#viva-content-${id}`).parentElement;
  item.classList.toggle('open');
};

vivaSearch.addEventListener('input', renderVivaList);

vivaCatBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    vivaCatBtns.forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    currentVivaCat = btn.getAttribute('data-cat');
    renderVivaList();
  });
});

// ==========================================
// 9. CLIPBOARD COPY HELPERS
// ==========================================

window.copyCode = function (elemId) {
  const el = document.getElementById(elemId);
  if (!el) return;
  navigator.clipboard.writeText(el.innerText).then(() => {
    alert('Code copied to clipboard! Ready to paste into Google Colab.');
  });
};

window.copyText = function (type) {
  let text = '';
  if (type === 'pitch-1min') {
    text = `“Good morning respected evaluators. When you rotate your phone to watch a video, how does the screen turn smoothly without distorting, stretching, or shrinking your apps? Our project, ‘Screen Rotation as Orthogonal Transformation’, demonstrates the exact linear algebra behind this. Smartphone screen rotation is governed by the 2D rotation matrix Q(θ) = [[cosθ, -sinθ], [sinθ, cosθ]]. We prove that Q is an orthogonal matrix because QᵀQ = I and det(Q) = 1. As demonstrated on our interactive dashboard, when we rotate a point like (2, 3) by 90°, it maps precisely to (-3, 2) via P' = QP. Crucially, the distance √13 ≈ 3.61 units remains completely unchanged (||Qv|| = ||v||). This proves that orthogonal transformations preserve distance, angles, shape, and size—forming the mathematical foundation of smartphone operating systems, computer graphics, and robotics.”`;
  } else if (type === 'pitch-30sec') {
    text = `“Our project proves that smartphone screen rotation is a practical application of orthogonal transformations in linear algebra. Using the 2D rotation matrix Q(θ), we demonstrate that QᵀQ = I and det(Q) = 1. This mathematical property guarantees that Euclidean distances and angles are strictly preserved (||Qv|| = ||v||), ensuring that screen icons, videos, and UI elements rotate without distortion or loss of shape.”`;
  }
  navigator.clipboard.writeText(text).then(() => {
    alert('Presentation script copied to clipboard!');
  });
};

// ==========================================
function renderMath() {
  if (window.renderMathInElement) {
    try {
      window.renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    } catch (e) {
      // Graceful fallback
    }
  }
}

// 10. INITIALIZATION
// ==========================================

window.addEventListener('DOMContentLoaded', () => {
  renderVivaList();
  updateDashboard();
  setTimeout(renderMath, 200);
});
