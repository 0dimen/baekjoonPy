# 수 찾기 : https://www.acmicpc.net/problem/1920
'''
문제 설명

N개의 정수 A[]를 받고, M개의 정수 X[]를 입력 받아 해당 값이 주어진 정수 A에 존재하는지 확인한다.

입력
첫번째 줄 : [N]
    - N : 입력 받을 정수(A[n])의 수
두번째 줄 : [A[1]] [A[2]] ... [A[N]]
    - A[n] : 주어진 정수
세번째 줄 : [M]
    - M : 존재하는지 확인할 정수의 수
네번째 줄 : [X[1]] [X[2]] ... [X[M]]
     - X[n] : 존재하는지 확인할 정수
'''

'''
시도 1
if X in A

해당 알고리즘을 사용할 경우, 최악의 경우 A 전체를 다 돌아야 한다.
그 경우 O(n)의 시간이 걸려 시간 초과가 나타나게 된다.
O(n)보다 빠른 알고리즘을 사용해야 한다.
'''

'''
시도 2

scale이 1인 searching을 사용해보았다.
O(n/2)는 O(n)과 비슷한 성능을 보이기 때문에 시간 초과가 나왔다.
그래서 이보다 효율적인 binary search를 사용해보았다.
'''

# 696ms

import sys


def binarySearch(A, x):
    maxIndex = len(A) - 1  # 최대 인덱스
    index = (maxIndex + 1) // 2  # 참조하는 인덱스
    scale = index // 2  # 움직이는 단위

    # 초기 조건.
    if A[0] == x or A[1] == x:
        return 1
    if A[maxIndex] == x or A[maxIndex - 1] == x:
        return 1

    while 1 < index < maxIndex - 1 : # 양 끝 인덱스에서는 -1, maxIndex+1의 값을 참조할 수 없기 때문에,
        a = A[index]
        if a == x:
            return 1
        elif a < x:
            # A[index] < x < A[index + 1]인 경우, x는 존재하지 않음.
            if A[index + 1] > x:
                return 0
            else:
                index += scale

        elif a > x:
            # A[index - 1] < x < A[index]인 경우, x는 존재하지 않음.
            if A[index - 1] < x:
                return 0
            else:
                index -= scale

        # scale 1/2로 줄임.
        scale //= 2
        # A[1], A[maxIndex-1]에는 도달하기 위함.
        if scale == 0:
            scale = 1


'''
시도 2

def searching(A, x):
    size = len(A)
    index = size//2

    if A[0] == x:
        return 1
    if A[size-1] == x:
        return 1

    while 1 <= index < size - 1:
        if A[index] == x:
            return 1
        elif A[index] < x:
            if A[index +1] > x:
                print("없음")
                return 0
            else:
                index += 1
        elif A[index] > x:
            if A[index-1] < x:
                print("없음")
                return 0
            else:
                index -= 1

    return 0
'''

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    A = list(map(int, sys.stdin.readline().rstrip().split()))

    M = int(sys.stdin.readline())

    X = map(int, sys.stdin.readline().rstrip().split())

    '''
    시도 1
    
    for x in X:
    if x in A:
        print(1)
    else:
        print(0)
    '''

    # A 리스트 정렬
    A.sort()

    for x in X:
        print(binarySearch(A, x))
