from rest_framework import serializers
from .models import product, review
from django.contrib.auth.models import User


class UserSerealizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name']
        
class ReviewSerealizer(serializers.ModelSerializer):
    user = UserSerealizer()
    class Meta:
        model = review
        fields = ['review_id', 'user', 'rating', 'title', 'comment_text']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerealizer(many=True)
    class Meta:
        model = product
        fields = ['product_id', 'product_name', 'catagories', 'reviews']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['product_id', 'product_name', 'catagories',]

class NewReviewSerealizer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ['user', 'rating', 'title', 'comment_text']
    
    def to_representation(self, instance):
        self.fields['user'] =  UserSerializer(read_only=True)
        return super(NewReviewSerealizer, self).to_representation(instance)
