# For developpers, how to install and work on the app :
Clone with https : https://github.com/Nastyflav/P13-Site-Pypo-Production.git \
or clone with SSH : git@github.com:Nastyflav/P13-Site-Pypo-Production.git\
into a repo on your local machine\
Documentation about pull --> https://help.github.com/en/articles/cloning-a-repository

Set your virtual environment under python3.8.x `pip install virtualenv`\
Create an new virtual environment `virtualenv -p python3 env`\
Activate it `source env/scripts/activate`\
Install all the packages `pip install -r requirements.txt`

Configure your local settings in site_pypo/settings/base.py\
Make the migrations : `python manage.py makemigrations` then `python manage.py migrate`

# Dependancies :
Python 3.8.2
download : https://www.python.org/downloads/ \
install : https://realpython.com/installing-python/

Depending of your python's install, you might need PIP\
install pip : https://packaging.python.org/tutorials/installing-packages/

# Modules :
site_pypo/ general settings\
site_pypo/home/ index, terms, team and generic html pages\
site_pypo/blog/ blog index and articles\
site_pypo/events/ events Django models\
site_pypo/artists/ artists Django models\
site_pypo/contact/ contact Django models and form\
site_pypo/media/ all the images or videos integrated in the project\
site_pypo/tests/ functional tests with Selenium and browsers

# Tests :
To launch tests `python manage.py test`\
If you want to run the tests files, please be sure to locally collect all the static files by running `python manage.py collectstatic`

# Built with :
Visual Studio Code (IDE)\
Python 3.8.2\
UTF-8

# Author :
Flavien Murail : https://github.com/Nastyflav