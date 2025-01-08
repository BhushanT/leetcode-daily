class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i,word in enumerate(words):
            for j,word_alt in enumerate(words):
                if j > i and self.isPrefixAndSuffix(word, word_alt):
                    print("Words:" + word + ", " + word_alt)
                    count += 1
        return count

    def isPrefixAndSuffix( self, word_1, word_2):
        if len(word_1) > len(word_2):
            return False
        print( word_1 + "," + word_2 + " , " + word_2[len(word_2)-len(word_1):] + " , " + word_2[:len(word_1)])
        if word_1 == word_2[len(word_2)-len(word_1):] and word_1 == word_2[:len(word_1)]:
            return True
        else:
            return False