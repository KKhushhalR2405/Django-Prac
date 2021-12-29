import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task2.settings')

import django
django.setup()


import random
from app1.models import User
from faker import Faker 

fakegen = Faker()

def add_name(n = 10):
    for _ in range(n):
        fname = fakegen.first_name()
        lname = fakegen.last_name()
        email = fakegen.email()

        print(fname,lname,email)
        u = User.objects.get_or_create(first_name = fname, last_name = lname, email = email)[0]


if __name__ == '__main__':
    print("Populating scripts")
    add_name(20)