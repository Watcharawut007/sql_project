import hashlib
import random
import os
import csv

from django.contrib.auth.models import User
from review_production.models import *

from password_generator import PasswordGenerator
file = open("C:/Users/peeza/PycharmProjects/djangoProject2/sql_project/scripts/archive/1429_1.csv",encoding="utf8")
csv = csv.reader(file)

def run():
    create_user_object()
def create_dummy_object():
    password = '123'

    User.objects.get(username='dummy',password=password)
def create_user_object():
    password = PasswordGenerator()
    password.excludeschars = "!$%^{}[]()=/"
    count = 0
    dup = []
    for test in csv:
        if count == 0:
            pass
            count = count + 1
        elif count == 1000:
            break
        elif test[20] in dup:
            pass
        elif count == 1:
            passw = "12345"
            user = User.objects.create(username="usertest")
            user.set_password(passw)
            user.save()
            dup.append(test[20])
            count = count + 1
        else :
            passw = password.generate()
            print(test[20],passw+'\n')
            User.objects.create(username=test[20])
            user = User.objects.get(username=test[20])
            user.set_password(passw)
            user.save()
            dup.append(test[20])
            count = count + 1

def create_product_object():
    for test in csv:
        if not(product.objects.filter(product_name=test[1]).exists()):
            product.objects.create(product_name=test[1],catagories=test[4])
            
def create_review_object():
    count = 0
    dup = []
    review_count = 0
    for test in csv:
        if (review.objects.filter(title=test[17],comment_text=test[16]).exists()):
            continue
        if count == 0 :
            count =  count + 1
        elif (review_count > 90 and test[1] in dup) or test[14] == '' or len(test[16]) > 9999:
            pass
        else :
            product_select= product.objects.filter(product_name=test[1]).first()
            if test[1] not in dup:
                review_count = 0
            try :
                user_select = User.objects.get(username=test[20])
            except user_select.DoesNotExist :
                user_id = random.randrange(1,115)
                user_select = User.objects.get(id=user_id)
                review.objects.create(title=test[17],comment_text=test[16],rating=int(test[14]),product=product_select,user=user_select)
            except user_select.MultipleObjectsReturned:
                user_select = User.objects.filter(username=test[20]).first()
                review.objects.create(title=test[17], comment_text=test[16], rating=int(test[14]), product=product_select,
                                      user=user_select)
            else:
                review.objects.create(title=test[17],comment_text=test[16],rating=int(test[14]),product=product_select,user=user_select)
            review_count = review_count + 1
        print(count,test[1])
        count = count + 1




