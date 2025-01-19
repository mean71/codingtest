import re

def solution(new_id):
    new_id = "".join(filter(lambda c:re.match(r"[a-z0-9-_.]", c), new_id.lower()) ).strip(".").split(".")
    new_id = ".".join(s for s in new_id if s)[:15].strip(".")
    return new_id + new_id[-1:]*(3-len(new_id)) or "aaa"