from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


app_name = 'review_production'
urlpatterns = [
    path("api/products", views.product_list),
    path("api/products/search", views.product_search_api),
    path("api/products/<int:product_id>", views.product_detail),
    path("api/products/<int:product_id>/reviews", views.product_reviews),

    path("api/reviews/", views.review_list),
    path("api/reviews/<int:review_id>", views.review_detail),
    path("api/reviews/search", views.reviews_search_api),
    
    path("home/",views.successlogin),
    path("api/search", views.reviews_search_api),
    path('api/login', views.user_login_api),
    path('login', views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
]