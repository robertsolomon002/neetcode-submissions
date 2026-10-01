class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) +1)
        dp[len(s)] =True

        for i in range(len(s)-1,-1,-1):
            for words in wordDict:
                split_word = s[i:i+ len(words)]
                #print(len(words))
                #print(split_word)
                if split_word == words:
                    #print(i)
                    #print(words)
                    dp[i] = dp[i] or dp[i+len(words)]
        print(dp)
        return dp[0]

        