from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        direction = [[1,3], [0,2,4],[1,5], [0, 4], [1,3,5], [2,4]]
        target = '123450'
        visited = set()
        q = deque()
        start = ''.join(str(x) for row in board for x in row)
        
        visited.add(start)
        q.append(start)
        ans = 0
        while q:
            depth_size = len(q)
            for _ in range(depth_size):
                cur = q.popleft()

                if cur == target:
                    return ans
                
                pos = cur.find('0')
                for new in direction[pos]:
                    new_state = list(cur)
                    new_state[pos], new_state[new] = new_state[new], new_state[pos]
                    new_str = ''.join(new_state)
                    if new_str not in visited:
                        visited.add(new_str)
                        q.append(new_str)

            ans += 1
            

        return -1

# Time Complexity: O(1) since the board is always 2x3
# Space Complexity: O(1) since the board is always 2x3
# Topics: BFS