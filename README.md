# niepogoda's reroll script

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/0e8/niepogodasreroll)

This script automates the process of rerolling quests in Lee:// RPG. It utilizes OCR to read from screen.
## Installation

#### Before using this script, ensure you have installed Python (tested on 3.12.4)

1. **Install Dependencies:**
   - Open a command prompt or terminal.
   - Navigate to the directory containing `reroll.py` and `requirements.txt`.
   - Run the following command to install required packages:
     ```
     pip install -r requirements.txt
     ```
   - Install Tesseract
      - Download and install [Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html)
      - Add Tesseract to path
         - Open Start Menu and search for "Environment Variables".
         - Click on "Edit the system environment variables".
         - In the System Properties window, click on the "Environment Variables" button.
         - In the Environment Variables window, find the "Path" variable under System variables and select it. Click "Edit."
         - Click "New" and add the path to the Tesseract executable directory (e.g., C:\Program Files\Tesseract-OCR).
         - Click "OK" to close all dialog boxes.
       - Verify installation by running `tesseract -v` in commmand prompt

2. **Configure Screen Regions:**
   - Run `py regions.py`. This script allows you to select specific regions on your screen where quests and reroll buttons are located.
   - Follow the on-screen instructions to select regions for Quests and their respective reroll buttons.
   - Save the regions when prompted. This will generate a `regions.json` file that `reroll.py` will use.

   **How to select those areas?** <br>
   <img src="./img/questarea.png"> <br>
   <img src="./img/buttonarea.png"> <br>

   **Make sure to leave some margins around the text and to not get the *Kill Quest* label in the quest area!**

3. **Configure `config.json`:**
   - Ensure `config.json` is present in the script's directory with the following parameters:
     - `minimum_chests`: Minimum number of chests required in each quest.
     - `chest_type` : Type of chest to roll for.
     - `delay`: Delay (in seconds) between each reroll.
     - `start_keybind`: Keyboard key to start the reroll process.
     - `kill_keybind`: Keyboard key to stop the script.

     For the template, check *config.json.example*

4. **Run the Script:**
   - Run `py reroll.py` to execute the script.
   - Once started, press `start_keybind` (configured in `config.json`) to begin the reroll process.
   - Press `kill_keybind` (configured in `config.json`) to stop the script at any time.
## Troubleshooting

- If the script does not behave as expected, ensure all dependencies are correctly installed and configured.
- Check `latest.log` for error messages or warnings that may indicate issues with screen resolution or configuration files.

For further assistance, [open an issue](https://github.com/0e8/niepogodasreroll/issues) or refer to the documentation of the libraries used in this script.

## Notes
Much love to all of the people that helped me with this script.  
Thanks to **lmmortalz** that contributed ALOT to this project.

Want a new feature? [open an issue](https://github.com/0e8/niepogodasreroll/issues)!

---

# TODO
   - script pause
   - gui/tui
   - .exe file, so people that doesnt know how to use computer and chatgpt can run this thing

Remember that contributes are welcome :)
