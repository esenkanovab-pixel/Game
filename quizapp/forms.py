from django import forms
from .models import Player, Question

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'answer']
