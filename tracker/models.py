from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    TRACKING_STATUS_CHOICES = [
        ('IN_TRANSIT', 'In Transit'),
        ('OUT_FOR_DELIVERY', 'Out for Delivery'),
        ('DELIVERED', 'Delivered'),
        ('PICKED_UP', 'Picked Up'),
    ]

    tracking_number = models.CharField(max_length=200, unique=True)
    status = models.CharField(max_length=20, choices=TRACKING_STATUS_CHOICES, default='IN_TRANSIT')
    current_location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Notification(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.package.tracking_number} to {self.user.username}'