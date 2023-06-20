class Solution:
    def getAverages(self, nums, k: int):
        if k == 0:
            return nums
        
        length = len(nums)
        avgs = [-1]*length
        size = 2*k+1
        

        if length < size:
            return avgs
        
        current_sum = 0

        for j in range(0, size):
            current_sum += nums[j]
        avgs[k] = current_sum

        for i in range(k+1, length-k):
            avgs[i] = avgs[i-1] - nums[i-k-1] + nums[i+k]
        
        for i in range(k, length-k):
            avgs[i] //= size

        return avgs


"""
Input: List of Integers, Integer
Output: List of Integers

We initialize a list of -1 with the same length as nums.
We initialize a variable, (window)size, to 2*k+1.

We check if the length of nums is less than size, if so, the input is invalid, so we return avgs.

We loop through the first size elements of nums.
We add the current element to current_sum

We set the kth element of avgs to current_sum.

We loop through the rest of nums.
We remove the last element from current_sum and add the next element.
We set the ith element of avgs to current_sum.

We loop through the middle elements of avgs.
We divide the ith element of avgs by size.

We return avgs.

Time Complexity: O(n)
Space Complexity: O(n)
"""