import hashlib
import random
from review_production.models import *

import os
import csv
from password_generator import PasswordGenerator
file = open("C:/Users/peeza/PycharmProjects/djangoProject2/scripts/archive/1429_1.csv",encoding="utf8")
csv = csv.reader(file)
def run():
    create_review_object()
def create_user_object():
    password = PasswordGenerator()
    password.excludeschars = "!$%^{}[]()=/"
    count = 0
    for test in csv:
        if count == 0:
            pass
            count = count + 1
        elif count == 1000:
            break
        else :
            passw = hashlib.md5(password.generate().encode())
            User.objects.create(username=test[20],password=passw.hexdigest())
            count = count + 1
def create_product_object():
    dup = []
    for test in csv:
        if test[1] not in dup:
            product.objects.create(product_name=test[1],catagories=test[4])
            dup.append(test[1])
def create_review_object():
    count = 0
    dup = []
    review_count = 0
    for test in csv:
        if count == 0 :
            pass
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
                review.objects.create(title=test[17],comment_text=test[16],rating=test[14],product=product_select,user=user_select)
            except user_select.MultipleObjectsReturned:
                user_select = User.objects.filter(username=test[20]).first()
                review.objects.create(title=test[17], comment_text=test[16], rating=test[14], product=product_select,
                                      user=user_select)
            else:
                review.objects.create(title=test[17],comment_text=test[16],rating=test[14],product=product_select,user=user_select)
            review_count = review_count + 1
        print(count,test[1])
        count = count + 1


def run():
    product.objects.all().delete()

