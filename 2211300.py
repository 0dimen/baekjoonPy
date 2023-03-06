# 영화감독 숌 : https://www.acmicpc.net/problem/1436
'''
문제 설명
'666'과 같이 6이 연속으로 3번 들어가는 숫자 중, N번째로 작은 숫자를 만든다.

입력값 : [N]
    - N : N번째
'''

'''
시도 1
 '666'이 포함된 타이틀이 생성되는 규칙을 10000번째까지 찾는다.
10000번째 까지는 총 4개의 규칙이 존재했다.

 찾은 규칙을 적용했으나, 정상적으로 실행되지 않았다.
규칙을 잘못 적용했거나, 규칙을 잘못 찾은 것이 문제인 것 같다.

 이 방식은 inputNum의 값이 커질수록 타이틀을 찾기위해서는 알고리즘의 갱신이 필요하다는 점이 문제이다.
 그러나 속도가 작성된 알고리즘보다 빠를 것이다.
 
'''

'''
시도 2

'''




if __name__ == '__main__':
    inputNum = int(input()) # 찾는 타이틀 번째수
    SUBTITLE = '666' # 포함 되어야 하는 문자열

    n = 666 # 가장 최근에 찾은 타이틀
    titleNum = 1 # 현재까지 찾은 타이틀 숫자 번째수

    while titleNum != inputNum: # 찾는 타이틀 순서인지 확인.
        n += 1
        if str(n).__contains__(SUBTITLE): # n에 '666'이 포함되어 있는지 확인
            titleNum += 1

    print(n) # 찾은 타이틀 출력


    ''' 시도 2
    while True:
        if str(n).__contains__(SUBTITLE):
            titleNum += 1
            print(titleNum)

            if titleNum == inputNum: # 찾는 타이틀인지 확인
                print(n)
                break
        n += 1
    '''

''' 시도 1
def loop1_1(n):
    share = n // 19
    remainder = n % 19

    if share == 0 and remainder < 10:
        result = SUBTITLE + str(remainder)
    elif remainder < 10:
        result = str(share) + SUBTITLE + str(remainder)
    else:
        result = str(share * 10 - 3 + remainder) + SUBTITLE  # (share*10 - 10 + 7 + remainder)

    return result

def loop1_2(n):
    share = n // 19
    remainder = n % 19

    result = ''

    if remainder == 0:
        result = str(share * 10 + 5) + SUBTITLE
    elif remainder < 10:
        result = str(share * 10 - 3 + remainder) + SUBTITLE  # (share*10 - 10 + 7 + remainder)
    else:
        result = SUBTITLE + str(remainder)
    return result

def loop2(n):
    share = n // 19
    if share >= 10 :
        share = 0
    remainder = n % 19


    if remainder == 0 or remainder >= 9:
        result= str(67 + share*10) + SUBTITLE + str(remainder)
    elif remainder < 9:
        result =  str(67 + share*10 + remainder) + SUBTITLE

    return result

def loop3(n):
    share = n // 271
    remainder = n % 271

    if share == 0 and remainder < 100:
        result = SUBTITLE + str(remainder)
    elif remainder < 100 :
        result = str(share) + SUBTITLE + str(remainder)
    elif remainder >= 100 :
        result = str(share*(10**5)+ int(loop2(remainder - 100)))

    return result



if __name__ == '__main__':
    N = int(input()) - 1
    result = ''
    if N == 0 :
        result = SUBTITLE
    elif N < 6 :
        result = str(N) + SUBTITLE
    elif N < 120 :
        result = loop1_1(N-6)
    elif N < 1794 :
        result = loop3(N-120)

    elif N <= 4597 :
        result = loop3(N - 1680)

    print(result)

'''

