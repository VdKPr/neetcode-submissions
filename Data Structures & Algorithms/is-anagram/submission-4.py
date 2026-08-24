# for num in s:
#     if num in t:            this is not right

# think like 
# 1. Count every character in s
# 2. Count every character in t
# 3. Compare the two frequency tables

        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        # count chat in s
        count_s = {}
        for char in s:
            if char in count_s:
                count_s[char] +=1
            else:
                count_s[char] = 1

        # count chat in t
        count_t = {}
        for char in t:
            if char in count_t:
                count_t[char] +=1
            else:
                count_t[char] = 1
        
        #compare
        return count_s == count_t


        