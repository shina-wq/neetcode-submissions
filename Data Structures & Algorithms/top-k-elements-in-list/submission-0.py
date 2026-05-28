class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort by frequency descending
        sorted_items = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # Extract first k numbers
        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result
        