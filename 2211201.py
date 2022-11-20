# 별 찍기 - 2 : https://www.acmicpc.net/problem/2439
# 문제 설명 : 줄 수 N을 받고, n번째 줄에는 n개의 "*"을 출력한다. 단, 오른쪽으로 정렬시켜서 출력한다.
'''
총 3개의 for문을 사용하여 출력할 string을 구성했다.

첫 번째 for문 : 몇 번째 줄인지 값 참조용.
두 번째 for문 : 오른족 정렬을 위한 공백 추가용.
세 번째 for문 : 별 추가용.
'''
# 72ms

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for n in range(1, N+1):
        printStr = "" # 각 줄에 출력될 string

        # 오른쪽 정렬을 위한 공백 추가
        for spaceN in range(0, N-n):
            printStr += " "
        # 별 추가
        for starN in range(0,n):
            printStr +="*"

        print(printStr)