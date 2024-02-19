from django.db import models
import uuid

# Create your models here.

class Item(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )
    name = models.CharField(max_length=255)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', 'price', 'quantity']
    def __str__(self):
        return self.name + ' ' + self.quantity + ' ' + self.description