import re 
def solution(new_id):
    # [^0-9a-z-_.] =>  0-9a-z-_. 가 아닌 부분을 기준으로 split한다
    # 따라서  0-9a-z-_.  속하지 않는 문자들 제거 
    id = ''.join(re.split(r"[^0-9a-z-_.]",new_id.lower()))
    id = list(re.sub("[.]{2,}",".",id))
    if id and  id[-1] == '.' :
        id.pop()
    if id and  id[0] == '.':
        id = id[1:]
    if not id :
        id = ['a']
    if len(id) >= 16 : 
        id = id[:15]
        if id[-1] =='.' :
            id.pop()
    id += id[-1] * (3-len(id)) if len(id)<= 2 else ''
    return ''.join(id)
