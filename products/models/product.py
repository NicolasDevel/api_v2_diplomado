from django.db import models
from .category import Category
from .tag import Tag 
from users.models import User #Importo el modelo de user

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        null=True
        )
    #Agregar una relacion de muchos a muchos con la tabla tags
    tags = models.ManyToManyField(
        Tag,
        blank = True,
        related_name = 'products'
    )

    #Agregar relación con usuarios
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        null = True 
    )
    

    def __str__(self):
        return self.name
