from decimal import Decimal
from django.db import models, migrations
from django.conf import settings
from datetime import datetime
from marketplace.models import prodProduct
from member.models import Person



class Basket(models.Model):

    class Meta:
        db_table = 'basket'
    productqty = models.IntegerField(default=0)
    productid = models.ForeignKey(prodProduct, on_delete=models.CASCADE)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_checkout = models.BooleanField(default=0)
    transaction_code = models.CharField(max_length=255,null=True)
    
    def save(self):
        super().save()
    
    # def get_subtotal_price(self, fk1):
    #     basket_items = Basket.objects.select_related('product').filter(product__pk=fk1)
    #     subtotal = sum(Decimal(item.product.productPrice) * item.productqty for item in basket_items)
    #     return subtotal

    # def get_total_price(self, fk1):
    #     subtotal = self.get_subtotal_price(fk1)
    #     SHIPPING_CHARGE = Decimal(3.00)
    #     total = subtotal + SHIPPING_CHARGE
    #     return total
    # def deleteProduct(self):
    #     super().delete()

    # def __init__(self, productqty, productid, Person_fk):
    #     # self.session = request.session
    #     # basket = self.session.get(settings.BASKET_SESSION_ID)
    #     # if settings.BASKET_SESSION_ID not in request.session:
    #     #     basket = self.session[settings.BASKET_SESSION_ID] = {}
    #     # self.basket = basket
    #     self.productqty = productqty
    #     self.productid = productid
    #     self.Person_fk = Person_fk

    # def add(self, product, qty=1, update_qty=False):
    #     """
    #     Adding and updating the users basket session data
    #     """
    #     product_id = str(product.id)

    #     if product_id not in self.basket:
    #         self.basket[product_id] = {'qty': 0, 'price': str(product.price)}
    #     self.basket[product_id]['qty'] += qty

    #     self.save()

    # def __iter__(self):
    #     """
    #     Collect the product_id in the session data to query the database
    #     and return products
    #     """
    #     product_ids = self.basket.keys()
    #     products = prodProduct.products.filter(id__in=product_ids)
    #     basket = self.basket.copy()

    #     for product in products:
    #         basket[str(product.id)]['product'] = product

    #     for item in basket.values():
    #         item['price'] = Decimal(item['price'])
    #         item['total_price'] = item['price'] * item['qty']
    #         yield item

    # def __len__(self):
    #     """
    #     Get the basket data and count the qty of items
    #     """
    #     return sum(item['qty'] for item in self.basket.values())

    # def update(self, product, qty):
    #     """
    #     Update values in session data
    #     """
    #     product_id = str(product)
    #     if product_id in self.basket:
    #         self.basket[product_id]['qty'] = qty
    #     self.save()

    # def get_subtotal_price(self, fk1):
    #     product = prodProduct.objects.get(pk=fk1)
    #     basket = Basket.objects.all()
    #     return sum(Decimal(product['productPrice']) * basket['productqty'])

    # def get_total_price(self, fk1):
    #     product = prodProduct.objects.get(pk=fk1)
    #     basket = Basket.objects.all()
    #     subtotal = sum(Decimal(product['productPrice']) * basket['productqty'])

    #     if subtotal == 0:
    #         shipping = Decimal(0.00)
    #     else:
    #         shipping = Decimal(3.00)

    #     total = subtotal + Decimal(shipping)
    #     return total

    # def delete(self, product):
    #     """
    #     Delete item from session data
    #     """
    #     product_id = str(product)

    #     if product_id in self.basket:
    #         del self.basket[product_id]
    #         self.save()

    # def clear(self):
    #     # Remove basket from session
    #     del self.session[settings.BASKET_SESSION_ID]
    #     self.save()

    # def save(self):
    #     self.session['basket'] = self.basket
    #     self.session.modified = True