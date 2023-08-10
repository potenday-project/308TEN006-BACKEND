from django import forms
from .models import Memos

class PostForm(forms.ModelForm):

    class Meta:
        model = Memos
        fields = ['title', 'text', 'experience_date', 'price', 'district', 'platform', 'tag_text', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'platform': forms.TextInput(attrs={'class': 'form-control'}),
            'tag_text': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '제목',
            'text': '내용',
            'experience_date': '체험 날짜',
            'price': '가격',
            'district': '지역',
            'platform': '예약 플랫폼',
            'tag_text': '태그',
            'category': '카테고리',
        }
