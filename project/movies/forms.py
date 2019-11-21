from django import forms
from .models import Movie, Review


class ReviewForm(forms.ModelForm):
    score = forms.IntegerField(
        label='평점',
        min_value=0,
        max_value=10,
    )
    class Meta:
        model = Review
        fields = ('content', 'score')
