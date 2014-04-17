Project Cylon
=============
Web Automated Testing Framework using Behave and Selenium

About
-----
Project Cylon framework provide easy way to create web automation test without coding skill, just focus on the test scenario.

Prerequisite
------------
1. Ensure your test machine has Firefox installed.

How to install on Windows (manually)
------------------------------------
1. Install vc redist (Microsoft Visual C++ 2010 Redistributable Package).
2. Install Python (use version 2.7). 
    * Download from: [python downloads](https://www.python.org/downloads/)
3. Add following to PATH environment variable.
    ```C:\Python27;C:\Python27\Scripts;C:\Python27\Lib\site-packages;```
4. Install Python for Windows extension.
    * Download from: [pywin32](http://sourceforge.net/projects/pywin32/files/pywin32/)
    * Select latest build and correct Python version
5. Install python setuptools. 
    * Download from: [setuptools](https://pypi.python.org/pypi/setuptools/0.9.6#installation-instructions)
6. Run following command to install required packages.

    ```
    easy_install pip
    pip install pyyaml
    pip install behave
    pip install selenium
    pip install colorama
    ```
7. Install ansicon.
    * Download from: [ansicon](https://github.com/adoxa/ansicon/downloads)
	* Read installaion instructions from: [ANSI escape sequence support with ansicon](http://www.kevwebdev.com/blog/in-search-of-a-better-windows-console-using-ansicon-console2-and-git-bash.html#ansicon)

8. Install project-cylon package.

    ```
    pip install project-cylon
    ```

How to install on Windows (via package manager)
-----------------------------------------------
1. We have suggest to use [chocolatey](https://chocolatey.org/) as your package manager, install by following command.

    ```
    @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%systemdrive%\chocolatey\bin
    ```
2. install python 2.7 and pip.

    ```
    cinst python -Version 2.7.6
    cinst pip
    ```
3. install required packages.

    ```
    pip install pyyaml
    pip install behave
    pip install selenium
    pip install colorrama
    ```
4. install ansicon.

    ```
    cinst ansicon
    ```
5. install project-cylon package.

    ```
    pip install project-cylon
    ```

Setup Thai font for Windows console
-----------------------------------
1. Install Thai Font for Windows console
    * Download [ThaiLang4CMD.zip](https://bitbucket.org/gigapixel/projectcylon/downloads/ThaiLang4CMD.zip)
    * Install font ```Courmon.ttf``` to windows fonts folder
    * Run ```ThaiLangInDOS.reg```
    * Restart machine
    * Run cmd windows and set font to ```Courier Mono Thai``` and set font size to 24

2. Make Python able to run Thai
    * Edit ```C:\Python27\Lib\site.py```
    * Find the following 2 lines and comment them out:
        ```
        if hasattr(sys, "setdefaultencoding"):
            del sys.setdefaultencoding
        ```

	* Create ```sitecustomize.py``` file at ```C:\Python27\Lib\site-packages``` with the following content
        ```
        import sys
	    reload(sys)
	    sys.setdefaultencoding("utf-8")
        ```

3. Change Language for non-Unicode program to Thai (Region and Language -> Administrative -> Language for non-Unicode program)
4. Restart machine

How to install on Mac
---------------------
1. We have suggest to use [homebrew](http://brew.sh/) as your package manager, install by following command.

    ```
    ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
    ```
2. After installation completed use following command to check your system and update homebrew.

    ```
    brew doctor
    brew update
    ```
3. Install python on your machine.

    ```
    brew install python
    ```
4. After python installation completed you should have pip, use it to install required packages.

    ```
    pip install pyyaml
    pip install behave
    pip install selenium
    ```
5. Install project-cylon package.

    ```
    pip install project-cylon
    ```

How to install on Linux
-----------------------
Almost Linux already bundle with Python, so you can install required packages by following command.
```
sudo easy_install pip
sudo pip install pyyaml
sudo pip install behave
sudo pip install selenium
```

Then install project-cylon package.
```
sudo pip install project-cylon
```

Create test project
-------------------
1. Download test project template from: [example-test-v0.1.0.zip](https://bitbucket.org/gigapixel/projectcylon/downloads/example-test-v0.1.0.zip)
2. Extract the zip file to any location (you can rename this folder as your test project name)
3. Add / Edit ```.yaml``` files in ```pageobjects``` folder
4. Add / Edit ```.feature``` file in ```features``` folder see example from: [feature files](http://pythonhosted.org/behave/tutorial.html#feature-files)
5. Edit ```steps.py``` file in ```features/steps``` folder (optional)

Run test features
-----------------
You can run all tests via following batch / shell script.

* For Windows use ```RunAllFeatures.bat```
* For Mac / Linux use ```RunAllFeatures.sh```

You can run test with following ```behave``` command at your project directory.

* To run all feature files use:
    ```behave --color --no-source --no-skipped --logging-level INFO```

* To run with specified tags use:
    ```behave --color --no-source --no-skipped --logging-level INFO --tags=@your_tag```

Package Dependencies
--------------------
* [pyyaml](https://pypi.python.org/pypi/PyYAML)
* [behave](https://pypi.python.org/pypi/behave)
* [selenium](https://pypi.python.org/pypi/selenium)

