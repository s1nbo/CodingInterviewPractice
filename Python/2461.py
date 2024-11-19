from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        included = set()
        l = 0
        cur = 0

        for r in range(len(nums)):
            if nums[r] not in included: 
                cur += nums[r]
                included.add(nums[r])

                if r - l + 1 == k: # r - l + 1 = len(included)
                    ans = max(ans, cur)
                
                    cur -= nums[l]
                    included.remove(nums[l])
                    l += 1
            else:
                while nums[r] != nums[l]:
                    cur -= nums[l]
                    included.remove(nums[l])
                    l += 1
                
                l += 1

        return ans


# Topic: Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(k)

'''
We track all the elements in the current window using a set.
We track the sum of our current window using cur.

We loop through the list.
Add the most recent element to cur and included if it is not already in included.
If the length is k we, save the maximum  answer and remove the last element from the window.

If the element is already in the window, we remove elements from the window until we reach the duplicate element.
We do not remove the duplicate element itself and simply increment l by 1.
'''