from django.contrib.auth import login,authenticate, logout
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response

import json
from .models import product, review
from .serializers import ProductsSerializer, ProductSerializer, ReviewSerealizer
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST', ])
def product_list(request):
    if request.method == "GET":
        page_number = request.GET.get("page",1)
        products = product.objects.all()
        pagnitor  = Paginator(products, 25)

        serialized = ProductsSerializer(pagnitor.get_page(page_number), many=True)
        
        data = {}
        data["page_number"] = page_number
        data["num_pages"] = pagnitor.num_pages
        data["products_list"] = serialized.data
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        pass
    
@csrf_exempt
@api_view(['GET', 'POST', ])
def product_detail(request, product_id):
    try:
        p = product.objects.get(pk=product_id)
    except product.DoesNotExist:
        content = {'except': 'DoesNotExist'}
        return Response(content,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(p)
        
        return JsonResponse(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST',])
def product_reviews(request, product_id):
    try:
        p = product.objects.get(pk=product_id)
    except product.DoesNotExist:
        content = {'except': 'DoesNotExist'}
        return Response(content,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        page_number = request.GET.get("page",1)
        reviews = review.objects.filter(product=p)
        pagnitor  = Paginator(reviews, 25)

        serialized = ReviewSerealizer(pagnitor.get_page(page_number), many=True)

        data = {}
        data["page_number"] = page_number
        data["num_pages"] = pagnitor.num_pages
        data["reviews_list"] = serialized.data
        return JsonResponse(data, safe=False)

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


@api_view(['GET', "POST"])
@csrf_exempt
def user_login_api(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success":True})
        return JsonResponse({"success":False})


def search(request):
    return 0

def successlogin(request):
    return render(request, 'test.html', {'name': request.user.username })

def user_login(request):
    username = request.POST.get('username',"")
    password = request.POST.get('password',"")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'home.html', {'name': request.user.username})
    else:
        return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
