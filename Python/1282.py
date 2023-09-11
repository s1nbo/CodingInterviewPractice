class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        groups = {}
        for i, j in enumerate(groupSizes):
            if j not in groups:
                groups[j] = []
            groups[j].append(i)

            if len(groups[j]) == j:
                ans.append(groups[j])
                groups[j] = []

        
        return ans