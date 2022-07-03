from django import template

register = template.Library()

@register.filter
def USD(value):
    return "${:,.2f}".format(value)
