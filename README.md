Project-Cylon
=============
Generic Web Acceptance Testing Framework.

About
-----
Project-Cylon framework provide easier way to create web acceptance testing.
Without coding skill, user can write test scenario by focusing on systems behaviour.

This project powered by most popular tools [Selenium](http://docs.seleniumhq.org/) and [Behave](http://pythonhosted.org/behave/).

![alt text](http://docs.seleniumhq.org/images/big-logo.png)
![alt text](https://raw.githubusercontent.com/behave/behave/master/docs/_static/behave_logo.png)


Changelog
---------
See: [Changelog](https://github.com/gigapixel/project-cylon/blob/master/CHANGELOG.md)

Prerequisite
------------
1. Ensure your test machine has [Firefox](http://www.mozilla.org/en-US/firefox/new/) installed.

How to install
--------------
Please see installation guide for your systems.

* [Windows](https://github.com/gigapixel/project-cylon/wiki/Installation-on-Windows)
* [Mac OSX](https://github.com/gigapixel/project-cylon/wiki/Installation-on-Mac-OSX)
* [Linux](https://github.com/gigapixel/project-cylon/wiki/Installation-on-Linux)

Create test project
-------------------
1. Download test project template from: [project-cylon-demo.zip](https://github.com/gigapixel/project-cylon-demo/archive/master.zip)
    * For Windows, you need to place project folder on drive C: (has known issue to import steps from different root)
2. Extract the zip file to any location (you can rename this folder as your test project name)
3. Add / Edit ```.yaml``` files in ```pageobjects``` folder
    * see how to write page object in [wiki](https://github.com/gigapixel/project-cylon/wiki/Page-Object)
4. Add / Edit ```.feature``` file in ```features``` folder
    * see example from: [feature files](http://pythonhosted.org/behave/tutorial.html#feature-files)
    * see all bundle keywords in [wiki](https://github.com/gigapixel/project-cylon/wiki/Bundle-Keywords)
5. Edit ```steps.py``` file in ```features/steps``` folder (optional)

Run test features
-----------------
You can run all tests via following batch / shell script.

* For Windows use ```RunAllFeatures.bat```
* For Mac / Linux use ```RunAllFeatures.sh```

You can run test with following ```behave``` command at your project directory.

* To run all feature files use:

    ```
    behave --quiet
    ```
* To run with specified tags use:

    ```
    behave --quiet  --tags=@your_tag
    ```
* For another command options see: [Using Behave](http://pythonhosted.org/behave/behave.html)

Package Dependencies
--------------------
* [pyyaml](https://pypi.python.org/pypi/PyYAML)
* [behave](https://pypi.python.org/pypi/behave)
* [selenium](https://pypi.python.org/pypi/selenium)

Python Package Index
--------------------
See: https://pypi.python.org/pypi/project-cylon

Support Editor Plugin
---------------------
For Atom editor user, please see [project-cylon-snippets](https://atom.io/packages/project-cylon-snippets)
