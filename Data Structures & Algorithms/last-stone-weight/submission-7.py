class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:


            val1 = heapq.heappop_max(stones)
            val2 = heapq.heappop_max(stones)

            heapq.heappush_max(stones, val1 - val2) if val1 > val2 else None
            heapq.heappush_max(stones, val2 - val1) if val2 > val1 else None

        stones.append(0)
        return stones[0]