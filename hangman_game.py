import matplotlib.pyplot as plt
import time
import matplotlib.image as mpimg

class Hangman:
    def __init__(self, word):
        self.word = word.upper()
        self.stars = ['*' for _ in word]
        self.used_letters = []
        self.misses = 0
        self.max_misses = 11
        self.game_over = False

    def display_hangman(self):
        stages = [
            lambda: plt.plot([0, 4], [-1, -1], 'k', linewidth=5),
            lambda: plt.plot([2, 2], [-1, 10], 'k'),
            lambda: plt.plot([2, 9], [10, 10], 'k'),
            lambda: plt.plot([2, 4], [8, 10], 'k'),
            lambda: plt.plot([9, 9], [10, 8], 'k'),
            lambda: plt.plot(9, 7.5, 'ko', markersize=20),
            lambda: plt.plot([9, 9], [8, 4], 'k'),
            lambda: plt.plot([8, 9], [6, 6], 'k'),
            lambda: plt.plot([9, 10], [6, 6], 'k'),
            lambda: plt.plot([9, 8], [4, 2], 'k'),
            lambda: plt.plot([9, 10], [4, 2], 'k')
        ]

        plt.xlim((-1, 11))
        plt.ylim((-1, 11))
        plt.axis('off')

        for i in range(self.misses):
            stages[i]()

        plt.show()

    def check_letter(self, letter):
        positions = [pos for pos, char in enumerate(self.word) if char == letter]

        if positions:
            print('Good job!')
            for pos in positions:
                self.stars[pos] = self.word[pos]
        else:
            self.misses += 1
            print('Wrong letter!')
            self.display_hangman()

            if self.misses == self.max_misses:
                print('You lost!')
                self.game_over = True

    def play(self):
        print(' '.join(self.stars))

        while '*' in self.stars and not self.game_over:
            letter = input('Guess a letter: ').upper()

            if letter in self.used_letters:
                print('This letter was already used!')
            else:
                self.used_letters.append(letter)
                self.check_letter(letter)
                print(' '.join(self.stars))

        if '*' not in self.stars:
            print('Well done!!!')

# Example Usage
if __name__ == "__main__":
    word_to_guess = 'word'
    game = Hangman(word_to_guess)
    game.play()
