from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.Charfield(max_length=150)
    content = forms.Charfield()
    is_published = forms.Booleanfield()
    category = forms.ModelChoiceField(queryset=Category.objects.all())