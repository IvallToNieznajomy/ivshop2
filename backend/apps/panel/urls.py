from . import views

from django.urls import path

urlpatterns = [
    path('shops/user_shops/', views.ShopsViewSet.as_view({'get': 'list'})),
    path('shops/create_shop/', views.CreateShop.as_view())
]
