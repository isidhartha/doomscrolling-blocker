# Architecture — Doomscrolling Blocker

## Overview

The application is a single-threaded Python process that continuously captures frames from the system webcam, runs object detection, and triggers an alert when a mobile phone is detected.

## Component Breakdown

### Frame Capture Loop
`cv2.VideoCapture` opens the selected camera device (index from `CAMERA_INDEX`). Each iteration reads one frame and passes it to the detection pipeline.

### DNN Blob Preprocessor
OpenCV's `cv2.dnn.blobFromImage` resizes the frame to 300×300 and normalises pixel values to the range expected by MobileNet SSD (mean subtraction of 127.5, scale 0.007843).

### MobileNet SSD Detector
A pretrained Caffe MobileNet SSD model (trained on COCO) runs inference on the blob. COCO class ID 77 corresponds to `cell phone`. If any detection exceeds the confidence threshold, a phone is considered present.

### Cooldown State Machine
A simple timestamp-based guard prevents repeated triggers. Once Rickroll fires, a cooldown period (`COOLDOWN_SECONDS`) must elapse before the next trigger. This avoids a Rickroll storm when the phone remains in frame.

### Alert Dispatcher
`webbrowser.open()` opens the Rickroll URL in the user's default browser. This is intentionally simple and platform-agnostic. It can be swapped for any URL or system command.

## Data Flow

```
Webcam → Frame → Blob → MobileNet SSD → Detections → Class 77 Filter → Confidence Gate → Cooldown Check → webbrowser.open()
```

## Extension Points

- Replace `webbrowser.open` with a system notification, sound alarm, or screen lock
- Swap MobileNet SSD for a fine-tuned YOLO model for higher accuracy
- Add a whitelist of "allowed phone times" using a schedule config
