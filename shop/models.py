from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Categorie(models.Model):
	name = models.CharField('שם הקטגוריה', max_length=20, unique=True)
	

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField('שם המוצר', max_length=100)
	price = models.FloatField('מחיר המוצר', validators=[MinValueValidator(5)])
	description = models.TextField("תיאור המוצר", blank=True)
	image = models.ImageField('תמונת המוצר', upload_to="product_images/")
	count = models.PositiveIntegerField('כמות המוצר')
	sale = models.BooleanField('לעשות מבצע ?', default=False)
	sale_price = models.FloatField('מחיר המבצע', validators=[MinValueValidator(5)])
	category = models.ManyToManyField(Categorie, 'קטגוריות', blank=True, default='uncategorized')
	hot_product = models.BooleanField('להוסיף למוצרים חמים ?', default=False)
	recomanded_product = models.BooleanField('להוסיף להמלצות שלי?', default=False)


	def __str__(self):
		return self.name


class HeaderImages(models.Model):
	image = models.ImageField('הוספת תמונה לראש האתר', upload_to="header/")


	def __str__(self):
		return self.image.name
