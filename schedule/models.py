from django.db import models



class Schedule(models.Model):
    teacher = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    class_date = models.CharField(max_length=10)
    class_time = models.CharField(max_length=5, null=True)
    student = models.CharField(max_length=50)