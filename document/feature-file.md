---
layout: page
title: Feature file
---

A feature file is a plain-text written in __Gherkin__ format,
it use for describing test scenario with expected outcomes.

All feature files are save in `.feature`,
basically require following sections.


## Feature

Every feature files start with the keyword `Feature:` followed by any free text.
You can write whatever you want until the first scenario.

Here is an example:

{% highlight gherkin %}
Feature: Your feature name
    Write your feature description / documentation.
    You can write whatever you want up until the first scenario.
Scenario:
    ...
{% endhighlight %}


## Scenario

Every scenario start with the keyword `Scenario:`,
it consists of a list of steps which must start with one of the keywords __Given__, __When__, __Then__, __And__ or __But__.

Here is an example:

{% highlight gherkin %}
Scenario: Verify stock info
    Given User has [Settrade Home] page open
     When User enters 'ICHI' to the [symbol input]
      And User clicks the [search button]
     Then The browser shows [Stock Details] page
      And The [symbol] value is 'ICHI'
{% endhighlight %}


## Scenario Outline

Sometimes a scenario should be run with multiple set of variables and they are using the same basic scenario.
Instead of write several scenario for each data set, you can use a `Scenario Outline:` and `Examples:` to make it repetitive.

Here is an example:

{% highlight gherkin %}
Scenario Outline: Verify stock info
    Given User has [Settrade Home] page open
     When User enters '<symbol>' to the [symbol input]
      And User clicks the [search button]
     Then The browser shows [Stock Details] page
      And The [symbol] value is '<symbol>'
      And The [price] value is more than '<floor>'
      And The [price] value is less than '<ceil>'

Examples:
    | symbol | floor   | ceil   |
    | ADVANC | 171.00  | 317.00 |
    | INTUCH | 55.00   | 99.00  |
    | MCOT   | 20.20   | 37.25  |
{% endhighlight %}

This will run scenario once for each line in the `Examples:` data tables.


## Background

The `Background:` section allows to add repetitive steps to the beginning of all scenarios.
when each scenario is run, steps under `Background:` will run before that scenario.

Here is an example:

{% highlight gherkin %}
Background:
    Given User has [Settrade Home] page open
      And ...
      And ...

Scenario: scenario 1
     When ...
     Then ...

Scenario: scenario 2
     When ...
     Then ...
{% endhighlight %}

For all available steps to write scenario please see: [Built-in steps]({{ site.baseurl }}document/built-in-steps.html)
