from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Product, Category
from .forms import ContactForm
from .cart import Cart


def product_list(request, category_slug=None):
    products = Product.objects.select_related('category').filter(is_active=True)
    categories = Category.objects.all()
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    sort = request.GET.get('sort', 'new')
    if sort == 'old':
        products = products.order_by('created_at')
    elif sort == 'popular':
        products = products.order_by('-views', '-created_at')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:
        sort = 'new'
        products = products.order_by('-created_at')

    context = {
        "title": f"Категорія: {category.name}" if category else "Каталог товарів",
        "categories": categories,
        "category": category,
        "products": products,
        "current_sort": sort,
    }
    return render(request, "main/product_list.html", context)


def product_detail(request, id, slug):
    product = get_object_or_404(
        Product.objects.select_related('category'),
        id=id,
        slug=slug,
        is_active=True,
    )

    # Атомарний інкремент переглядів, безпечний при паралельних запитах
    Product.objects.filter(id=id).update(views=F('views') + 1)
    product.refresh_from_db(fields=['views'])

    related_products = Product.objects.filter(
        category=product.category,
        is_active=True,
    ).exclude(id=product.id).select_related('category')[:4]

    context = {
        "title": product.name,
        "product": product,
        "related_products": related_products,
    }
    return render(request, "main/product_detail.html", context)

def contact_view(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = f"Повідомлення з форми контактів: {data['subject']}"
            message = (
                f"Ім'я: {data['name']}\n"
                f"Email: {data['email']}\n\n"
                f"Повідомлення:\n{data['message']}"
            )
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, "Ваше повідомлення успішно надіслано! Ми зв'яжемося з вами найближчим часом.")
                return redirect("main:contact")
            except Exception:
                messages.error(request, "Виникла помилка під час надсилання повідомлення. Спробуйте пізніше.")
    else:
        form = ContactForm()

    return render(request, "main/contact.html", {
        "form": form,
        "categories": categories,
        "title": "Контакти",
    })


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    override_quantity = request.POST.get('override_quantity') == 'True'
    cart.add(product=product, quantity=quantity, override_quantity=override_quantity)
    return redirect('main:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('main:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'main/cart_detail.html', {'cart': cart})
