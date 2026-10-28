class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1
        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )
        answer = []
        for i,j in sorted_items:
            if k>0:
                answer.append(i)
                k -=1
        return answer