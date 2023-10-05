class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        elem_amount = {}
        for i in nums:
            elem_amount[i] = elem_amount.get(i,0) + 1
        
        return [i for i in elem_amount if elem_amount[i] >  len(nums)//3]