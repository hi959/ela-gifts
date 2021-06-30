from django.db import models

# Create your models here.

class Products(models.Model):
	name = models.CharField('שם המוצר', max_length=100)
	price = models.FloatField('מחיר המוצר')
	description = models.TextField("תיאור", blank=True)
	image = models.ImageField('למונה',upload_to="product_images/")
	count = models.IntegerField('מחיר')

	def __str__(self):
		return self.name
