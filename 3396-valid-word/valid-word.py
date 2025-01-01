class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3:
            return False

        if not all(char.isalnum() for char in word):
            return False
    
        vowels = set("aeiouAEIOU")
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

        has_vowel = False
        for char in word:
            if char in vowels:
                has_vowel = True
                break

        has_consonant = False
        for char in word:
            if char in consonants:
                has_consonant = True
                break
    
        return has_vowel and has_consonant