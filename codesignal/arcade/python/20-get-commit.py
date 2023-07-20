import re

def solution(commit):
    return re.sub('[!+?0]', '', commit)
