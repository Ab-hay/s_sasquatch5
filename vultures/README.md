

# Vultures

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/vultures.git
    $ cd vultures
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
