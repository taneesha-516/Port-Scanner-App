import PyInstaller.__main__
import os

#file to convert to app
filename = "Port_Scanner.py"

#check if file exists
if not os.path.exists(filename):
    print(f"Error: {filename} not found.")
else:
    print("Starting build process... please wait.")
    
    # Run PyInstaller
    PyInstaller.__main__.run([
        filename,                   # The script to convert
        '--onefile',                # Create a single executable file
        '--noconsole',              # Hide the black command window
        '--name=PortScannerApp',    # Name of the final app
        '--clean',                  # Clean cache before building
        
    ])

    print("\nBuild complete!")
    print("Look for your app in the 'dist' folder.")