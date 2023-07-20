import re

def solution(s):
    s = re.sub('%%','{%}',s)
    s = re.sub('%[dfgexXocbs]','{}',s)
    return re.sub('{%}','%',s)