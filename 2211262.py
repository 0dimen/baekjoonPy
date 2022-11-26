# X보다 작은 수 : https://www.acmicpc.net/problem/10871
# 문제 설명 : 정수 N개로 이루어진 수열 A와 정수 X를 입력받는다. A에서 X보다 작은 수를 모두 출력한다.

# A도 각 요소에 대해 한 번의 참조만이 필요하여 map을 객체로 사용했다.
# 76ms

import sys

if __name__ == '__main__' :
    N, X = map(int, sys.stdin.readline().rstrip().split()) # 수열의 요소 개수 N , 정수 X 입력 받기.
    A = map(int, sys.stdin.readline().rstrip().split()) # 수열 A 입력 받기.

    resultString = ''
    for a in A:
        if a < X :
            resultString += str(a) + ' '

    print(resultString)