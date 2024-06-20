<<<<<<< HEAD
# ALL CREDIT GOES TO - niepogoda


# Step 1: Download Tesseract OCR

**Visit the Official Tesseract GitHub Repository: Open your browser and go to the Tesseract GitHub releases page. (https://github.com/tesseract-ocr/tesseract/releases)

Choose the Correct Installer: Scroll down to the "Assets" section of the latest stable release and download the appropriate installer for your operating system:

For Windows, download the .exe file.
For macOS, Tesseract can be installed via Homebrew.
For Linux, Tesseract can be installed using the package manager.**

# Step 2: Install Tesseract OCR

**Windows

Run the Installer: Locate the downloaded .exe file and double-click it to run the installer.
Follow the Installation Wizard: Proceed through the installation steps, selecting the default options unless you have specific needs.
Add Tesseract to System Path: Ensure that you check the option to add Tesseract to your system's PATH during installation. If you missed this, you can add it manually:
Right-click on 'This PC' or 'My Computer' and select 'Properties'.
Go to 'Advanced system settings' and click 'Environment Variables'.
Find the 'Path' variable under System variables, select it, and click 'Edit'.
Add the path to the Tesseract executable (e.g., C:\Program Files\Tesseract-OCR) and click 'OK'.
macOS

Install Homebrew: If you don't have Homebrew installed, open Terminal and run the following command:

```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

Install Tesseract: Once Homebrew is installed, run the following command in Terminal:

```brew install tesseract```

Linux

Update Package Lists: Open Terminal and update your package lists:

```sudo apt update```

Install Tesseract: Run the following command:

```sudo apt install tesseract-ocr```

# Step 3: Verify Installation

Open Command Prompt or Terminal: Open the Command Prompt on Windows or Terminal on macOS/Linux.
Check Tesseract Version: Type the following command and press Enter:

```tesseract --version```

You should see the version information of Tesseract OCR, indicating that it has been installed correctly.**

=======
# niepogoda's reroll script

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues) 
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/0e8/niepogodasreroll)
>>>>>>> niepogodasrerollTesseract/main

This script automates the process of rerolling quests in ***Lee:// RPG***. It utilizes OCR to read from screen.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python (version 3.10.6 or higher recommended)
- Required Python packages (install via `pip install -r requirements.txt`)
- Windows operating system

## Setup Instructions

1. **Install Python:**
   - If Python is not installed, download it from [python.org](https://www.python.org/downloads/) and follow the installation instructions.

2. **Install Dependencies:**
   - Open a command prompt or terminal.
   - Navigate to the directory containing `reroll.py` and `requirements.txt`.
   - Run the following command to install required packages:
     ```
     pip install -r requirements.txt
     ```

3. **Configure Screen Regions:**
<<<<<<< HEAD
   - Run `regions.py` by double-clicking on it. This script allows you to select specific regions on your screen where quests and reroll buttons are located.
   - Follow the on-screen instructions to select regions for Quests 1, 2, 3, and their respective reroll buttons.
   - Save the regions when prompted. This will generate a `regions.json` file that `reroll.py` will use.

**How to select those areas?** <br>
<img src="https://github.com/JoeSmoePoe/REVISED/blob/main/REVISEDniepogodasreroll-3.0/img/questarea.png"> <br>
<img src="https://github.com/JoeSmoePoe/REVISED/blob/main/REVISEDniepogodasreroll-3.0/img/buttonarea.png"> <br>
=======
   - Run `py regions.py`. This script allows you to select specific regions on your screen where quests and reroll buttons are located.
   - Follow the on-screen instructions to select regions for Quests 1, 2, 3, and their respective reroll buttons.
   - Save the regions when prompted. This will generate a `regions.json` file that `reroll.py` will use.

   **How to select those areas?** <br>
   <img src="./img/questarea.png"> <br>
   <img src="./img/buttonarea.png"> <br>
>>>>>>> niepogodasrerollTesseract/main

   **Make sure to leave some margins around the text and to not get the *Kill Quest* label in the area!**

4. **Configure `config.json`:**
   - Ensure `config.json` is present in the script's directory with the following parameters:
     - `minimum_chests`: Minimum number of chests required in each quest.
     - `delay`: Delay (in seconds) between each reroll.
     - `start_keybind`: Keyboard key to start the reroll process.
     - `kill_keybind`: Keyboard key to stop the script.

5. **Run the Script:**
<<<<<<< HEAD
   - Double-click on `reroll.py` to execute the script.
=======
   - Ryb `py reroll.py` to execute the script.
>>>>>>> niepogodasrerollTesseract/main
   - Once started, press `start_keybind` (configured in `config.json`) to begin the reroll process.
   - Press `kill_keybind` to stop the script at any time.

## Notes

- **Logging:** Detailed logs are written to `latest.log` in the script's directory. Check this file for information on script operations and any errors encountered.
<<<<<<< HEAD
=======
- **Pull requests:** If you want to make a pull request, please do it at `tests` branch!
>>>>>>> niepogodasrerollTesseract/main

## Troubleshooting

- If the script does not behave as expected, ensure all dependencies are correctly installed and configured.
- Check `latest.log` for error messages or warnings that may indicate issues with screen resolution or configuration files.

For further assistance, contact me on Discord or refer to the documentation of the libraries used in this script.
