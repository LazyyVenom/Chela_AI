import moondream as md
from PIL import Image
import time
import pyautogui

pyautogui.screenshot('SS.png')
start_time = time.time()

model = md.vl(model=r"C:\users\anubhav choubey\Downloads\moondream-2b-int8.mf")
print("Loaded Model in time: ", time.time() - start_time)

image = Image.open(r"SS.png")
encoded_image = model.encode_image(image)
print(model.caption(encoded_image, "short"))
print("total_time: ", time.time() - start_time)