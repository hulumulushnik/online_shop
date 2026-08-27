from django import template
from django.utils import timezone

register = template.Library()


def _pluralize_days(days):
    """Відмінює слово «день» відповідно до української граматики."""
    last_two = days % 100
    last_one = days % 10

    if 11 <= last_two <= 14:
        word = "днів"
    elif last_one == 1:
        word = "день"
    elif 2 <= last_one <= 4:
        word = "дні"
    else:
        word = "днів"

    return f"{days} {word}"


@register.simple_tag
def days_on_site(date_joined):
    """Показує, скільки днів користувач зареєстрований на сайті."""
    delta = timezone.now() - date_joined
    days = delta.days

    if days <= 0:
        return "перший день"

    return _pluralize_days(days)
