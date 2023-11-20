from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if cart is None:
        return False

    keys = cart.keys()
    for id in keys:
        # Skip 'null' and None values
        if id in ('null', None):
            continue

        if int(id) == product.id:
            return True

    return False
    

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    if cart is None:
        return 0

    keys = cart.keys()
    for id in keys:
        # Check for 'null' before attempting to convert to an integer
        if id == 'null':
            continue

        if int(id) == product.id:
            return cart.get(id)

    return 0
 