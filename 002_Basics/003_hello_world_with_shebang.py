# Platform             : GitHub
# Course Name          : python3-tutorials
# Company              : Go Digit General Insurance Limited
# Author               : Deepjyoti Barman
# Designation          : QA Analyst
# Date                 : April 04 (Saturday), 2020




""" Program with shebang to print "Hello World" and "Good Bye" world in console """

#!/usr/bin/env python

print("Hello World!  :)  ")
print("Goodbye World!  :(  ")


"""
    INITIAL NOTES:
    --------------
    - The first line in this file is the "shebang" line.
    - When you execute a file from the shell, the shell tries to run the file using the command specified on the shebang line.
    - The ! is called the "bang".  The # is not called the "she", so sometimes the "shebang" line is also called the "hashbang".
    - The hash character is used because it defines a comment in most scripting languages, so the shebang line will be ignored by the scripting language by default.
    - The shebang line was invented because scripts are not compiled, so they are not executable files, but people still want to RUN them. The shebang line specifies exactly how to run a script. In other words, this shebang line says that, when I type in ./basics.py, the shell will actually run:
        /usr/bin/env python basics.py
    if we use:
        #!/usr/bin/env python
    - In order to execute a python script without explicitly running python, you need to add execute permissions to the file.  To do add execute permission to basics.py, use:
        chmod +x basics.py

    SPECIAL NOTES:
    --------------
    - To directly execute .py files using:
        ./hello_world.py
    instead of executing .py files using python command:
        python hello_world.py
    we use "shebang" specially in Mac/Linux systems.
    - In "shebang" we write the path of python executable, version of python to be used to execute the specific file - as well as optional parameters
        e.g. #!/usr/bin/env python3 -u
        /usr/bin/env -> Path of the python executable
        python3      -> Version of Python to be used to execute the file
        -u           -> optional parameters
    - It plays a very important role to specify the Python version to be used to execute the script when multiple version of Python (Python2 and Python3) is installed on the same system.
    - "shebang" line is not required in Windows systems.
"""