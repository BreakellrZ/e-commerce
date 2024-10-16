from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Reviews(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField(max_length=100)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review by {self.author} on {self.product}'
