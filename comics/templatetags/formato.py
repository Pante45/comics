from django import template

register = template.Library()


@register.filter
def pesos_chilenos(valor):
    if valor is None:
        return "$0"

    return f"${int(valor):,}".replace(",", ".")