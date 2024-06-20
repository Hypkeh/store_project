from django.urls import path
from django.contrib.auth import views
from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    
    path('search/', views.search, name='search_form'),

    
    path('login/', views.login_view, name='login_view'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),

    path('products/', views.ProductList.as_view(), name='product_list'),
    path('create/', views.ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>', views.ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),

    path('orders/', views.OrderList.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreate.as_view(), name='order_create'),
    path('orders/delete/<int:pk>', views.OrderDelete.as_view(), name='order_delete')
]