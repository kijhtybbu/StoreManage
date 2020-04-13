from django.db import models
from django.forms import ModelForm, Textarea

from store_manage.models import StoreComment


class CommentForm(ModelForm):
    class Meta:
        model = StoreComment
        fields = ['content']
        labels = {
            'content': '#',
        }
        widgets = {
            'content': Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 5}),
        }
