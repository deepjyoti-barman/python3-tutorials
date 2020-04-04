## Important commands in terminal (Mac or Linux)

>Command: <span style='color: lightseagreen'>pwd</span>

- **'pwd'** stands for **P**rint **W**orking **D**irectory.
- This command will tell you the full absolute path of where you are at in the command line.

---

>Command: <span style='color: brown'>cd</span>

- **'cd'** stands for **C**hange **D**irectory.
- This command will help you navigating through file and folders.
- Examples:
  - ```cd /home/defiant-dj04/Documents (Changing directory by absolute path)```
  - ```cd Documents (Changing directory By relative path)```
  - ```cd .. (Going up one level)```
  - ```cd ../.. (Going up couple of level)```
  - ```cd - (Going back to the previous directory)```
  - ```cd / (Changing to root directory)```
  - ```cd ~ (Changing to home directory)```

---

>Command: <span style='color: mediumblue'>ls</span>

- **'ls'** stands for **L**ist.
- This command is used to list the contends of the directory.
- You can supply options such as '-a', '-l' to format the listing of directories.
- Examples:
  - ```ls -a (List all files and directories (including hidden ones))```
  - ```ls -l (List all files and directories (excluding hidden ones) in longer format)```
  - ```ls -al (List all files and directories (including hidden ones) in longer format)```

---

>Command: <span style='color: seagreen'>mkdir</span>

- **'mkdir'** stands for **M**ake **D**irectory.
- This command is used to create a new child directory inside the current directory.
- Examples:
  - ```mkdir Photos (To create a new directory)```
  - ```mkdir Songs Movies (To create multiple directories)```
  - ```mkdir "Songs/Classical" (To create nested directories, one directory inside another directory)```

---

>Command: <span style='color: orange'>touch</span>

- This command **'touch'** followed by the file name and file-type extension is used to create a new file of that type inside the current directory.
- If you use touch command in a file that already exists it will modify the last updated date and time of that tile.
- Examples:
  - ```touch Notes.txt (To create a new file)```

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
  - ```mv notes.txt official_notes.txt (To rename a file)```
  - ```mv notes.txt ../ (To move the file one level up to the parent directory)```
  - ```mv notes.txt ../official_notes.txt (To rename and move the file one level up to the parent directory)```

---

>Command: <span style='color: red'>rm</span>

- **'rm'** stands for **R**e**m**ove.
- This command is used to delete files and directories.
- Along with this command we need to pass -r (recursive), -v (verbose), -f (force) options to prevent warnings and to remove directories containing sub-directories or files.
- Examples:
  - ```rm demo.cpp (To delete a single file)```
  - ```rm demo.cpp temp.txt (To delete multiple files)```
  - ```rm Photos (To remove an empty directory)```
  - ```rm -rvf Photos (To remove a directory and its contents)```