import re
import getpass
import os
import sys

os.system('cls')
path = input("Please enter destination file path containing your files for sanitization: ")

filelist = []
filenames = []

for root, dirs, files in os.walk(path):
    for file in files:
        filelist.append(os.path.join(root, file))
        filenames.append(os.path.join(file))

number = len(filelist)
print("\n"*5)
print(f"                                              I found, {number} Files! and have listed them below: ")
print("\n"*3)

for name in filenames:
    print(f"                                              {name}")
print("\n" * 3)

def sanitise():
    for name in filelist:
        with open(name, 'r', encoding="utf-8", errors="ignore") as f:
            content = f.read()
            y = '\d+\.\d+\.\d+\.\d+'
            x = re.sub(y, "***.***.***.***", content, flags=re.DOTALL)
            f.close()
            with open(name, 'w', encoding="utf-8", errors="ignore") as f:
                f.write(x)
            f.close()
            print(f'''                       {name} successfully sanitized!       ''')
            print("\n")

userinput = input("         Do you want to sanitise the above files? ENTER 'y' OR 'n' ")
print("\n" * 3)

if userinput == 'y':
    sanitise()
if userinput == 'n':
    print("\n"*3)
    print("                           thanks for using the sanitization tool. Press Ctrl+Z to close out.")
