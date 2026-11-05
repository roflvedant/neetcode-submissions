class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)

        
        
        while len(stones) > 1:

            val1 = heapq.heappop_max(stones)
            val2 = heapq.heappop_max(stones)

            if val1 > val2:
                heapq.heappush_max(stones, val1 - val2)

        stones.append(0)

        return stones[0]
