from django import forms
from item.models import Category

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['name']