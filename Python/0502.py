import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        maxProfit = [] # only Projects we can afford
        minCapital = [(c,p)for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for _ in range(k):
            
            while minCapital and minCapital[0][0] <= w:
               _, p = heapq.heappop(minCapital)
               heapq.heappush(maxProfit, -1 * p)

            if not maxProfit:
                break
                
            w += -1 * heapq.heappop(maxProfit)
        
        return w


"""
Input: int, int, array of ints, array of ints
Output: int

We use a max heap to store the projects we can afford (maxProfit)
We use a min heap to store the projects we cannot afford (minCapital)

We iterate k times (number of projects we are allowed to do)
    
    We iterate through the minCapital heap and add all the projects we can afford to the maxProfit heap
    A project is affordable if the current capital is greater than or equal to the project's capital
    We add the project to the maxProfit heap by multiplying the profit by -1 and pushing it to the heap
    we do this because we want to use a max heap but we want to store the projects with the highest profit at the top of the heap

    If the maxProfit heap is empty, we break out of the loop because we cannot afford any more projects

    We add the project with the highest profit to the current capital
    We multiply the profit by -1 because we multiplied it by -1 when we added it to the maxProfit heap

Return the current capital

Time Complexity: O(k * logn) where n is the number of projects and k is the number of projects we are allowed to do
Space Complexity: O(n)

"""
