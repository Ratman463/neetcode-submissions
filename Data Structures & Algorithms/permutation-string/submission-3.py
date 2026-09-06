class Solution:
    def isSameDick(self, arr1, arr2) -> bool:
        if(len(arr1) == len(arr2)):
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True
        return False
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicks = [0] * 26
        new_dicks = [0] * 26

        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False

        for i in range(l1):
            dicks[ord(s1[i]) - ord('a')] += 1
            new_dicks[ord(s2[i]) - ord('a')] += 1
        
        if self.isSameDick(dicks, new_dicks):
            return True

        for i in range(1, l2 - l1 + 1):            
            newChar = ord(s2[i + l1 - 1]) - ord('a')
            oldChar = ord(s2[i - 1]) - ord('a')

            new_dicks[newChar] += 1
            new_dicks[oldChar] -= 1

            # print(i)
            # print(dicks)
            # print(new_dicks)

            if self.isSameDick(dicks, new_dicks):
                return True
        
        return False