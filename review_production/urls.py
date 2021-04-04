
from django.urls import path

from . import views



urlpatterns = [
    path("api/products/", views.product_list),
    path("api/products/<str:product_id>", views.product_detail),
    path("api/products/<str:product_id>/reviews", views.product_reviews),

    path("api/reviews/", views.review_list),
    path("api/reviews/<str:review_id>", views.review_detail),
    
    path("api/search", views.search),

]