class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        ans = [0] * len(queries)

        # [2,5] = [0,5] - [0,1]

        dp = [0] * len(words)

        for i,word in enumerate(words):
            if i == 0:
                if word[0] in vowels and word[-1] in vowels:
                    dp[i] = 1
                else:
                    dp[i] = 0
            else:
                temp = 0
                if word[0] in vowels and word[-1] in vowels:
                    temp = 1
                dp[i] = dp[i - 1] + temp 

        print(dp)
        for i,query in enumerate(queries):
            if query[0] == 0:
                ans[i] = dp[query[1]]
            else:
                ans[i] = dp[query[1]] - dp[query[0] - 1]

        return ans