# 기찍 N : https://www.acmicpc.net/problem/2742
# 문제 설명 : 자연수 N을 입력받고, N ~ 1까지 반대로 값 자연수 출력.

# 배운 점 : range를 역순으로 사용하기 위해서는 reversed를 사용하면 된다.
# 116 ms

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for n in reversed(range(1, N+1)):
        print(n)