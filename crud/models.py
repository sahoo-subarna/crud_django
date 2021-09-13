from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    createdat = models.DateTimeField(auto_now_add=True)
    is_complited = models.BooleanField(default=False)


    def __str__(self):
        return self.title
