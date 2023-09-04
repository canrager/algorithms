#%% https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}
        for char in magazine:
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] = 1

        for char in ransomNote:
            if char not in char_count:
                return False
            else:
                char_count[char]-=1
            if char_count[char] < 0:
                return False
        return True
    

#%% https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Idea: hash_function: sorted
        anagrams = {}
        for st in strs:
            strsort = "".join(sorted(st))
            if strsort in anagrams:
                anagrams[strsort].append(st)
            else:
                anagrams[strsort] = [st]
        return list(anagrams.values())