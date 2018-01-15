from django.db import models
from django.utils import timezone

class Product(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField(blank=True)
        image = models.ImageField(null=True, blank=True)
        image_alt = models.ImageField(null=True, blank=True)
        url_with_notch = models.CharField(max_length=250, blank=True)
        url_without_notch = models.CharField(max_length=250, blank=True)
        premium = models.BooleanField(default=False)
        price = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
        
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title