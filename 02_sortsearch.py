#%% https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mn = 0
        mx = len(nums)-1
        while mx >= mn :
            mid = (mn+mx)//2
            print(mid)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                mn = mid+1
            else:
                mx = mid - 1
        return -1
    

#%%