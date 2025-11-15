from django.shortcuts import render
from products.models import Product


def home(request):
    # Берем 6 последних товаров для показа на главной
    featured_products = Product.objects.filter(available=True).order_by('-created')[:6]

    return render(request, 'core/home.html', {
        'featured_products': featured_products
    })