from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import product, review
from .serializers import ProductSerializer, ReviewSerealizer
# Create your views here.

@csrf_exempt
def product_list(request):
    if request.method == "GET":
        products = product.objects.all()
        serialize = ProductSerializer(product, many=True)
        return JsonResponse(serialize.data)
    
@csrf_exempt
def product_detail(request, product_id):
    return 0

@csrf_exempt
def review_list(request):
    if request.method == "GET":
        reviews = review.objects.all()
        serialize = ReviewSerealizer(reviews, many=True)
        return JsonResponse(serialize.data)

@csrf_exempt
def review_detail(request, review_id):
    return 0

def search(request):
    return 0