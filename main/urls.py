from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("", views.home, name='home'),
    path('seller_signup/', views.seller_signup, name='seller_signup'),
    path('item/new/', views.ItemFormView.as_view(), name='new_item'),
    path('inventory/', views.seller_items, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('new_sale/', views.new_sale, name='new_sale'),
    path('new_customer/', views.new_customer, name='new_customer'),
    path('customer_orders/', views.customer_orders, name='customer_orders'),
    path('profile/', views.SellerProfileView.as_view(), name='profile'),
]