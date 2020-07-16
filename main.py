import pyautogui
import time
from PIL import Image
from datetime import datetime
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

time.sleep(5)
screenshot = pyautogui.screenshot()
now = datetime.now()
current_time = now.strftime("%D %H:%M:%S")
cropped_image = screenshot.crop((50,620,150,660))
result = pytesseract.image_to_string(cropped_image)
previous_result = result
index = 0

while True:
    time.sleep(0.5)
    screenshot = pyautogui.screenshot()
    now = datetime.now()
    current_time = now.strftime("%D %H:%M:%S")
    cropped_image = screenshot.crop((50, 620, 150, 660))
    result = pytesseract.image_to_string(cropped_image)
    if result != previous_result:
        cropped_image.save("images/" + str(index) + ".png")
        print(result + " at " + current_time + "\n")
        f = open("f.txt", "a")
        f.write(str(result) + " at " + str(current_time) + "\n")
        f.close()
        previous_result = result
    index += 1


