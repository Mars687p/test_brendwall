from django import template
from django.db.models import Model

register = template.Library()


@register.filter
def verbose_name(the_object: Model, name_field: str) -> str:
    return the_object._meta.get_field(name_field).verbose_name
