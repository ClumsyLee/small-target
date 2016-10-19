from django.db import models
from django.utils import timezone
import datetime

class Student(models.Model):
    student_id = models.CharField(max_length=10)
    lastcheckintime = models.DateField(default=timezone.now)
    checkintimes = models.IntegerField()
    def __str__(self):
        return self.student_id

class Checkin(models.Model):
    student = models.ForeignKey(Student,related_name='record',on_delete=models.CASCADE,null = True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} @ {}'.format(self.student_id, self.time)
