# 핵심은 정규식을 이용해서  head + number + tail 로 분리하기 !! 
import re 
def solution(files):
    splits = sorted([re.split(r"([0-9]+)", s) for s in files],key = lambda x:(x[0].lower(),int(x[1])))
    return [''.join(x) for x in splits ]
    
