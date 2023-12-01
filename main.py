"""
Doomscrolling Blocker
Detects when you're looking at your phone via webcam and plays Rickroll as punishment.
"""

import cv2
import webbrowser
import time
import numpy as np

RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
COOLDOWN_SECONDS = 10
PHONE_CONFIDENCE_THRESHOLD = 0.55


def load_detector():
    # Uses a lightweight MobileNet SSD pretrained on COCO (class 77 = cell phone)
    net = cv2.dnn.readNetFromCaffe(
        "models/MobileNetSSD_deploy.prototxt",
        "models/MobileNetSSD_deploy.caffemodel",
    )
    return net


def detect_phone(frame, net):
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5
    )
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        class_id = int(detections[0, 0, i, 1])
        # COCO class 77 = cell phone
        if class_id == 77 and confidence > PHONE_CONFIDENCE_THRESHOLD:
            return True, confidence
    return False, 0.0


def play_rickroll():
    print("[!] Phone detected — enjoy your punishment.")
    webbrowser.open(RICKROLL_URL)


def run():
    print("Doomscrolling Blocker started. Press Q to quit.")
    try:
        net = load_detector()
    except Exception:
        print(
            "[WARN] Model files not found in ./models/. Run download_models.py first.\n"
            "       Running in demo mode (no detection)."
        )
        net = None

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Cannot open webcam.")
        return

    last_triggered = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        phone_found = False
        if net is not None:
            phone_found, conf = detect_phone(frame, net)
            if phone_found:
                cv2.putText(
                    frame,
                    f"PHONE DETECTED ({conf:.0%})",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                )

        cv2.imshow("Doomscrolling Blocker", frame)

        now = time.time()
        if phone_found and (now - last_triggered) > COOLDOWN_SECONDS:
            last_triggered = now
            play_rickroll()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()
