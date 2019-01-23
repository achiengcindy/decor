from decimal import Decimal
from django.conf import settings
from products.models import Product

class Cart(object):
    def __init__(self, request):
    """
    Initialize the cart.
    """
    self.session = request.session
    cart = self.session.get(settings.CART_SESSION_ID)
    if not cart:
        # save an empty cart in the session
        cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    """ add products to cart or update quantities """
    def add(self, product, quantity=1, update_quantity=False, date):
        """ convert the product id into a string because 
        Django uses JSON to serialize session data, 
        and JSON only allows string key names """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True


