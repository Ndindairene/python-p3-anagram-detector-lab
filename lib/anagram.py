# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, match):
        self._match = []
        for word in match:
            if sorted(word) == sorted(self.word) and word != self.word:
                self._match.append(word)
        return self._match
    
    

    
