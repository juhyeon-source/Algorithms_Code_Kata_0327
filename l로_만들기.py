def solution(myString):
    answer = ''
    front_l = 'abcdefghijk'
    for i in myString:
        if i in front_l:
            answer += 'l'
        else:
            answer += i
    return answer