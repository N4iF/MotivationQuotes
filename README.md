## Description:

The messages_notifier.py script is a Python program that fetches motivational quotes from an API and displays them as desktop notifications at regular intervals. The script uses the winotify library to show notifications without disrupting your workflow. It's a simple way to receive inspiration throughout the day without any manual intervention.

## How to Use:

1. Clone or download this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the script using the command python messages_notifier.py.

## Important step

* change the path file for image in the python code at 17 line.
  
## Features:

Fetches motivational quotes from a public API.
Displays notifications with custom titles and messages.
Runs in the background and shows notifications at specified intervals.
Supports Windows operating system.

> Note:
This script is intended for educational and personal use only. Make sure to adjust the notification interval and customize the script as needed.

## Method to make it run like auto start app

Create a Batch Script:

Open a text editor (like Notepad) on your Windows computer.

Copy and paste the following code into the text editor:

```batch
@echo off
start pythonw.exe "C:\Scripts\messages_notifier.py"
```
Replace "C:\Scripts\messages_notifier.py" with the actual path to your Python script.

Save the file with a .bat extension, such as RunScript.bat.

Include the Batch Script in Startup:

Press Win + R to open the Run dialog box.

Type shell:startup and press Enter. This opens the Startup folder for your user account.

Move the .bat file you created (e.g., RunScript.bat) to this Startup folder.

## Picture for the script
![Alt text](https://imageupload.io/ib/q0Qikf8siBaKLlJ_1699552709.jpeg)
