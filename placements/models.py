from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    department = models.CharField(max_length=30)
    cgpa = models.FloatField()

    def __str__(self):
        return self.name
