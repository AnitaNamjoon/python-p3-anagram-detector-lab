class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        return [w for w in words if self.is_anagram(w)]

    def is_anagram(self, other_word):
        return sorted(self.word.lower()) == sorted(other_word.lower())
