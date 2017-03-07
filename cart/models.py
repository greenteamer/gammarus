# -*- coding: utf-8 -*-
from django.db import models
from core.models import Product, PropertyValue
from django.contrib.auth.models import User
# from authentication.models import Account


class CartItem(models.Model):
    product = models.ForeignKey(Product)
    property = models.ForeignKey(PropertyValue, blank=True, null=True)
    # user = models.ForeignKey(Account)
    count = models.IntegerField()
    cart_id = models.CharField(max_length=240)

    class Meta:
        verbose_name = u'Объект корзины'
        verbose_name_plural = u'Корзина'

    def total_price(self):
        return self.count * self.product.price

    # def url(self):
    #     return self.product.url()

    def __unicode__(self):
        return u"cartItem - " + self.product.name


class Order(models.Model):
    user = models.ForeignKey(User)
    cart_id = models.CharField(max_length=240)
    is_paid = models.BooleanField(default=False)

    def get_all_cart_items(self):
        return CartItem.objects.filter(cart_id=self.cart_id)

    def total_price(self):
        cart_items = self.get_all_cart_items()
        price = 0
        for item in cart_items:
            price = price + item.total_price()
        delivery = Delivery.objects.get(cart_id=self.cart_id)
        price = price + delivery.price
        return price

    class Meta:
        verbose_name = u'Обьект заказа'
        verbose_name_plural = u'Заказы'

    def __unicode__(self):
        return u"Order - " + self.user.get_full_name()


class Delivery(models.Model):
    area = models.CharField(max_length=240, blank=True, null=True)
    area_type = models.CharField(max_length=240, blank=True, null=True)
    block = models.CharField(max_length=240, blank=True, null=True)
    block_type = models.CharField(max_length=240, blank=True, null=True)
    postal_code = models.CharField(max_length=240, blank=True, null=True)
    country = models.CharField(max_length=240, blank=True, null=True)
    region = models.CharField(max_length=240, blank=True, null=True)
    region_type = models.CharField(max_length=240, blank=True, null=True)
    city = models.CharField(max_length=240, blank=True, null=True)
    city_type = models.CharField(max_length=240, blank=True, null=True)
    street = models.CharField(max_length=240, blank=True, null=True)
    street_type = models.CharField(max_length=240, blank=True, null=True)
    settlement = models.CharField(max_length=240, blank=True, null=True)
    settlement_type = models.CharField(max_length=240, blank=True, null=True)
    house = models.CharField(max_length=240, blank=True, null=True)
    house_type = models.CharField(max_length=240, blank=True, null=True)
    flat = models.CharField(max_length=240, blank=True, null=True)
    flat_type = models.CharField(max_length=240, blank=True, null=True)

    cart_id = models.CharField(max_length=240)

    provider_name = models.CharField(max_length=240, blank=True, null=True)
    provider_type = models.CharField(max_length=240, blank=True, null=True)
    days = models.IntegerField(default=0, blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = u'Доставка'
        verbose_name_plural = u'Доставка'

    def get_current_order(self):
        return Order.objects.get(cart_id=self.cart_id)

    def __unicode__(self):
        return u"Delivery - %s" % self.get_current_order().id


class CartInfoHelper():
    cart_id = ''
    delivery_price = 0
    item_price = 0
    total_price = 0

    def get_all_cart_items_helper(self):
        return CartItem.objects.filter(cart_id=self.cart_id)

    def cart_total_price_helper(self):
        cart_items = self.get_all_cart_items_helper()
        self.item_price = 0
        for item in cart_items:
            self.item_price = self.item_price + item.total_price()

    def get_total_price(self):
        self.cart_total_price_helper()
        self.total_price = self.delivery_price + self.item_price
        return self.total_price
