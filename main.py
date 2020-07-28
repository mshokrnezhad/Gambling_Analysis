import pyautogui
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe' # set the path based of your config
screenshot = pyautogui.screenshot() # taking screenshot
cropped_image = screenshot.crop((390, 100, 1200, 500)) # Adjusting margins
imgplot = plt.imshow(cropped_image)
plt.show() # Using this demonstration, you can adjust margins at Line 7 to get what text you want from the screen
line = pytesseract.image_to_string(cropped_image)
print(line)