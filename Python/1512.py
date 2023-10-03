class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        num_idx = {}
        ans = 0

        for idx, num in enumerate(nums):
            if num in num_idx:
                num_idx[num].append(idx)
            else:
                num_idx[num] = [idx]
        
        for value in num_idx.values():
            ans += sum(range(len(value)))

        return ans


sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))
