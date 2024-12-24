from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название товара")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, null=True, verbose_name="Описание товара")


    def __str__(self):
        return self.name
