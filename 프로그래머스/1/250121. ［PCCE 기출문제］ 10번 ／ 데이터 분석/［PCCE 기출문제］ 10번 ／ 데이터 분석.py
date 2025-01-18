def solution(data, ext, val_ext, sort_by):
    val = {"code":0, "date":1, "maximum":2, "remain":3}
    ext = val[ext]
    sort_by = val[sort_by]
    return sorted(filter(lambda x:x[ext] < val_ext, data), key=lambda x:x[sort_by])