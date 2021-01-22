from . import views

from django.urls import path

urlpatterns = [
    path('shops/user_shops/', views.ShopsViewSet.as_view({'get': 'list'})),
    path('shops/shop/<id>', views.ShopsViewSet.as_view({'get': 'retrieve'})),
    path('shops/create_shop/', views.CreateShop.as_view()),
    path('servers/user_servers/', views.ServersViewSet.as_view({'get': 'list'})),
    path('servers/server/<id>', views.ServersViewSet.as_view({'get': 'retrieve'})),
]
