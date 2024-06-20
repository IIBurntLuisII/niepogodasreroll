import ctypes
import pytesseract
import re
import time
import threading
import pydirectinput
import keyboard
import cv2
import json
import os
import logging
from PIL import ImageGrab
from tkinter import Tk, messagebox

# Setup logging
try:
    os.remove("latest.log")
except FileNotFoundError:
    pass

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log_filename = "latest.log"
file_handler = logging.FileHandler(log_filename)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)

# Configure pytesseract
# Comment out the line below if tesseract is in the PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load configuration
try:
    with open("config.json") as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    logging.error("config.json not found! Please place it in the script's directory.")
    exit()
except json.JSONDecodeError as e:
    logging.error(f"Error decoding config.json: {e}")
    exit()

try:
    with open("regions.json") as regions_file:
        regions = json.load(regions_file)
except FileNotFoundError:
    logging.error("regions.json not found! Please run the region selector script first.")
    exit()
except json.JSONDecodeError as e:
    logging.error(f"Error decoding regions.json: {e}")
    exit()

DELAY = config["delay"]
START_KEYBIND = config["start_keybind"]
KILL_KEYBIND = config["kill_keybind"]

logging.info("Config loaded: {}".format(config))
logging.info("Regions loaded: {}".format(regions))

running = True

def getChests(quest_number):
    bbox_map = {
        1: (regions["regions"]["quest1"]),
        2: (regions["regions"]["quest2"]),
        3: (regions["regions"]["quest3"]),
        4: (regions["regions"]["quest4"])
    }
    if quest_number not in bbox_map:
        return ["0"]
    
    bbox = bbox_map[quest_number]
    quest_screenshot = ImageGrab.grab(bbox=bbox)
    filename = f'quest{quest_number}.png'
    quest_screenshot.save(filename)

    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cv2.imwrite(filename, thresh)

    try:
        OCR_result = pytesseract.image_to_string(thresh)
        logging.info(f"Successfully read quest {quest_number} content: {OCR_result}")
        if quest_number in [1, 2, 3]:
            filtered = [re.search(r'(\d+)', item).group(1) for item in OCR_result.split('\n') if "artifact chest" in item.lower()]
        elif quest_number == 4:
            filtered = [re.search(r'(\d+)', item).group(1) for item in OCR_result.split('\n') if "diamond chest" in item.lower()]
        else:
            filtered = ["0"]
    except Exception as e:
        logging.error(f"Error reading quest {quest_number} content: {e}")
        filtered = ["0"]

    if not filtered:
        filtered = ["0"]
        
    logging.info(f"Filtered result for quest {quest_number}: {filtered}")
    logging.info(f"Found {filtered[0]} artifact chests in quest {quest_number}")
    return filtered

def reroll(quest_number):
    coordinates = {
        1: (regions["buttons"]["reroll1"]),
        2: (regions["buttons"]["reroll2"]),
        3: (regions["buttons"]["reroll3"]),
        4: (regions["buttons"]["reroll4"])
    }
    if quest_number not in coordinates:
        return
    
    x, y = coordinates[quest_number]
    pydirectinput.moveTo(x, y)
    pydirectinput.moveTo(x+1, y+1)
    pydirectinput.click()

    logging.info(f"Rerolling chest {quest_number}... Waiting for contents to refresh...")

def main_loop():
    global running
    logging.info(f"Script loaded! Press {START_KEYBIND} to start rerolling. Press {KILL_KEYBIND} to exit.")
    while running:
        time.sleep(0.001)
        if keyboard.is_pressed(START_KEYBIND):
            time.sleep(0.2)
            for quest_number in range(1, 5):  # Changed range to include quest 4
                while True:
                    chest_count = int(getChests(quest_number)[0])
                    if chest_count >= config["minimum_chests"][f"quest{quest_number}"]:
                        logging.info(f"Quest {quest_number} has enough chests: {chest_count}")
                        break
                    reroll(quest_number)
                    time.sleep(DELAY)

def killswitch():
    global running
    keyboard.wait(KILL_KEYBIND)
    running = False
    cleanup()
    os._exit(0)

def cleanup():
    logging.info("Cleaning up temporary files...")
    try:
        os.remove("quest1.png")
        os.remove("quest2.png")
        os.remove("quest3.png")
        os.remove("quest4.png")
    except FileNotFoundError:
        pass
    logging.info("Exiting...")

if __name__ == "__main__":
    time.sleep(1)
    logging.info(" > niepogoda's reroll script < ")

    main_thread = threading.Thread(target=main_loop)
    main_thread.daemon = True
    main_thread.start()

    killswitch()
