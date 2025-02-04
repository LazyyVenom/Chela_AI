import pyautogui
from PIL import Image
import cv2

def screen_analysis(model):
    pyautogui.screenshot('SS.png')
    return model.caption(model.encode_image(Image.open("SS.png")), "short")

def camera_analysis(model):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open video device")
    
    ret, frame = cap.read()
    if not ret:
        raise Exception("Failed to capture image")
    
    cv2.imwrite('camera_image.png', frame)
    cap.release()
    cv2.destroyAllWindows()
    return model.caption(model.encode_image(Image.open("camera_image.png")), "short")