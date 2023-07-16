from django import forms

from .models import Review

INPUT_CLASSES = 'w-100 py-1 px-2 rounded border'

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ('content',)

    widgets = {
      'content': forms.Textarea(attrs={
        'class': INPUT_CLASSES,
      }),
    }