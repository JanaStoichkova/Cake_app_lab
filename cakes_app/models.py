from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Baker(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    desciption = models.TextField()
    image = models.ImageField()
    baker = models.ForeignKey(Baker, on_delete=models.CASCADE, related_name='cakes', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

