Title: Setting up pelican blog on github pages
Date: 2016-03-25 07:20
Category: Python
Tags: pelican, publishing
Slug: setup-pelican
Authors: Sathya Narrayanan
Summary: Pelican is a static site generator written on python. You can convert github pages as a very powerful blogging platform with the help of pelican.

Two days back I was trying to setup a blog with wordpress on 512 MB digitalocean machine. 
Since the package consists of PHP, MYSQL, PHPMYADMIN etc. It turned out to be too much for 
the machine to handle. After that I was searching for some cheap alternative. 

## Github pages to the resuce

Github provides its pages service which lets the github user host any static site for there
repository. All your have to do is create a repository in the format ```username.github.io```
and put all your html and css files there. 


## Pelican the powerful companion

Pelican is a static site generator written on python. You can convert github pages as a very 
powerful blogging platform with the help of pelican. Pelican supports ```.rst .md .html`` content
formats.

The way to setup your pelican blog in github pages is given below.

* I am assuming you have already created a repository in the format username.github.io.
* do a ```pip install pelican```.
* fire up ```pelican-quickstart``` from your terminal. Pelican will be prompting few questions which you would like to answer.
* And then the fun part. Writing your blog.

## How pelican works

Once you have completed the above process you will end with the folder structure as following.
    
```md
    output/                # has all your html and css, javascript outputs.
    content/               # has you input files like .md, .rst etc.
    develop_server.sh 
    fabfile.py             # python fablicfile
    Makefile
    pelicanconf.py
    publishconf.py
```

## Commands you will be needing.

What you will be doing is create a source .rst or .md file in content directory. Once you are done with it you
will be compiling to html files and upload the output directory to github. Along the run.

```
make devserver  #run the pelican devserver which can be accessible in http://localhost:8000
make html       #builds .html, .css, .js files from .rst and .md files. (.css, .js, .html taken from themes)

``` 

## Building your first post.

For .RST

```
My super title
##############

:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds

My first super post

```

For .md 

```
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```

Place your file inside content directory and file up ```make html```. Open http://localhost:8000 to view the change.

## Customising your blog

If you have been seeing this blog. Its written based on the theme of [pelican-clean-blog](https://github.com/gilsondev/pelican-clean-blog). Often people want to change their blog themes. So these are the procedures to do so.


```
  # Lets clone the above theme.
  mkdir themes
  git clone --recursive https://github.com/gilsondev/pelican-clean-blog themes/

```

After that add the below changes to pelicanconf.py

```
# pelicanconf.py

...
THEME = 'themes/pelican-clean-blog'
...

```

Now do a ```make html``` again you are done. For more details you can check this link [customising](http://docs.getpelican.com/en/3.6.3/themes.html).


## Upload

Once you are done.

```
cd output/
git init
git remote add origin https://yourrepo.git
git add --all
git commit -m "My first new blog"
git push origin master

```

Open your browser and look at username.github.io to view your blog.

You are done now, Enjoy !



