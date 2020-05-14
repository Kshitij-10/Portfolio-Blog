from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=15)
    date = models.DateField(auto_now=False)
    summary = models.TextField()
    image= models.ImageField(upload_to='blog_images/')

    def summ(self):
        return self.summary[:90]
    def __str__(self):
        return self.title
