tango-with-django-project
=========================

Tango with Django - Working through section by section

# Using Django 1.6

The Tango with Django tutorial specifies 1.5.4. This is a walk-through to see what changes are needed when using Django 1.6.

# Cloning and Installation

Create a working directory (for example, ~/devel) and change to it:

    $ mkdir ~/devel
    $ cd ~/devel
    
Create virtual environment for project using virtualenvwrapper:

    $ mkvirtualenv twd --no-site-packages
    $ workon twd
    
Clone git repository:

    (twd)$ git clone git@github.com/ChrisFreeman/tango-with-django-project.git
    
This creates the directory `~/devel/tango-with-django-project`.  Change to this directory and install python packages using pip_install script. This script adds switches to the standard pip install -r requirements.txt command for proper installation of PIL package.

    (twd)$ cd tango-with-django-project
    (twd)$ ./pip_install

Start local server and test installation:

    (twd)$ python manage.py runserver

Open browser and visit URL [http://127.0.0.1:8000/rango](http://127.0.0.1:8000/rango).  You should see the top "Rango" webpage at the latest chapter completion.  See below to checkout the website at other points during development.

# See Tango with Django Revisions for Other Chapter Completions

At the completion of each major chapter in Tango with Django the code was committed and tagged. To see the finished code for a specific chapter, checkout the corresponding tag.

Use git tag to see a list of tags:

    (twd)$ git tag
    v0.0
    v3.7
    v4.6
    v5.10
    v6.4
    v7.3
    v8.8
    v9.4
    v10.9
    v11.5

Use git checkout to see the code as it was at the end of a specific chapter.  For example, to see the code at the end of Chapter 4, type:

    (twd)$ git checkout v4.6
