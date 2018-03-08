import datetime

from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import default


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote_amount = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
    
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    
    
    def __str__(self):
        return self.choice_text
    
class Votes(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE) 
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    class Meta:
        unique_together = ("voter", "question")