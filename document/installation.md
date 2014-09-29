---
layout: page
title: Installation
---

Please follow installation guide below to setup project-cylon on your system.


## For Windows

### Setup project-cylon and dependencies

1. Download Windows installation package - project-cylon-windows-install_v0.1.3.zip
[here](https://github.com/kamolcu/project-cylon-installation/blob/master/project-cylon-windows-install_v0.1.3.zip?raw=true).
2. Extract to a directory on your Windows machine. For example: d:\downloads\project-cylon-windows-install_v0.1.3\
3. Run the file __cylon_install_v0.1.bat__. (If your Windows setting not set to show file type, you will not see __.bat__ so only __cylon_install_v0.1__ will be your target file)
4. Follow the on screen instructions (This will involve many clicks but do not have to type anything). Until the command prompt display:

    ```
    ===>Finished project-cylon installation ...
    ```

5. Press __Enter__ to close the command prompt window.

NOTE: If an error happens, report the error or create and issue report
[here](https://github.com/gigapixel/project-cylon/issues).


### Verify the installation

1. Open command prompt (Run --> cmd).
2. Type 'pip freeze' and check its output. The expected output should be printed as below (Please note that the version you saw might be newer than stated in this page):

```
PyYAML==3.11
behave==1.2.4
colorama==0.3.1
...

project-cylon==0.5.6
pywin32==219
selenium==2.42.1
...
```


### Setup Thai font for Windows console

1. Download [ThaiLang4CMD.zip](https://bitbucket.org/gigapixel/projectcylon/downloads/ThaiLang4CMD.zip)
2. Install font `Courmon.ttf` to windows fonts folder
3. Run `ThaiLangInDOS.reg`
4. Restart machine
5. Open cmd prompt and set font to `Courier Mono Thai`

NOTE: Please refer to
[manual installation](https://github.com/gigapixel/project-cylon/wiki/Manual-Installation-on-Windows-(for-reference))
in case you want to install step-by-step manually.


## For Mac OSX

1. Install [homebrew](http://brew.sh/) package manager by following command.

    ```
    $ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
    ```

2. After installation completed run following commands to check system and update homebrew.

    ```
    $ brew doctor
    $ brew update
    ```

3. Install python (and pip) on your machine.

    ```
    $ brew install python
    ```

4. Install other require packages.

    ```
    $ pip install pyyaml
    $ pip install behave
    $ pip install selenium
    ```

5. Install project-cylon package.

    ```
    $ pip install project-cylon
    ```


## For Linux (test on Ubuntu)

1. Almost linux are bundle with python and easy_install, firstly you need to install pip.

    ```
    $ sudo easy_install pip
    ```

2. Then install required packages by following command.

    ```
    $ sudo pip install pyyaml
    $ sudo pip install behave
    $ sudo pip install selenium
    ```

3. Finally install project-cylon package.

    ```
    $ sudo pip install project-cylon
    ```
