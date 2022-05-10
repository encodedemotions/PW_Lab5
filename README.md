# bussiness-news-app

To run the application you need `Python version 3.7`, create a virtual environment and use `pip install -r requirements.txt`.
After the installation is complete run the following commands to create the database:

  1. `python manage.py makemigrations` 
  2. `python manage.py migrate`

Finally use `python manage.py createsuperuser`, to create the admin user that will assign staff status to the user for 
obtaining editor rights.
