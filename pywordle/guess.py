from PyDictionary import PyDictionary

dictionary = PyDictionary()

class Guess:
    def __init__(self, word=None):
        self.word = None if word is None else word
        self.GREEN_LETTERS = 0
        self.MAX_ATTEMPTS = 6

    def correct_letters(self):
        self.GREEN_LETTERS += 1

    @classmethod
    def get_guess(cls):
        new_guess = input("Guess word: ").lower().strip()
        return Guess(new_guess)
    
    def validate(self):
        MAX_LETTERS = 5

        if dictionary.meaning(self.word, 
                        disable_errors=True) and len(self.word) == MAX_LETTERS:
            return True
        
        return False
    