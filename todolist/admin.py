from django.contrib import admin

from .models import Question, Choice, Votes

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Votes)