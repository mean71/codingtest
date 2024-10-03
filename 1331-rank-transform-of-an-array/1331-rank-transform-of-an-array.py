class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return [{k:v+1 for v,k in enumerate(sorted(set(arr)))}[i] for i in arr]