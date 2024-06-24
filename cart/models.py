from django.db import models
from Myapp.models import Obra
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Carrito de {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Obra, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.nombre}"