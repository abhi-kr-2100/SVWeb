from django.db import models


class StudyTip(models.Model):
    text = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text