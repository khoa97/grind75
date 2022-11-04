class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, n in enumerate(nums):
            complement = target - n
            if complement in m:
                return [idx,m[complement]]
            else:
                m[n] = idx
        return 
        