from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem, Favorite


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
        'cart_items': cart_items,
    })


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Количество товара "{product.name}" увеличено')
    else:
        messages.success(request, f'Товар "{product.name}" добавлен в корзину')

    return redirect('cart:cart_detail')


@login_required
def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()

    messages.success(request, f'Товар "{product.name}" удален из корзины')
    return redirect('cart:cart_detail')


@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'cart/favorite_list.html', {'favorites': favorites})


@login_required
def favorite_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        product=product
    )

    if created:
        messages.success(request, f'Товар "{product.name}" добавлен в избранное')
    else:
        messages.info(request, f'Товар "{product.name}" уже в избранном')

    return redirect('products:product_detail', product_id=product.id, product_slug=product.slug)


@login_required
def favorite_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    favorite = get_object_or_404(Favorite, user=request.user, product=product)
    favorite.delete()

    messages.success(request, f'Товар "{product.name}" удален из избранного')
    return redirect('cart:favorite_list')


@login_required
def cart_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    cart_item = get_object_or_404(CartItem, cart=cart, product=product)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f'Количество товара "{product.name}" изменено')
        else:
            cart_item.delete()
            messages.success(request, f'Товар "{product.name}" удален из корзины')

    return redirect('cart:cart_detail')