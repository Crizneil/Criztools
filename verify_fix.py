import sys
import os

# Add the project dir to path to import main
project_dir = r"c:\Users\ABC\OneDrive\Desktop\Projects\CrizTools"
sys.path.append(project_dir)
os.chdir(project_dir)

from main import PersonalTools

print("[*] Testing GitHub Streak functionality...")
try:
    PersonalTools.github_streak()
    print("[+] Test completed.")
except Exception as e:
    print(f"[-] Test failed: {e}")
