import os
import win32com.client

def read_shortcut(path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(path)
    print(f"Target: {shortcut.TargetPath}")
    print(f"WorkingDirectory: {shortcut.WorkingDirectory}")

if __name__ == "__main__":
    path = r"c:\Users\ABC\OneDrive\Desktop\Projects\CrizTools\launch_criztools.lnk"
    if os.path.exists(path):
        try:
            read_shortcut(path)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Shortcut not found")
