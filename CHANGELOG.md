# Changelog

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
