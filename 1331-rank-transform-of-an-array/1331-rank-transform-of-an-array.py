class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank, rank_dic = 0, {}

        for i in sorted(arr):
            if i not in rank_dic:
                rank += 1
                rank_dic[i] = rank

        return [rank_dic[i] for i in arr]