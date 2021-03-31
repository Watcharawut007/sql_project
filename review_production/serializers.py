from rest_framework import serializers
from .models import product, review

class ReviewSerealizer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ['review_id',  'rating', 'Title', 'comment_text']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerealizer(many=True)
    class Meta:
        model = product
        fields = ['product_id', 'product_name', 'catagories', 'reviews']

