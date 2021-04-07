from django.db import models
from PIL import Image

class Product(models.Model):
	product_id = models.AutoField
	name = models.CharField(max_length = 100)
	model = models.CharField(default="", max_length = 100)
	price = models.IntegerField(default = 0)
	description = models.TextField()
	category = models.CharField(default="",max_length = 50)
	colours_available = models.CharField(default="",max_length = 100)
	image1= models.ImageField(default='default.jpg', upload_to='image1')
	# image2 = models.ImageField(default='default.jpg', upload_to='image2')
	# image3= models.ImageField(default='default.jpg', upload_to='image3')
	# image4 = models.ImageField(default='default.jpg', upload_to='image4')
	# image5 = models.ImageField(default='default.jpg', upload_to='image5')

	def __str__(self):
		return (self.name) 	

	def save(self):
		super().save()

		# img1 = Image.open(self.image1.path)
		# if img1.height > 300 or img1.width > 300:
		# 	output_size=(300,300)
		# 	img1.thumbnail(output_size)
		# 	img1.save(self.image1.path)	

		