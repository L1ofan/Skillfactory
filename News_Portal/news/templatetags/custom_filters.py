from django import template


register = template.Library()

STOP_LIST = [
    'мат',
    'мат',
    'мат',
    'asdas',
]

CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CURRENCIES_SYMBOLS[code]

   return f'{value} {postfix}'


@register.filter()
def censor(value):
    for word in STOP_LIST:
        value = value.replace(word[1:], '*' * len(word[1:]))
    return value
