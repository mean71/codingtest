import re

def parsing(file):
    m =  re.match(r"(^\D+)(\d+)", file)
    return m.group(1).lower(), int(m.group(2))

def solution(files):
    return sorted(files, key=parsing)