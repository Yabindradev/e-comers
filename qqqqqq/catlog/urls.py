from django.urls import path
from .import views

# app_name = 'catlog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/',views.product_detail, name='product_detail'),
    path('help', views.help, name='help'),
    path('login', views.login, name='login'),
    path('singup', views.singup, name='singup'),
    path('logout', views.logout, name='logout'),
    path('sell', views.sell, name='sell'),
    path('dmain', views.dmain, name='dmain'),
    path('dashbord', views.dashbord, name='dashbord'),
    path('products', views.products, name='products'),
    path('create', views.create, name='create'), 
    path('category', views.category, name='category'),
    path('user_informaction', views.user_informaction, name="user_informaction"),
    path('overview', views.overview, name="overview"),
    path('cart', views.cart, name="cart"),


    ]

