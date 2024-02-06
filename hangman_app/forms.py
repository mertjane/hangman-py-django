# hangman_app/forms.py

from django import forms

class HangmanForm(forms.Form):
    letter = forms.CharField(max_length=1, required=False)
    guess_word = forms.CharField(max_length=50, required=False)
