from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

from .models import product, review
from .serializers import ProductSerializer, ReviewSerealizer
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', ])
def product_list(request):
    if request.method == "GET":
        products = product.objects.all()
        serialized = ProductSerializer(products, many=True)
        
        return JsonResponse(serialized.data, safe=False)
    
@csrf_exempt
@api_view(['GET', 'POST', ])
def product_detail(request, product_id):
    try:
        p = product.objects.get(pk=product_id)
    except product.DoesNotExist:
        content = {'except': 'DoesNotExist'}
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(p)
        return JsonResponse(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST', ])
def review_list(request):
    if request.method == "GET":
        reviews = review.objects.all()
        serialize = ReviewSerealizer(reviews, many=True)
        return JsonResponse(serialize.data, safe=False)

@csrf_exempt
@api_view(['GET', 'POST', ])
def review_detail(request, review_id):
    try:
        r = review.objects.get(review_id=review_id)
    except review.DoesNotExist:
        content = {'except': 'DoesNotExist'}
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerealizer(r)
        return JsonResponse(serializer.data)

def search(request):
    return 0