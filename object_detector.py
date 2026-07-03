import cv2
import numpy as np

prototxt = 'MobileNetSSD_deploy.prototxt'
caffemodel = 'MobileNetSSD_deploy.caffemodel'
img_path = 'test_image.jpg'

print("Loading model...")
# قراءة الموديل مباشرة
net = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)

image = cv2.imread(img_path)
(h, w) = image.shape[:2]

blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()

print("\n--- Object Detection Output ---")
for i in range(np.shape(detections)[2]):
    confidence = detections[0, 0, i, 2]
    if confidence >= 0.80:
        class_id = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        print(f"Object ID: {class_id} | Confidence: {confidence*100:.2f}%")
        print(f"Bounding Box Coordinates: ({startX}, {startY}) to ({endX}, {endY})")
print("-" * 31)