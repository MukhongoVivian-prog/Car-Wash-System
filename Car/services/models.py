from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

from django.db import models

class Plan(models.Model):

    class PlanName(models.TextChoices):
        BASIC = 'basic', 'Basic'
        STANDARD = 'standard', 'Standard'
        PREMIUM = 'premium', 'Premium'

    type = models.CharField(max_length=50)
    name = models.CharField(
        max_length=20,
        choices=PlanName.choices,
        default=PlanName.BASIC
    )

