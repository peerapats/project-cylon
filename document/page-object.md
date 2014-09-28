---
layout: page
title: Page object
---

Page object is an object repository for project-cylon,
we use yaml format to store identifier of page and elements.

Page object basiacally require `page:` and `elements:` sections.


## Page

This section keep name and url for html page, require 2 fields in this section.

* `name:` Specified page name to use in feature file.
* `url:` Specified URL of this page.

Here is an example:

{% highlight yaml %}
page:
  name: GoogleHomePage
  url: https://www.google.com
{% endhighlight %}


## Elements

This section keep name and xpath of each elements under the page,
each elements require 2 fields following.

* `name:` Specified element name to use in feature file.
* `xpath:` Specified xpath to identify this element.

Here is an example:

{% highlight yaml %}
elements:
- name: txt_search
  xpath: //*[@id="gbqfq"]
- name: btn_search
  xpath: //*[@id="gbqfb"]
{% endhighlight %}


## Put it all together

When put it all together, the `GoogleHomePage.yaml` file will look like this example.

{% highlight yaml %}
--- ## Google Home Page
page:
  name: GoogleHomePage
  url: https://www.google.com

elements:
- name: txt_search
  xpath: //*[@id="gbqfq"]
- name: btn_search
  xpath: //*[@id="gbqfb"]

...
{% endhighlight %}


## Multiple page in one file

You can have multiple page store in the same file,
separate each page by `---` like this example.

{% highlight yaml %}
--- # Google Home Page
page:
  name: GoogleHomePage
  url: https://www.google.com

elements:
- name: txt_search
  xpath: //*[@id="..."]
- name: btn_search
  xpath: //*[@id="..."]

--- # Gmail Page
page:
  name: GmailPage
  url: https://www.gmail.com

elements:
- name: txt_email
  xpath: //*[@id="..."]
- name: txt_password
  xpath: //*[@id="..."]

...
{% endhighlight %}


## References

For fully details of YAML please see: [YAML Wiki](http://en.wikipedia.org/wiki/YAML)  
For fully details of XPath please see: [XPath Wiki](http://en.wikipedia.org/wiki/XPath)
