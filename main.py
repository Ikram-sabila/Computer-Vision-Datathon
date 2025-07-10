import cv2
from ultralytics import YOLO

model = YOLO("model/atribut pekerja kontruksi.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera tidak ditemukan.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = model.names[cls]

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        text = f"{label} {conf:.2f}"
        cv2.putText(frame, text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Deteksi Real-time YOLOv8", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()