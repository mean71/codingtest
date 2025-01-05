def solution(key, targets):
    press = {c: min(i for k in key if (i := k.find(c) + 1)) for c in set(''.join(key))}
    return [sum(x) if all((x:=[press.get(c, 0) for c in target])) else -1for target in targets]