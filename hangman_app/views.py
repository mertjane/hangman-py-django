# hangman_app/views.py

from django.shortcuts import render, redirect
from .models import HangmanGame
from .forms import HangmanForm
import random

def start_game(request):
    words = ['python', 'django', 'hangman', 'programming', 'javascript', 'dog', 'cat', 'building', 'school']
    word_to_guess = random.choice(words)
    game = HangmanGame.objects.create(word_to_guess=word_to_guess)
    return redirect('play_game', game_id=game.id)

def play_game(request, game_id):
    game = HangmanGame.objects.get(id=game_id)

    if request.method == 'POST':
        form = HangmanForm(request.POST)

        if form.is_valid():
            letter = form.cleaned_data['letter'].lower()
            guess_word = form.cleaned_data['guess_word'].lower()

            if guess_word == game.word_to_guess:
                game.is_winner = True
                game.save()
                return render(request, 'hangman_app/result.html', {'game': game, 'result_message': 'Congratulations! You Win!'})

            if guess_word:
                # Check if guessed word is incorrect, then declare user a loser
                if guess_word != game.word_to_guess:
                    game.attempts_left = 0
                    return render(request, 'hangman_app/result.html', {'game': game, 'result_message': 'Sorry! You Lose!'})


                if set(guess_word) == set(game.word_to_guess):
                    game.is_winner = True
                    game.save()
                    return render(request, 'hangman_app/result.html', {'game': game, 'result_message': 'Congratulations! You Win!'})

            if letter.isalpha() and letter not in game.guessed_letters:
                game.guessed_letters += letter

                if letter not in game.word_to_guess:
                    game.attempts_left -= 1

                if set(game.guessed_letters) == set(game.word_to_guess):
                    game.is_winner = True
                    game.save()
                    return render(request, 'hangman_app/result.html', {'game': game, 'result_message': 'Congratulations! You Win!'})

                game.save()
                form = HangmanForm()  # Clear the letter input in the form after submission

                if game.attempts_left == 0:
                    return render(request, 'hangman_app/result.html', {'game': game, 'result_message': 'Sorry! You Lose!'})

    else:
        form = HangmanForm()

    return render(request, 'hangman_app/play_game.html', {'game': game, 'form': form})
