from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
now = timezone.now()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class TakenPoll(models.Model):
    user = models.CharField(max_length=200)
    poll = models.CharField(max_length=200)
    poll_id = models.BigIntegerField()
    time_taken = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "Poll ID:{} User:{}  Poll:{}".format(self.poll_id, self.user, self.poll)
