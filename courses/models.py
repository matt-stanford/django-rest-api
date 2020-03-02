from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.name

    objects = models.Manager()
