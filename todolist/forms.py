from django import forms
from .models import Choice, Question


class ChoiceForm(forms.Form):
    choice_text = forms.CharField(label='Choice text', max_length=200)
    question = forms.IntegerField(widget=forms.HiddenInput())
    
class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question text', max_length=200)

class UpdateQuestionForm(forms.Form):
    question_text = forms.CharField(label='Question text', max_length=200)
    question = forms.IntegerField(widget=forms.HiddenInput())
    
    
class UpdateChoiceForm(forms.Form):
    choice_text = forms.CharField(label='Choice text', max_length=200)
    question = forms.IntegerField(widget=forms.HiddenInput())
    choice = forms.IntegerField(widget=forms.HiddenInput())