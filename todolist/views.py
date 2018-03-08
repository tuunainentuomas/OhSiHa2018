from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.db.models import Count

from django.http import HttpResponse
from django.template import loader

from .models import Question, Choice, Votes

from django.db.models.aggregates import Count

from .forms import ChoiceForm, QuestionForm, UpdateQuestionForm, UpdateChoiceForm

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'todolist.html', context)