from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category

def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def buy_now(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        # Here you'd normally save the order
        return render(request, 'products/order_placed.html', {'product': product})

    return render(request, 'products/buy_now.html', {'product': product})
