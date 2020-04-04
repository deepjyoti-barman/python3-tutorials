## Command-line syntax in Windows vs in Mac/Linux

- Mac and Linux operating systems are both based on UNIX and they share many of the same terminal commands.
- Windows has entirely different Kernel (base) and has traditionally has its own command-line syntax for MS-DOS and command prompt.

## What is Powershell?

- Powershell is a superior shell to command prompt for windows users.
- Powershell has adopted aliases that mimic the most common UNIX commands, hence it allows Windows users to type UNIX like commands on their system.
- Powershell ships with all modern Windows systems (since Windows 7).
- Using Powershell we can change directories, manipulate files and directories, and so forth.

## Important commands in Powershell (Windows)

>Command: <span style='color: purple'>Get-Service | where-Object {$_.Status -eq "Running"}</span>

- This command prints out all the processes that are currently running on our system.

---

>Command: <span style='color: lightseagreen'>pwd</span>

- **'pwd'** stands for **P**rint **W**orking **D**irectory.
- This command will tell you the full absolute path of where you are at in the command line.

---

>Command: <span style='color: brown'>cd</span>

- **'cd'** stands for **C**hange **D**irectory.
- This command will help you navigating through file and folders.
- Examples:
  - ```cd C:\Users\defiant-dj04\Desktop (Changing directory by absolute path)```
  - ```cd Documents (Changing directory By relative path)```
  - ```cd /d E:\Pictures (First switches to drive E: then moves into Pictures directory)```
  - ```cd .. (Going up one level)```
  - ```cd ..\.. (Going up couple of level)```
  - ```cd \ (Changing to root directory)```
  - ```cd ~ (Changing to home directory)```
  - ```cd ~\Desktop (Shortcut to switch to Desktop directory by referencing home directory with ~)```

---

>Command: <span style='color: mediumblue'>ls</span>

- **'ls'** stands for **L**ist.
- This command is used to list the contends of the directory.
- You can supply options such as '-a', '-l' to format the listing of directories.
- Examples:
  - ```ls (List all files and directories (excluding hidden ones))```
  - ```ls -Hidden -System (List all hidden and system files)```
  - ```ls -Exclude *.bat (List all files and directories excluding .bat files)```
  - ```ls -Filter *.bat (List only .bat files)```

---

>Command: <span style='color: seagreen'>mkdir</span>

- **'mkdir'** stands for **M**ake **D**irectory.
- This command is used to create a new child directory inside the current directory.
- Examples:
  - ```mkdir Photos (To create a new directory)```
  - ```mkdir -Path Songs, Movies (To create multiple directories)```
  - ```mkdir "Songs\Classical" (To create nested directories, one directory inside another directory)```

---

>Command: <span style='color: orange'>New-Item -ItemType file <file_name.extension></span>

- This command followed by the file name and file-type extension is used to create a new file of that type inside the current directory.
- Examples:
  - ```New-Item -ItemType File hello-world.py```

---

>Command: <span style='color: #1F618D'>touch</span>

- This command **'touch'** followed by the file name and file-type extension is used to create a new file of that type inside the current directory.
- If you use touch command in a file that already exists it will modify the last updated date and time of that tile.
- Examples:
  - ```touch Notes.txt (To create a new file encoded with UTF-8)```

---

>Command: <span style='color: deeppink'>mv</span>

- **'mv'** stands for **M**ove.
- This command is used to move or rename files and directories.
- It takes two arguments: the source and the destination.
- We can get 3 cases, while using this command on a file or folder:
  - If the destination is in a different directory, the file / directory will be moved to that directory.
  - If the destination is a new name in the same directory, it will rename the file / directory.
  - If it is both, the destination is a different name and it is in a different directory it will rename the targeted file / directory and will move it over there.
- Examples:
  - ```mv notes.txt class_notes.txt (To rename a file)```
  - ```mv class_notes.txt Temp (To move the into 'Temp' directory)```
  - ```mv class_notes.txt ..\official_notes.txt (To rename and move the file one level up to the parent directory)```

---

>Command: <span style='color: red'>rm</span>

- **'rm'** stands for **R**e**m**ove.
- This command is used to delete files and directories.
- Along with this command we need to pass -r (recursive), -v (verbose), -fo (force) options to prevent warnings and to remove directories containing sub-directories or files.
- Examples:
  - ```rm demo.cpp (To delete a single file)```
  - ```rm -Path temp1.txt, temp2.txt (To delete multiple files)```
  - ```rm Photos (To remove an empty directory)```
  - ```rm -r -v -fo Photos (To remove a directory and its contents)```