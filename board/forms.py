from django import forms
from django.db import models

from .models import Memos

class PostForm(forms.ModelForm):
    class Meta:
        model = Memos
        # fields = ['text2','images', 'secret', 'text', 'text3' ]
        fields = ['text2','text', 'text3' ]

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'text2': forms.TextInput(attrs={'class': 'form-control'}),
            'text3': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'text': '태그',
            'text2': '본문 내용',
            'text3': '지역 태그',
        }
