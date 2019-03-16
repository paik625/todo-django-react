from django.db import models

# Create your models here.
class Todoapp(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



    def __self__(self):
        return self.title
