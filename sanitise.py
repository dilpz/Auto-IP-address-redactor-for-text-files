import re
import getpass
import os
import sys


def sanitise():
    for name in filelist:

        with open(name, '+', encoding="utf-8", errors="ignore") as f:
            content = f.read()
            y = '\d+\.\d+\.\d+\.\d+'
            x = re.sub(y, "***.***.***.***", content, flags=re.DOTALL)
            f.write(x)

        print(f'''                       {name} successfully sanitized!       ''')
        print("\n")


if __name__ == "__main__":
    os.system('cls')
    path = input("Please enter destination file path containing your files for sanitization: ")

    filelist = []
    filenames = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))
            filenames.append(os.path.join(file))

    number = len(filelist)
    print("\n" * 5)
    print(f"                                              I found, {number} Files! and have listed them below: ")
    print("\n" * 3)

    for name in filenames:
        print(f"                                              {name}")
    print("\n" * 3)

    userinput = input("         Do you want to sanitise the above files? ENTER 'y' OR 'n' ")
    print("\n" * 3)

    if userinput == 'y':
        sanitise()
    else:
        print("\n" * 3)
        print("                           thanks for using the sanitization tool. Press Ctrl+Z to close out.")
