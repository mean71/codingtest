def solution(data, ext, val_ext, sort_by):
    val = {"code":0, "date":1, "maximum":2, "remain":3}
    return sorted(filter(lambda x:x[val[ext]] < val_ext, data), key=lambda x:x[val[sort_by]])