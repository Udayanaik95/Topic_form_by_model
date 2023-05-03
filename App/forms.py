from django import forms
from App.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['topic_name']

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','url']

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields=['author','date']