# Changelog

## 0.4.0 - 2014-06-16
- Added keywords to support url path
  ```
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
