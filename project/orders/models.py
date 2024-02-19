from django.db import models
import uuid
from django.contrib.auth.models import User
from items.models import Item

import uuid
import random
import string

# Create your models here.

class Order(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )
    # code = models.CharField(max_length=255)
    # amount = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=255, editable=False, unique=True)  # Updated to be non-editable and unique
    amount = models.PositiveIntegerField(default=0)
    quantity = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    items = models.ManyToManyField(Item, related_name='orders') # Order will have manyToMany relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Order will have oneToOne relationship
    # item = models.ForeignKey(Item, related_name='items', on_delete=models.CASCADE) # Order will have oneToMany relationship

    # Generate a random string automatically for the code field
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.ascii_uppercase, k=8))
        super().save(*args, **kwargs)