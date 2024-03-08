# speed-tester

Welcome to the Desktop Internet Speed Tester,
which has all the basic features of a 
Internet speed tester.

This features ping speed, download speed and upload speed.

The ping speed is displayed in milliseconds, the download speed in Mbps and upload speed also in Mbps.

## Installation

To Start with the Installation, follow these Steps:

- Download the installer or use the portable (`.zip`) file.
- For the **Zip file**: Extract the zip to any location you want and run the `.exe` file (`speedtest.exe`)
- For the **Setup Installer**: Open the setup, follow the steps and install the app.

## Building from Source
You can build from source and use it. But to do that you have to install some tools.

To do that follow the steps.

### Part 1: Setup
- If you have Git installed, clone this repository by typing `git clone https://github.com/agnivomallick/speed-tester.git `
- Or you can download the source from the Releases page and extract it.
- Now then you need to have Python 3.11+ installed. I recommend Python 3.12 as I coded it in that version only.
- Then when installing Python make sure you have `pip` installed.
- Now you have to install some packages for this to work. Type the commands:
```
- pip install PySide6
- pip install speedtest-cli
- pip install cx-Freeze
```
The first installs PySide6, second the speedtest-cli for speed test, and third cx_Freeze for the build.

### Part 2: Building

- Now open the extracted folder in code editor. Or you can create a file in the folder, called `setup.py`
- Type the following code: 
- ```Python
  from cx_Freeze import setup, Executable
  import sys

  base = "Win32GUI" if sys.platform == "win32" else None 

  build_options = {
    "packages": ["PySide6", "speedtest", "math"],
    "include_files": ["speedtest_ui.py", "speedtest_icon.ico", "speedtest_icon.png"],
    "include_msvcr": True
  }

  executable_main = Executable(
    "speedtester.py",
    base="base",
    icon="speedtest_icon.ico",
    target_name="speedtest"
  )

  setup(
  name="SpeedTester",
  version="1.0.0",
  author="<your name/company>",
  description="SpeedTester",
  options={"build_exe": build_options},
  executables=[executable_main]
  )

Replace `<your name/company>` with your name or company.

- Then in the command line run in the folder only: `py setup.py build`
- If you want a build only and will use another software to package it into an installer, use the above command.
- Or if you want to use cx_Freeze's default packaging system, then type `py setup.py bdist_msi`
- This command will work on Windows only. For Mac, type `py setup.py bdist_dmg` or `py setup.py bdist_mac`
- The result `.msi` or `.app` can be found in the `dist/` directory.
- For the build only, it can be found in the `build/` directory.
- Now you can package your installer and distribute it. But adhere to the [MIT License](/LICENSE).
- This can also be packaged using PyInstaller. See their guide for packaging it.