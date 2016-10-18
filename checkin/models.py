from django.db import models

class Checkin(models.Model):
    student_id = models.CharField(max_length=16)
    time = models.DateTimeField()

    def __str__(self):
        return '{} @ {}'.format(self.student_id, self.time)
