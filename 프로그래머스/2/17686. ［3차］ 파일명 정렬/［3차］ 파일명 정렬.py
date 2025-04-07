import re

def solution(files):
    return sorted(files,
                  key=lambda file: (
                      (m := re.search(r"(?P<name>\D+)(?P<num>\d+)(?P<rest>.*)", file)).group("name").lower(),
                      int(m.group("num"))
                      )
                  )