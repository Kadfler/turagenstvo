from django.db import models
from django.conf import settings


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    tour_id = models.ForeignKey('Tour', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    add_service_id = models.ForeignKey('AddService', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour_id = models.ForeignKey('Tour', on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(default=0)

class AddService(models.Model):
    add_service_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    cost = models.IntegerField(default=0)

class Transport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    carrier= models.TextField()
    type = models.TextField()
    way= models.TextField()

class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    rating = models.IntegerField(default=0)

class Tour_operator(models.Model):
    tour_operator_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    site = models.TextField()
    email = models.TextField()
    country = models.TextField()

class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    transport_id = models.ForeignKey('Transport', on_delete=models.CASCADE)
    program_id = models.ForeignKey('Program', on_delete=models.CASCADE)
    tour_operator_id = models.ForeignKey('Tour_operator', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(auto_now_add=True)
    cost_for_one_person = models.IntegerField(default=0)

class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    title = models.TextField()
    services = models.TextField()
    description = models.TextField()
    country = models.TextField()
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    city = models.TextField()
    meal = models.TextField()
    duration = models.IntegerField(default=0)
    persons = models.TextField()
    activities = models.TextField()
