class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank_dic = {k:v+1 for v,k in enumerate(sorted(set(arr)))}
        return [rank_dic[i] for i in arr]