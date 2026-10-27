"""
CodeAlpha Python Internship - Task 1: Hangman Game

A simple text-based Hangman game.
- 5 predefined words (no file or API needed)
- 6 incorrect guesses allowed
- Console input/output only

Concepts used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "variable", "function", "keyboard", "internet"]
MAX_WRONG = 6

STAGES = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def show_word(word, correct_letters):
    """Return the word with unguessed letters hidden, e.g. 'p _ t _ _ n'."""
    shown = []
    for letter in word:
        if letter in correct_letters:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def ask_for_letter(all_guesses):
    """Keep asking until the player enters one new letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter from a to z.")
        elif guess in all_guesses:
            print(f"You already tried '{guess}'. Pick a different letter.")
        else:
            return guess


def play_round():
    """Play one game of Hangman. Returns True if the player won."""
    word = random.choice(WORDS)
    correct_letters = []
    wrong_letters = []

    print("\nI have picked a word. You can miss 6 times. Good luck!")

    while len(wrong_letters) < MAX_WRONG:
        print(STAGES[len(wrong_letters)])
        print("\nWord:", show_word(word, correct_letters))
        print("Wrong guesses:", ", ".join(wrong_letters) if wrong_letters else "none")
        print(f"Chances left: {MAX_WRONG - len(wrong_letters)}")

        guess = ask_for_letter(correct_letters + wrong_letters)

        if guess in word:
            correct_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_letters.append(guess)
            print(f"Sorry, '{guess}' is not in the word.")

        # Win check: every letter of the word has been guessed
        if all(letter in correct_letters for letter in word):
            print("\nWord:", show_word(word, correct_letters))
            print(f"You won! The word was '{word}'.")
            return True

    print(STAGES[MAX_WRONG])
    print(f"\nGame over. The word was '{word}'.")
    return False


def main():
    print("=" * 36)
    print("          HANGMAN GAME")
    print("=" * 36)

    wins = 0
    played = 0

    while True:
        played += 1
        if play_round():
            wins += 1

        print(f"\nScore: {wins} won out of {played} played.")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
