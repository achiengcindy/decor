from django import template
from products.models import Category
import locale
from decimal import Decimal

register = template.Library()
@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL,'om_KE.utf8')
    except:
        locale.setlocale(locale.LC_ALL,'')
    value =Decimal(value)
    loc = locale.localeconv()
    return locale.currency(value, loc['currency_symbol'], grouping=True)

@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
    active_categories = Category.objects.filter(is_active=True)
    return {'active_categories': active_categories,'request_path': request_path}
