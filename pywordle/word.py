from wonderwords import RandomWord

r = RandomWord()

class Word:
    def __init__(self):
        self.length = 5
        self.random_word = r.word(word_min_length=self.length, 
                                  word_max_length=self.length).lower()