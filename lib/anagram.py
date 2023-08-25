# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert the word to lowercase for case-insensitive comparison
    
    def match(self, possible_anagrams):
        anagrams = []
        
        for candidate in possible_anagrams:
            if self._is_anagram(candidate):
                anagrams.append(candidate)
        
        return anagrams
    
    def _is_anagram(self, candidate):
        candidate_lower = candidate.lower()  # Convert candidate to lowercase for case-insensitive comparison
        
        if candidate_lower == self.word:
            return False  # The same word is not considered an anagram
        
        return sorted(candidate_lower) == sorted(self.word)