from django.db import models
from django.forms import ModelForm

from store_manage.models import StoreComment


class CommentForm(ModelForm):
    class Meta:
        model = StoreComment
        fields = ['content']