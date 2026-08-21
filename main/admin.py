from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "is_active", "image_tag")
    list_filter = ("is_active", "created_at", "category")
    search_fields = ("name", "description")
    list_editable = ("is_active",)
    prepopulated_fields = {"slug": ("name",)}

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
        return format_html('<span>{}</span>', "немає зображення")

    image_tag.short_description = "Зображення"