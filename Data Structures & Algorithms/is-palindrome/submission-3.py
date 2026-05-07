class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while(not self.isAlpha(s[i])):
                i+=1
                if(i >= len(s)):
                    return True
            while(not self.isAlpha(s[j])):
                j-=1
                if(j < 0):
                    return True
            if(i>=j):
                return True
            if(self.toUpperCaseInt(s[i]) != self.toUpperCaseInt(s[j])):
                return False
            i+=1
            j-=1
        return True


    @staticmethod
    def isAlpha(a: chr) -> bool:
        res = ord(a)
        if(res >= ord('A') and res <= ord('Z')):
            return True
        elif(res >= ord('a') and res <= ord('z')):
            return True
        elif(res >= ord('0') and res <= ord('9')):
            return True
        else:
            return False

    @staticmethod
    def toUpperCaseInt(a: chr) -> int:
        res = ord(a)
        if(res > ord('Z')):
            return res - (ord('a') - ord('A'))
        else:
            return res