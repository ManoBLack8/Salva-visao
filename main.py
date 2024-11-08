import cv2
import mediapipe as mp
import tkinter as tk
from tkinter import Label

def show_alert():
    alert = tk.Tk()
    alert.attributes("-topmost", True)
    alert.attributes("-fullscreen", True)
    alert.configure(bg="red")
    label = Label(alert, text="Rosto muito próximo!", font=("Helvetica", 32), bg="red", fg="white")
    label.pack(expand=True)
    alert.after(2000, alert.destroy)  # Fecha a janela após 2 segundos
    alert.mainloop()

mp_face_detection = mp.solutions.face_detection
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignorando o frame vazio da câmera.")
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                
                if w > 220:
                    color = (0, 0, 255)
                    show_alert()  # Mostra a janela de alerta
                else:
                    color = (0, 255, 0)
                    
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                size_text = f"{w}x{h}"
                cv2.putText(image, size_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        #cv2.imshow('Face Detection', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
