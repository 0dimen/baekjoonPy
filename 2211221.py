# N 찍기 : https://www.acmicpc.net/problem/2741
# 문제 설명 : 자연수 N을 입력받고, 1~N까지의 자연수를 출력한다.

# 116ms

import sys

if __name__ == '__main__' :
    N = int(sys.stdin.readline())

    for n in range(1, N+1):
        print(n)