from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('favorites/add/<int:product_id>/', views.favorite_add, name='favorite_add'),
    path('favorites/remove/<int:product_id>/', views.favorite_remove, name='favorite_remove'),
    path('update/<int:product_id>/', views.cart_update, name='cart_update'),

]