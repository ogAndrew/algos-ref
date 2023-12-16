# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(idx, partial, result):
            if len(nums) == idx:
                subset = partial.copy()
                result.append(subset)
                return
            
            # exclude
            helper(idx + 1, partial, result)

            # include
            partial.append(nums[idx])
            helper(idx + 1, partial, result)
            partial.pop()
        
        res = []
        helper(0, [], res)
        return res