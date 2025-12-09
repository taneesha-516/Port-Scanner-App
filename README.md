
# Python GUI Port Scanner

This is a basic Python project where I created a simple GUI-based port scanner. The program takes an IP address as input and checks which TCP ports are open. I made this project mainly to understand socket programming, Tkinter GUI, and how multithreading works in Python.



## About the Project

As part of learning networking concepts during my second year of B.Tech, I wanted to try building a small tool related to cybersecurity. Instead of making a command-line scanner, I created a GUI so the user can directly enter an IP address and start scanning without using any terminal commands. The scanning process runs in a separate thread so the application window does not freeze.



## Features

* Simple Tkinter-based interface
* Scans common TCP ports (1 to 1000)
* Shows open ports in real time
* Multithreading used to keep the GUI responsive
* Can be converted into a Windows executable file



## Technologies Used

* Python 3
* Tkinter (for GUI)
* Socket module (for network connections)
* Threading module
* PyInstaller (for creating the exe file)



## How to Run

1. Install Python from the official website if not already installed.

2. Download or copy the project folder.

3. Open Command Prompt and move to the folder:

   ```
   cd folder-name
   ```

4. Run the program using:

   ```
   python scanner.py
   ```

The GUI window will open automatically.


## How the Program Works

1. When the user enters an IP address and starts the scan, the program creates a TCP socket.
2. It checks each port by using the `connect_ex()` function.
3. If the return value is 0, the port is considered open.
4. A background thread handles the scanning, so the GUI is not blocked.
5. Since threads should not update the GUI directly, the program uses `root.after()` to safely update the output area.



## Creating the Executable File

If you want to generate a Windows executable:

1. Install PyInstaller:

   ```
   pip install pyinstaller
   ```

2. Run the following command inside the project folder:

   ```
   pyinstaller --onefile --noconsole scanner.py
   ```

3. After the build finishes, the exe file will be available inside the `dist` folder.



## Disclaimer

This project is only for learning and academic purposes.
Port scanning networks that you do not own or do not have permission to test is illegal.
Use this tool only on your own systems or with proper authorization.

