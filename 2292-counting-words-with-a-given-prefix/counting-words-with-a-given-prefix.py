class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        pref_length = len(pref)
        for word in words:
            if pref == word[:pref_length]:
                count +=1
        return count