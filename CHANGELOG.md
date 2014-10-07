# Changelog

## 1.1.11 - 2014-10-07
- Added to maximize browser when start run.

## 1.1.10 - 2014-09-24
- Added following keywords.

  ```feature
  Then the [...] class contains '...'
  Then the [...] value matches pattern '...' ## use regex pattern
  ```

## 1.1.9 - 2014-09-23
- Improve element wait and synchronize.

## 1.1.8 - 2014-09-09
- Removed specific selenium version in setup script.

## 1.1.7 - 2014-09-05
- Fixed to wait popup appear in following keywords.

  ```feature
  When user accept the popup
  When user cancel the popup
  Then the popup message shows '...'
  ```

- Fixed fail report on following keywords.

  ```feature
  When user clicks the [...]
  When user enters '...' to the [...]
  ```

## 1.1.6 - 2014-09-04
- Added following keywords.

  ```feature
  Then the [...] is enabled
  Then the [...] is disabled
  ```

## 1.1.5 - 2014-08-28
- Fixed to wait and check url after open page.

## 1.1.4 - 2014-08-27
- Fixed code to check when enters, clicks and selects fail.
- Fixed code to check selected text on select.

## 1.1.3 - 2014-08-26
- Fixed following keywords to wait for expected state (timeout 8 seconds).

  ```feature
  Then the [...] exists
  Then the [...] does not exist
  Then the [...] is visible
  Then the [...] is invisible
  ```

## 1.1.2 - 2014-08-08
- Fixed `IndexError: string index out of range` when run without `site=<site>` option.
- Fixed cylon command to has return code when test failed.

NOTE: Need to run `cylon update project` command.

## 1.1.1 - 2014-08-07
- Fixed `AttributeError: 'Configuration' object has no attribute 'site'`

NOTE: Need to run `cylon update project` command.

## 1.1.0 - 2014-08-05
- Added site config in config.yaml file, example.

  ```
  sites:
    default: http://www.yoursite.com
    develop: http://dev.yoursite.com
  ```

- Added route config in pageobject file, example.

  ```
  ...
  page:
    name: home
    route: /
  ...
  ```

- Fixed cylon command to run with configure site, example.

  ```
  cylon run site=develop
  ```

- Drop command `cylon run tags <tags>` use `cylon run tags=<tags>` instead.
- Drop support for `site_url:` config in pageobject file.
- Drop support for `settings.yaml` file.

NOTE: Existing projects need to run `cylon update project` command.

## 1.0.5 - 2014-08-04
- Fixed bug on "move mouse over ..." step.

## 1.0.4 - 2014-07-31
- Fixed NoneType error on check url keywords.

## 1.0.3 - 2014-07-31
- Fixed NameError Page on check url keywords.

## 1.0.2 - 2014-07-24
- Fixed running crash when check element visible.

## 1.0.1 - 2014-07-22
- Added to check yaml syntax before run.
- Fixed console logs more readable.
- Updated code style follow [PEP8](http://legacy.python.org/dev/peps/pep-0008/).

NOTE: Existing projects need to run `cylon update project` command.

## 1.0.0 - 2014-07-16
- Fixed wait time when find element.
- Updated core libraries.
- Updated code style follow PEP8
- Addded unit test to core libraries.
- Added CLI command to update project files.

  ```
  Commands:
  ...
  update project                  Update project files to compatible
                                  with current version.
  ```

NOTE: _Existing projects need to run update command above._


## 0.5.7 - 2014-07-07
- Added keywords to enters date, Example:

  ```feature
  When user enters date 'today' to the [date input]
  When user enters date 'tomorrow' to the [date input]
  When user enters date next '3' days to the [date input]

  When user enters date '2014-07-07 00:00:00' to the [date input] # specific date time
  ```

## 0.5.6 - 2014-06-30
- Fixed cylon CLI to working on Windows

## 0.5.5 - 2014-06-30
- Added cylon CLI feature (experimental)

  ```
  Usage:
  cylon <command> [arguments]

  Commands:
  new project <name>                Create new project directory.
  new feature <name>                Create new feature file.
  new pageobject <name>             Create new pageobject file.
  run all                           Run test with all feature.
  run tags <tags>                   Run test with specified tags.
  ```

## 0.5.0 - 2014-06-26
- Added following keywords to support multi-line content

  ```feature
  When user enters following lines to the [element]
      """
      This keyword can enters multi-line content to element.
      1. line 1 content
      2. line 2 content
      """

  Then the [element] value is
      """
      any multi-line content...
      """

  Then the [element] value contains
      """
      any multi-line content...
      """
  ```

- Added accept fail keyword feature

  This feature allow scenario to continue running when the specified step was failed

  To use this feature just add `, accept fail` sentence after normal keyword for example:

  ```feature
  Then the [option1] is selected, accept fail
  Then user enters 'some text' to the [textbox] ## enters text to textbox either option1 was selected or not

  ```

- Added conditional keyword feature

  This feature allow to combine two steps as conditional and execution step,
  these two steps separated by `, ` (comma and one space)

  If conditional step was passed it will continue running the execution step, else it will ignore for example:

  ```feature
  When the [input] value is '1', user selects the [option1]
  When the [input] value is '2', user selects the [option2]
  ```

## 0.4.0 - 2014-06-16
- Added keywords to support url path

  ```feature
  Given User has [ProductDetail/product1] page opened
  Then The browser shows [ProductDetail/product1] page
  ```

  To use above pattern you need to define `url_paths:` in page object file like this.

  ```yaml
  page:
    name: ProductDetail
    url: http://yoursite.com/product
    url_paths:
    - name: product1
      path: /PID00001
    - name: product2
      path: /PID00002
  ```

## 0.3.3 - 2014-05-23
- Fixed to support http authentication url (e.g. ```http://user:pass@site.com```).
- Fixed wait for page load before verify url.

## 0.3.2 - 2014-05-21
- Fixed keywords to verify more than and less than value to compare with natural alphanumeric.
- Fixed code to get current selected value from select list.

## 0.3.1 - 2014-05-19
- Added [Page Analysis](https://github.com/gigapixel/project-cylon/wiki/Page-Analysis) feature.
- Added new keyword.

  ```feature
  Then The [...] value is between '...' and '...'
  ```

- Fixed wait time when check element does not exist.
- Fixed following keywords to support numeric value.

  ```feature
  Then The [...] value is more than '...'
  Then The [...] value is more than or equal '...'
  Then The [...] value is less than '...'
  Then The [...] value is less than or equal '...'
  Then The [...] value is between '...' and '...'
  ```
- Updated verify failure message.

## 0.2.3 - 2014-05-14
- First stable release.
