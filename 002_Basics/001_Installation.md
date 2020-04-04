## Installation Steps for Python3

- Depending on the platform or operating system you are using go the links given below
  - [Windows](https://www.python.org/downloads/windows/ "Python3 Download for Windows")
  - [Linux](https://www.python.org/downloads/source/ "Python3 Download for Linux")
  - [Mac](https://www.python.org/downloads/mac-osx/ "Python3 Download for Mac")
- Now for Windows users depending on the architecture or bit-size of the system click on the following link:
  - 32-bit Operating System: (click on) Windows x86 executable installer
  - 64-bit Operating System: (click on) Windows x86-64 executable installer
- Double click or open the installer, follow the installation steps and complete the installation (NOTE: Windows users must tick on 'Add Python 3.x to PATH' option while installing)
- To confirm that Python3 is successfully installed on your system open up terminal / Powershell / Command Prompt and type any of the following command:

  ```bash
  python --version
  ```
  ```bash
  python -V
  ```
- If the output is as following that means Python is successfully installed on your system:
<br><span style='color: blue'>PS C:\Users\Deepjyoti.Barman\Desktop></span><span style='color: lightseagreen'>python --version</span>
<br><span style='color: red'>Python 3.8.2</span>

- Alternatively you can also enter the following command in terminal / Powershell / Command Prompt:
    ```bash
  python
  ```
   This will open up the Python Interactive Shell also known as REPL (Read, Evaluate, Print and Loop). Essentially it is a place to type code in Python and it is mainly used to debugging purposes. (NOTE: to get out of the REPL you can either press ```Ctrl + D``` (on Mac) / ```Ctrl + Z``` (on Windows) or type in ```exit()``` or even ```quit()``` and press the ```Enter``` key on keyboard).
- NOTE: Whenever you type in something or perform any operation into Python Interactive Shell or REPL, it will automatically print out the result. But, in usual Python scripts you need to use print() function in order to print out the result or anything of your choice.
  