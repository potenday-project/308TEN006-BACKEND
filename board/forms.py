from django import forms
from .models import Memos

class PostForm(forms.ModelForm):
    price = forms.DecimalField(
        label='가격',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        decimal_places=0  # 소수점 이하 자리수
    )

    class Meta:
        model = Memos
        fields = ['title', 'text', 'experience_date', 'price', 'district', 'platform', 'tag_text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'platform': forms.TextInput(attrs={'class': 'form-control'}),
            'tag_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '제목',
            'text': '내용',
            'experience_date': '체험 날짜',
            'district': '지역',
            'platform': '예약 플랫폼',
            'tag_text': '태그',
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None:
            # 가격에 세자리마다 쉼표 추가
            formatted_price = format(price, ',')
            return formatted_price
