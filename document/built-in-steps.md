---
layout: page
title: Built-in steps
---

This page lists all built-in steps in project-cylon, you can use steps below to write scenario in features file.


## Given

The purpose of __Given__ steps is __to put the system in a known state__ before the user (or external system) starts interacting with the system.

```gherkin
Given user has [...] page open
```


## When

The purpose of __When__ steps is __to describe an action__ that user performs.

```gherkin
When user enters '...' to the [...]
When user enters date '...' to the [...]
When user clears value on the [...]
When user clicks the [...]
When user selects the [...]
When user selects '...' on the [...]
When user checks the [...]
When user unchecks the [...]
When user moves mouse over the [...]
When user uploads file '...' to the [...]
When user enters '...' to the popup
When user accept the popup
When user cancel the popup
```


## Then

The purpose of __Then__ steps is __to observe outcomes__. The observations should be related to the business value/benefit in your feature description.

```gherkin
Then the browser shows [...] page
Then the page url is '...'
Then the page url contains '...'
Then the page has '...' items of [...]
Then the [...] value is '...'
Then the [...] value is not '...'
Then the [...] value contains '...'
Then the [...] value is more than '...'
Then the [...] value is more than or equal '...'
Then the [...] value is less than '...'
Then the [...] value is less than or equal '...'
Then the [...] value is empty
Then the [...] value is not empty
Then the [...] exists
Then the [...] does not exist
Then the [...] is visible
Then the [...] is invisible
Then the [...] is checked
Then the [...] is unchecked
Then the [...] is selected
Then the [...] is not selected
Then the [...] tooltip text is '...'
Then the popup message shows '...'
```


## And / But

Purpose of __And__ / __But__ is to make scenario more readable rather than use multiple __Given__, __When__ or __Then__.

```gherkin
Scenario: Search on google
    Given user has [Google Home] page open
     When user enters 'abc' to the [search input]
      And user clicks the [search button]
     Then the browser shows [Google Search Result] page
      And the [search input] is not empty
      And the [search button] exists
```

Steps beginning with __And__ or __But__ are exactly the same kind of steps as all the others.
