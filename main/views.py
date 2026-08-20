from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request, category_slug=None):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        "title": "Каталог товарів",
        "categories": categories,
        "category": category,
        "products": products,
    }
    return render(request, "main/product_list.html", context)


def product_detail(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id, slug=product_slug, is_active=True)
    product.views += 1
    product.save(update_fields=["views"])
    return render(request, "main/product_detail.html", {"product": product})