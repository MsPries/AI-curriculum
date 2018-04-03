### Pip pip, hooray!
Pip is a package manager for Python. Installing it allows us to standardize the process for getting new Python libraries. **Note:** If you are using Anaconda and wish to continue using it, you will likely be able to use it to get all the libraries we need for this class. If you choose not to use pip, you are responsible for figuring out any installation strangeness.

**If you have more than one version of Python installed, make sure you're using pip for Python 3.** You may need to use the command pip3 if you have pip installed to manage Python 2.x

First, check to see if you have pip installed. Run the command "pip" in your Terminal/Command Prompt. If you get a list of options, pip is already installed (awesome!). If not - proceed with installation.

#### Installing pip:

1. Download get-pip.py from [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/). Note the .py extension: this is a Python file, so you should navigate to the directory where it is saved and run the file from your command line with **python get-pip.py**

2. Note where pip is installed - it will likely be in ~/[somethings]\Python35\Scripts\pip.exe

3. Add this path to your PATH (as you did with Python).

4. Test in a *new* Terminal/Command Prompt window - if you run **pip** and get pip options, great. If not, turn to Google, the Class Chat, or Ms. Pries.

#### Installing packages with pip:

Pip gives you several commands, the most important of which is install.  The first package we want is called numpy, so in the command line, run **pip install numpy**

This will collect the numpy package from the internet and install it for you. If you get a success message and run pip list you should now see that numpy is installed. You can test this in your REPL: open the Python REPL with the command python , then import numpy . If the import statement completes without error, you have successfully used pip to install the numpy package. 

