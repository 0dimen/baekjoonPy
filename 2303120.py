# 리그전 오브 레전드 : https://www.acmicpc.net/problem/23327

'''
문제 설명 : l에서 r 순위의 팀이 게임을 진행할 때, 재미도를 출력한다.

입력 :
    - N : 팀의 수
    - Q : 디비젼 수
    - A : 재미도 (a1, a2, ..., an)
    - l, r : 디비젼 범위

풀이 : 배열의 내적을 통해 구한다.
    1. 디비젼 범위의 재미도를 array 타입으로 arr에 저장.
    2. arr의 전치행렬과 arr 순서로 내적
    3. 내적한 행렬에서 대각 행렬을 제외한 하삼각 행렬의 합을 출력.
        - 하삼각 행렬 추출 이유 : 중복으로 곱해진 값을 제외하기 위함.(ex: a1*a2 == a2*a1)
        - 대각 행렬 제외 이유 : 자기 자신을 곱한 값을 제외하기 위함. (ex : a1*a1, a2*a2)

문제점 : 백준에서는 numpy 라이브러리를 지원하지 않음.
'''

import sys
import numpy as np

if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().rstrip().split())  # 팀의 수, 디비전 개수
    A = np.array([list(map(int, sys.stdin.readline().rstrip().split()))])  # 재미도

    print_result = []

    for i in range(0, Q):
        l, r = map(int, sys.stdin.readline().rstrip().split())

        arr = np.array([A[0, l - 1: r]])

        result = np.tril(np.dot(arr.T, arr)) # arr 내적 및 하삼각 행렬 추출.
        print_result.append(result.sum() - np.diag(result).sum()) # 하삼각 행렬의 합에서 대각 행렬의 값을 제외.

    for s in print_result:
        print(s)