class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 200

        if(len(s) != len(t)):
            return False

        for i,j in zip(s,t):
            arr[ord(i)] += 1
            arr[ord(j)] -= 1
        
        for i in range(len(arr)):
            if(arr[i]) != 0:
                return False
        return True

