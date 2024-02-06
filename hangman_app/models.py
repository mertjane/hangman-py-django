# hangman_app/models.py

from django.db import models

class HangmanGame(models.Model):
    word_to_guess = models.CharField(max_length=50)
    guessed_letters = models.CharField(max_length=50, default='')
    attempts_left = models.IntegerField(default=10)
    is_winner = models.BooleanField(default=False)
