# 랜선 자르기 : https://www.acmicpc.net/problem/1654

'''
문제 :
주어진 랜선을 필요한 개수만큼 최대한 길고, 같은 길이로 자른다.


입력 :
 - K : 랜선의 개수
 - N : 필요한 랜선의 개수

풀이 :
 - maxLen 구하기
    1. pivot 설정. 0 < maxLen <= (sum(input_lines)//N) 임을 통해 적절한 pivot을 설정한다.
    2. binary search를 통해 maxLen 구하기.
'''
import sys

def numOfLines(lines, cutLen):
    numLine = 0
    for l in lines:
        numLine += l//cutLen

    return numLine


if __name__ == '__main__':
    K, N = map(int, sys.stdin.readline().rstrip().split())
    input_lines = []
    for k in range(0, K):
        input_lines.append(int(input()))

    maxLen = sum(input_lines)//N # 가장 긴 랜선 길이
    move_scale = maxLen//2

    while maxLen > 0:
        n = numOfLines(input_lines, maxLen)
        if n >= N:
            n = numOfLines(input_lines, maxLen+1)
            if n < N: # 최대 길이를 찾았을 때
                break
            else: # 최대 길이에 도달하지 않았을 때
                maxLen += move_scale
        else:
            maxLen -= move_scale

        move_scale //= 2
        if move_scale < 1:
            move_scale = 1

    print(maxLen)
