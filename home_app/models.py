from django.db import models

class Wish(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    link = models.CharField(max_length=200)
    comment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "wishes"