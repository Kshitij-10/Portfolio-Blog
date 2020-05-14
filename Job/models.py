from django.db import models


class Job(models.Model):
    summary=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
