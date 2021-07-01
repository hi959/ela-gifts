from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Product(models.Model):
	name = models.CharField('שם המוצר', max_length=100)
	price = models.FloatField('מחיר המוצר', validators=[MinValueValidator(5)])
	description = models.TextField("תיאור המוצר", blank=True)
	image = models.ImageField('תמונת המוצר',upload_to="product_images/")
	count = models.PositiveIntegerField('כמות המוצר')
	tapStatus = models.BooleanField('לעשות מבצע ?', default=False)
	sale_price = models.FloatField('מחיר המבצע', validators=[MinValueValidator(5)])


	def __str__(self):
		return self.name
