import re
import getpass
import os
import sys


def sanitise(filelist):
    for name in filelist:
        with open(name, 'r', encoding="utf-8", errors="ignore") as f:
            content = f.read()
            y = '\d+\.\d+\.\d+\.\d+'
            x = re.sub(y, "***.***.***.***", content, flags=re.DOTALL)
            #f.close() #While using `with` statement, it doesn't need to close a file object explicitly
            with open(name, 'w', encoding="utf-8", errors="ignore") as f:
                f.write(x)
            #f.close() #While using `with` statement, it doesn't need to close a file object explicitly
            print(
                f'''                       {name} successfully sanitized!       '''
            )
            print("\n")


if __name__ == '__main__':
    os.system('cls')
    path = input(
        "Please enter destination file path containing your files for sanitization: "
    )

    filelist = []
    filenames = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))
            filenames.append(file)  #filenames.append(os.path.join(file))
    '''
    # or 
    for root, dirs, filenames in os.walk(path):
        for file in filenames:
            filelist.append(os.path.join(root, file))
    '''

    number = len(filelist)
    print("\n" * 5)
    print(
        f"                                              I found, {number} Files! and have listed them below: "
    )
    print("\n" * 3)

    for name in filenames:
        print(f"                                              {name}")
    print("\n" * 3)

    userinput = input(
        "         Do you want to sanitise the above files? ENTER 'y' OR 'n' ")
    print("\n" * 3)

    if userinput == 'y':
        sanitise(filelist)  # pass `filelist` as an argument
    elif userinput == 'n':  # It doesn't matter to use `if`, but I would use `elif` to express both conditions are together in the context.
        print("\n" * 3)
        print(
            "                           thanks for using the sanitization tool. Press Ctrl+Z to close out."
        )
    else:
        print("Wrong input. Please try again.")
