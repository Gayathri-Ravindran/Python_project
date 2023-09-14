from django.db import models

# Create your models here.
# Create table
class Place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    decription=models.TextField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    mode=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    dec=models.TextField()


# class abc(models.Model):
#     s=models.CharField(max_length=200)
#     d=models.TextField()
    def __str__(self):
        return self.mode

