from django.db import models
from item.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
  product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user