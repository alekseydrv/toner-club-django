from django.db import models

class Queries(models.Model):

	# Query text, which user type in form
	queryText = models.TextField()

	# Datetime of query
	date = models.DateField(auto_now="True")

	class Meta:
		ordering = ["queryText"]

	# Methods
	def __str__(self):
		return self.queryText

class Products(models.Model):

	# Unique ID of product
	productId = models.TextField()

	# Name of product
	productName = models.TextField()

	# Price of product
	productPrice = models.DecimalField(max_digits = 10, decimal_places = 2)

	# Image of product
	productImage = models.ImageField(upload_to='images/')

	# Stock of product in shop
	productStock = models.CharField(max_length = 15)

	# Product Manufacturer
	productManufacturer = models.CharField(max_length = 30)

	# Shop id, where this product is
	productShopId = models.IntegerField()

	def __str__(self):
		return self.productName

class Dependensies(models.Model):

	# Unique id of cartridge
	cartridgeId = models.CharField(max_length = 10)

	# Type of cartridge: 1 - original, 0 - compatible
	cartridgeType = models.IntegerField()

	# Model of printer
	modelPrinter = models.TextField()

	# Mark of printer
	markPrinter = models.TextField()
