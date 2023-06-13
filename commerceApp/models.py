from django.db import models
from django.utils import timezone

class Featured_Products(models.Model):
        image=models.ImageField(upload_to='static/Featured_Products_images')
        name = models.CharField(max_length=100)
        description = models.TextField()
        date_posted=models.DateTimeField(default=timezone.now)
        rating = models.FloatField()
        cost = models.FloatField()


        def __str__(self):
        

           return self.name


class Sales_Information(models.Model):
      name=models.CharField(max_length=200)
      description = models.TextField()
      date_starts=models.DateTimeField()
      date_ends=models.DateTimeField()
      offer = models.FloatField()
      def __str__(self):
        

           return self.name



    
    
       


# Create your models here.
