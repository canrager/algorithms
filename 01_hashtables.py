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
    

#%% https://app.codesignal.com/interview-practice/question/njfXsvjRthFKmMwLC/description

def solution(nums, k):
    # create ht keyed by nums elements
    ht = dict()
    for i, n in enumerate(nums):
        if n not in ht:
            ht[n] = [i]
        # if a key exists already, determine the difference between the current index and all values in that entry. If not, append to values
        else:
            for idx in ht[n]:
                # if an absolute difference is less than or equal to k, return True
                if i - idx <= k:
                    return True
            ht[n].append(i)
    # return False otherwise
    return False


#%% https://app.codesignal.com/interview-practice/question/3PcnSKuRkqzp8F6BN/description

def iterate(strings, patterns):
    ht = dict()
    for i, s in enumerate(strings):
        if s not in ht:
            ht[s] = patterns[i]
        else:
            if patterns[i] != ht[s]:
                return True
    return False

def solution(strings, patterns):
    if iterate(strings, patterns):
        return False
    if iterate(patterns, strings):
        return False
    return True

#%% https://app.codesignal.com/interview-practice/question/xrFgR63cw7Nch4vXo/description

def solution(dishes):
    # order in hashtable with ingredients as keys
    ht = dict()
    for dish in dishes:
        for i in range(1, len(dish)):
            if dish[i] not in ht:
                ht[dish[i]] = [dish[0]]
            else:
                ht[dish[i]].append(dish[0])
    
    # construct sorted list
    res = []
    for ing in sorted(list(ht.keys())):
        if len(ht[ing]) > 1:
            ht[ing].sort()
            res += [[ing] + ht[ing]]
    return res

