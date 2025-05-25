class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)

        print(dict(cnt))
        ans = 0
        t = 0
        o = False

        for word in words:
            if cnt[word] > 0:
                if word == word[::-1]:
                    if cnt[word]%2 == 0:
                        ans += 2 * cnt[word]
                        cnt[word] = 0
                    else:
                        if not o:
                            o = True
                            ans += 2 * cnt[word]
                            cnt[word] = 0
                        else:
                            ans += (2 * cnt[word]) - 2
                            cnt[word] = 0

                elif cnt[word[::-1]] > 0:
                    ans += 4
                    cnt[word] -= 1
                    cnt[word[::-1]] -= 1
        
        print(t)
        return ans



        