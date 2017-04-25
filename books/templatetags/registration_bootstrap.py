# coding=utf-8
from django import template
register = template.Library()

@register.filter()
def add_class(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter()
def add_attr(field,attr):
   return field.as_widget(attrs={"placeholder":attr})

def placeholder(value, token):
	value.field.widget.attrs["placeholder"] = token
	return value

register.filter(placeholder)