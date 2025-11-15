from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm


@login_required
def review_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # УБИРАЕМ ПРОВЕРКУ НА СУЩЕСТВУЮЩИЙ ОТЗЫВ
    # Теперь пользователь может оставлять несколько отзывов на один товар

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, 'Ваш отзыв успешно добавлен!')
            return redirect('products:product_detail', product_id=product.id, product_slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_add.html', {
        'form': form,
        'product': product,
    })