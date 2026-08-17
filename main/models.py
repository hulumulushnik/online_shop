from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис", blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Ціна"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    is_active = models.BooleanField(default=True, verbose_name="В наявності")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.price} грн"