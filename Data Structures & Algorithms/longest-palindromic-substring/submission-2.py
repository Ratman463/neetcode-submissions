class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = 0
        n = len(s)
        d = {}

        for i in range(n):
            #print(d)

            cnt1 = 1
            str1 = s[i]
            p1, p2 = i-1, i+1
            while p1 >= 0 and p2 <= n-1:
                if s[p1] == s[p2]:
                    cnt1 += 2
                    str1 = s[p1] + str1 + s[p2]
                    p1 -= 1
                    p2 += 1
                else:
                    break
            d[cnt1] = str1
            
            cnt2 = 0
            str2 = ""
            p1, p2 = i, i+1
            while p1 >= 0 and p2 <= n-1:
                if s[p1] == s[p2]:
                    str2 = s[p1] + str2 + s[p2]
                    cnt2 += 2
                    p1 -= 1
                    p2 += 1
                else:
                    break
            d[cnt2] = str2

            #print([cnt1, cnt2])

            best = max(cnt1, cnt2, best)

        #print(best)
        return d[best]


            