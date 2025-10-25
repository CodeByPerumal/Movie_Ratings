from django import forms
from app.models import Movie


class DateInput(forms.DateInput):
    input_type = 'date'

class MoviesForm(forms.ModelForm):
    moviename = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie name'})
    )
    rdate = forms.DateField(
        widget=DateInput(attrs={'class': 'form-control'})
    )
    hero = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter hero name'})
    )
    heroine = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heroine name'})
    )
    rating = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating (0–10)', 'min': '0', 'max': '10', 'step': '0.1'})
    )

    class Meta:
        model = Movie
        fields = ['moviename', 'rdate', 'hero', 'heroine', 'rating']
