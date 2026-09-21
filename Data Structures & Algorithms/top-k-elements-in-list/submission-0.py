from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = Counter(nums)
        # Sort the (number, count) pairs by count descending
        sorted_pairs = sorted(n.items(), key=lambda item: item[1], reverse=True)
        
        # Take the number from each of the top k pairs
        return [pair[0] for pair in sorted_pairs[:k]]