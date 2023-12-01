# Module API — Doomscrolling Blocker

This is a standalone script, not a web service. The following documents the public functions in `main.py`.

---

## `load_detector() → cv2.dnn.Net`

Loads the MobileNet SSD Caffe model from `./models/`.

**Raises:** prints a warning and returns `None` if model files are missing (demo mode).

---

## `detect_phone(frame: np.ndarray, net: cv2.dnn.Net) → Tuple[bool, float]`

Runs inference on a single frame.

**Parameters:**
- `frame` — OpenCV BGR frame (H×W×3)
- `net` — loaded DNN net from `load_detector()`

**Returns:** `(phone_detected: bool, confidence: float)`

---

## `play_rickroll() → None`

Opens the Rickroll URL in the system default browser.

---

## `run() → None`

Main entry point. Initialises the webcam, loads the detector, and runs the capture/detect/alert loop until `Q` is pressed.

**Environment variables read:**
- `CAMERA_INDEX` (int, default 0)
- `CONFIDENCE_THRESHOLD` (float, default 0.55)
- `COOLDOWN_SECONDS` (float, default 10)
