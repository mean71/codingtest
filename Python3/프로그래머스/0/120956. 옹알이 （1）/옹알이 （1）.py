def solution(babbling):
    baby = 'aya', 'ye', 'woo', 'ma'
    count = 0
    for ongR in babbling:
        for say in baby:
            ongR = ongR.replace(say, '0', 1)
        if ongR.isdigit():
            count += 1
    return count