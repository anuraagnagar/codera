from flask_script import Manager
from flask_blog import Users as User
from app import app
import re

# flask-scripts for application cli.
manager = Manager(app)

@manager.command
def createdb():
    """Create database for application"""
    print("DB Created Succesfully")


@manager.command
def createadmin():
    """Create superuser for application"""
    username = input("Username : ")
    email = input("Email Address : ")
    password = input("Password : ")

    # create admin user.
    admin = User(username=username, email=email, password=password)
    admin.set_password(password)
    admin.superuser = True
    admin.save()


if __name__ == '__main__':
    manager.run()