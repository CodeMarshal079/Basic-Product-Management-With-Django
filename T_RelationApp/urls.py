from django.urls import path
from T_RelationApp.views import *

urlpatterns = [
    # Authentication
    path('', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),

    # Dashboard
    path('dashboard/', dashboardPage, name='dashboard'),

    # Category
    path('category/', addCategory, name='category'),

    # Product
    path('product/', addProductPage, name='addProduct'),
    path('product/edit/<int:id>/', productEdit, name='editpro'),
    path('product/delete/<int:id>/', productDelete, name='deletepro'),
    path('viewproduct/<int:id>/', viewPage, name='viewProduct'),

    # Orders
    path('orderlist/', orderListPage, name='orderList'),
    path('order/<int:id>/', orderPage, name='order'),
    path('order/delete/<int:id>/', orderDelete, name='orderDelete'),
]