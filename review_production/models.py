from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=2000)
    catagories = models.CharField(max_length=1000)

    def __str__(self):
        return self.product_name
    
class review(models.Model):
    rating_score = [1,2,3,4,5]
    review_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000)
    comment_text = models.CharField(max_length=10000)
    rating = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    product =  models.ForeignKey(product,on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.Title
    

