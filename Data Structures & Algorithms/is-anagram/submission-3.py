class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= s.lower()
        t = t.lower()
        letters = [0] * 26
        letters2 = [0] * 26
        if len(s) != len(t):
            return False
        for x in range(len(s)):
            letters[ord('a')-ord(s[x])] += 1 
            letters2[ord('a')-ord(t[x])] += 1     
        print(letters, letters2)
        return letters == letters2