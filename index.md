---
layout: page
title: Welcome to project-cylon
---

This site shows how to create your automated test with project-cylon.


## Getting started
You can follow guide below to quick-start.

NOTE: For Windows users, you need run under drive `C:\` (behave not support to import steps from another drive).

### 1. Create test project

Firstly create new project directory use the command.

{% highlight bash %}
$ cylon new project mytest
{% endhighlight %}

The above command will create new directory name `mytest` in current directory.


### 2. Create feature file

After project directory is ready, walk-in and create new feature file.

{% highlight bash %}
$ cd mytest
$ cylon new feature MyFeature
{% endhighlight %}

This will create `MyFeaure.feature` in the `/features` directory (you can ommit `.feature` in file name).


### 3. Create page object

Then create new page object with following command.

{% highlight bash %}
$ cylon new page MyWebPage
{% endhighlight %}

This will create `MyWebPage.yaml` in the `pageobjects` directory (yes, you can ommit `.yaml` in file name also).


### 4. Run tests

After you have played around feature and page object, run tests with this command.

{% highlight bash %}
$ cylon run all
{% endhighlight %}

The above command will run all features in your project.

If you want to run only tests with specified tag, use this command.

{% highlight bash %}
$ cylon run tags=@mytag1
{% endhighlight %}

This command will run scenario specified with tag `@mytag1`.


## Documentation

For more documentation please see following pages.

[Write test scenario in feature file.]({{ site.baseurl }}/document/feature-file.html)  
[Mapping elements in page object.]({{ site.baseurl }}/document/page-object.html)  
[Built-in steps.]({{ site.baseurl }}/document/built-in-steps.html)


## FAQ

__Ask:__  
What does "Cylon" stand for?  

__Ans:__  
The name "Cylon" is inspired from the
American science fiction series named ["Battlestar Galactica"](http://en.wikipedia.org/wiki/Battlestar_Galactica).


<!--<div class="posts">
  {% for post in paginator.posts %}
  <div class="post">
    <h1 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h1>

    <span class="post-date">{{ post.date | date_to_string }}</span>

    {{ post.content }}
  </div>
  {% endfor %}
</div>

<div class="pagination">
  {% if paginator.next_page %}
    <a class="pagination-item older" href="{{ site.baseurl }}page{{paginator.next_page}}">Older</a>
  {% else %}
    <span class="pagination-item older">Older</span>
  {% endif %}
  {% if paginator.previous_page %}
    {% if paginator.page == 2 %}
      <a class="pagination-item newer" href="{{ site.baseurl }}">Newer</a>
    {% else %}
      <a class="pagination-item newer" href="{{ site.baseurl }}page{{paginator.previous_page}}">Newer</a>
    {% endif %}
  {% else %}
    <span class="pagination-item newer">Newer</span>
  {% endif %}
</div>-->
