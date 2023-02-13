from email import message
from django.db import models
from django.contrib.auth.models import User
from home.models import Films

# Create your models here.
class ToWatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Films, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=250, null=False)
    total_price = models.IntegerField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=True)
    tracking_number =  models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_number)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    film = film = models.ForeignKey(Films, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_number)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    