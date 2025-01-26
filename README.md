# Hangman Game

Welcome to the **Hangman Game**, a fun and engaging way to test your word-guessing skills! This Python-based implementation of the classic hangman game includes a visual representation of your progress as you try to guess the hidden word, one letter at a time.

---

## Features
- **Interactive Gameplay**: Guess letters and reveal the hidden word.
- **Dynamic Visuals**: Watch the hangman figure evolve with each incorrect guess.
- **Loss Screen**: Get an amusing surprise if you run out of guesses!
- **Simple Controls**: Play the game with just your keyboard.

---

## How to Play
1. **Start the Game**:
   - Run the Python script `refactored_hangman.py`.
   - The program will display a series of asterisks (`*`), representing the hidden word.
2. **Make Guesses**:
   - Type a letter and press `Enter`.
   - If the letter is in the word, it will replace the corresponding asterisks.
   - If the letter is not in the word, the hangman figure will gradually appear.
3. **Win or Lose**:
   - Reveal the entire word before the hangman figure is complete to win.
   - If the figure is fully drawn, you lose, and a funny loss screen will appear.

---

## Requirements
- **Python**: Version 3.6 or later
- **Matplotlib**: For visualizing the hangman figure

Install dependencies using pip:
```bash
pip install matplotlib
```

---

## Code Structure
### Main Components:
1. **`Hangman` Class**:
   - Handles the core game logic and state.
   - Manages the word to guess, the used letters, and the player's progress.
2. **`display_hangman` Method**:
   - Draws the hangman figure progressively as the player makes incorrect guesses.
3. **`play` Method**:
   - Main loop for player input and game progression.

### Example Usage:
```python
if __name__ == "__main__":
    word_to_guess = 'python'
    game = Hangman(word_to_guess)
    game.play()
```

---

## Customization
- **Change the Word**: Replace the `word_to_guess` variable with your desired word.
- **Adjust Maximum Misses**: Modify the `max_misses` attribute in the `Hangman` class.
- **Add More Fun**: Replace the loss screen image (`hang_fuck.png`) with a custom image to personalize the game.

---

## Known Limitations
- Only one-word phrases are supported.
- The hangman image relies on Matplotlib, so ensure the library is installed.

---

## Have Fun!
Challenge your friends and family, and see who can guess the word fastest! Enjoy this humorous take on the classic hangman game.

---

## License
This game is open-source and available for personal use. Feel free to modify and distribute it as you wish.
