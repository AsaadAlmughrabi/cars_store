from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    is_bought = models.BooleanField(default=False, blank=False)
    buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    buy_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"
    

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})