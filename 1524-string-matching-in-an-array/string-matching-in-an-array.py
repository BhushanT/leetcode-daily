class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for word in words:
            for word_2 in words:
                if word != word_2:
                    if word in word_2:
                        ans.add(word)
        return list(ans)