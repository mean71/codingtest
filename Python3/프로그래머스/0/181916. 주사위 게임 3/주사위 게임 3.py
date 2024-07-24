def solution(a, b, c, d):
    from collections import Counter
    dice = [a, b, c, d]
    count = Counter(dice)
    if len(count) == 1:
        return 1111 * dice[0]
    if len(count) == 4:
        return min(dice)
    if len(count) == 3:
        for value, cnt in count.items():
            if cnt == 2:
                pair_value = value
                remaining_values = [x for x in dice if x != pair_value]
                return remaining_values[0] * remaining_values[1]
    if len(count) == 2:
        pair_values = [value for value, cnt in count.items() if cnt == 2]
        if len(pair_values) == 2:
            p, q = pair_values
            return (p + q) * abs(p - q)
    if len(count) == 2 and any(cnt == 3 for cnt in count.values()):
        three_of_a_kind_value = [value for value, cnt in count.items() if cnt == 3][0]
        single_value = [value for value, cnt in count.items() if cnt == 1][0]
        return (10 * three_of_a_kind_value + single_value) ** 2
    return 0
