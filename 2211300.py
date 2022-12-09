# 영화감독 숌 : https://www.acmicpc.net/problem/1436
'''
문제 설명
'666'과 같이 6이 연속으로 3번 들어가는 숫자 중, N번째로 작은 숫자를 만든다.

입력값 : [N]
    - N : N번째
'''
SUBTITLE = '666'


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



