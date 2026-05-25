
# 📘 Assignment: Hangman

## 🎯 Objective

Build the classic Hangman word-guessing game to practice string manipulation, loops, conditionals, and handling user input in Python.

## 📝 Tasks

### 🛠️ Game Implementation

#### Description
Implement a console Hangman game. The program should select a secret word from a predefined list (starter list is provided in `starter-code.py`) and allow the player to guess letters until they either discover the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list.
- Display the current word progress using underscores for hidden letters (e.g., `_ _ p _ e`).
- Accept single-letter guesses (case-insensitive) and validate input (reject empty, multi-character, or non-alphabetic input).
- Track and show letters already guessed and number of incorrect attempts remaining (suggested default: 6).
- Reveal all occurrences of a correctly guessed letter.
- End the game with a clear win or lose message and show the correct word when the player loses.
- Include a `main()` entry point and break the logic into functions (for example: `choose_word()`, `display_progress()`, `process_guess()`).
- Use the provided `starter-code.py` as a starting point.

Example interaction:

```
Secret word: _ _ p _ e
Guess a letter: a
Incorrect! Attempts remaining: 5
Guess a letter: p
Correct! Current word: _ p p _ e
...
```

### 🛠️ Optional Features (Stretch)

#### Description
Add one or more enhancements to improve the game experience.

#### Requirements

- Add simple ASCII-art for the hangman that updates with incorrect guesses.
- Allow loading words from an external file (e.g., a CSV or plain text) instead of the hardcoded list.
- Add a replay option to start a new game without restarting the program.

Starter code: `starter-code.py`
