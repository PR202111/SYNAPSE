# ocr_yolo.py
import cv2
import easyocr
from ultralytics import YOLO
from config import CLASS_NAMES, YOLO_MODEL_PATH

reader = easyocr.Reader(['en'], gpu=False)
yolo_model = YOLO(YOLO_MODEL_PATH)

def capture_image():
    cap = cv2.VideoCapture(0)
    print("Press SPACE to capture, ESC to exit")
    captured_file = None

    while True:
        ret, frame = cap.read()
        cv2.imshow("Camera - Medicine Assistant", frame)
        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE
            captured_file = "captured.jpg"
            cv2.imwrite(captured_file, frame)
            print("Image captured!")
            break

    cap.release()
    cv2.destroyAllWindows()
    return captured_file

def process_image(image_path):
    # OCR
    ocr_result = reader.readtext(image_path, detail=0, paragraph=True)
    extracted_text = " ".join(ocr_result)
    print(f"Extracted Text: {extracted_text}")

    # YOLO detection
    results = yolo_model.predict(image_path)
    best_conf = 0
    best_class = None

    for result in results:
        if len(result.boxes) > 0:
            boxes = result.boxes.xyxy.cpu().numpy()
            confidences = result.boxes.conf.cpu().numpy()
            class_ids = result.boxes.cls.cpu().numpy()
            best_index = confidences.argmax()
            best_conf = confidences[best_index]
            best_class = int(class_ids[best_index])

    medicine_name = CLASS_NAMES[best_class] if best_class is not None else "Unknown medicine"
    return medicine_name, extracted_text
