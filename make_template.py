content = '''{% extends 'base.html' %}

{% block title %}{{ title }}{% endblock %}

{% block content %}
<div class="categories-menu">
    <a href="{% url 'main:product_list' %}" class="{% if not category %}active{% endif %}">\u0412\u0441\u0456 \u0442\u043e\u0432\u0430\u0440\u0438</a>
    {% for cat in categories %}
    <a href="{{ cat.get_absolute_url }}" class="{% if category.slug == cat.slug %}active{% endif %}">
        {{ cat.name }} ({{ cat.products.count }})
    </a>
    {% endfor %}
</div>

<div class="sort-container">
    <span class="sort-label">\u0421\u043e\u0440\u0442\u0443\u0432\u0430\u0442\u0438:</span>
    <div class="sort-buttons">
        <a href="?sort=new" class="sort-btn {% if current_sort == 'new' or not current_sort %}active{% endif %}">\u041d\u043e\u0432\u0456</a>
        <a href="?sort=old" class="sort-btn {% if current_sort == 'old' %}active{% endif %}">\u0421\u0442\u0430\u0440\u0456</a>
        <a href="?sort=popular" class="sort-btn {% if current_sort == 'popular' %}active{% endif %}">\u041f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u0456</a>
        <a href="?sort=price_asc" class="sort-btn {% if current_sort == 'price_asc' %}active{% endif %}">\u0414\u0435\u0448\u0435\u0432\u0448\u0456</a>
        <a href="?sort=price_desc" class="sort-btn {% if current_sort == 'price_desc' %}active{% endif %}">\u0414\u043e\u0440\u043e\u0436\u0447\u0456</a>
    </div>
</div>

{% if products %}
<div class="products">
    {% for product in products %}
    <div class="card">
        <a href="{{ product.get_absolute_url }}">
            {% if product.image %}
            <img src="{{ product.image.url }}" alt="{{ product.name }}">
            {% else %}
            <div class="no-image">\u0417\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f \u0432\u0456\u0434\u0441\u0443\u0442\u043d\u0454</div>
            {% endif %}
            <h3>{{ product.name }}</h3>
        </a>
        <p class="price">{{ product.price }} \u0433\u0440\u043d</p>
        <p class="views-count">{{ product.views }} \u043f\u0435\u0440\u0435\u0433\u043b\u044f\u0434\u0456\u0432</p>
        <a href="{{ product.get_absolute_url }}" class="btn-details">\u0414\u0435\u0442\u0430\u043b\u044c\u043d\u0456\u0448\u0435</a>
    </div>
    {% endfor %}
</div>
{% else %}
<p>\u0422\u043e\u0432\u0430\u0440\u0456\u0432 \u043f\u043e\u043a\u0438 \u043d\u0435\u043c\u0430\u0454.</p>
{% endif %}
{% endblock %}
'''

with open('main/templates/main/product_list.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Файл успішно перезаписано!")