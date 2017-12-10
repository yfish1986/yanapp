# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.
class JwColour(models.Model):
    colour_name = models.CharField(max_length=20)
    colour_type = models.CharField(max_length=20)
    def __str__(self):
        return self.colour_name

class JwStyle(models.Model):
    style_name = models.CharField(max_length=20)
    def __str__(self):
        return self.style_name

class JwSize(models.Model):
    size_name = models.CharField(max_length=20)
    def __str__(self):
        return self.size_name

#客户
class JwCustomer(models.Model):
    customer_name = models.CharField(max_length=20,default='张三')
    customer_phone = models.CharField(max_length=20,default='无')
    customer_addr = models.CharField(max_length=20,default='无')
    def __str__(self):
        return self.customer_name
#进货清单
class JwStockList(models.Model):
    colour_name = models.ForeignKey(JwColour)
    style_name = models.ForeignKey(JwStyle)
    size_name = models.ForeignKey(JwSize)
    num = models.IntegerField(default=1)
    price = models.FloatField(default=1)
    total = models.FloatField(default=1)
    stock_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return "%s-%s-%s"%(self.colour_name,self.style_name,self.size_name)
#存货清单
class JwBra(models.Model):
    style_name = models.ForeignKey(JwStyle)
    colour_name = models.ForeignKey(JwColour)
    size_name = models.ForeignKey(JwSize)
    num = models.IntegerField(default=0)
    price = models.FloatField(default=1)
    total = models.FloatField(default=0)
    def __str__(self):
        return "%s-%s-%s"%(self.colour_name,self.style_name,self.size_name)

class JwSalesBill(models.Model):
    customer_name = models.ForeignKey(JwCustomer)
    jwbra = models.ForeignKey(JwBra)
    sale_date = models.DateTimeField(default=timezone.now())
    sale_num = models.IntegerField(default=1)
    sale_price = models.FloatField(default=1)
    total = models.FloatField(default=1)
    def __str__(self):
        return "%s-%s-%s" % (self.customer_name,self.jwbra,self.sale_date)



