# 직사각형에서 탈출 : https://www.acmicpc.net/problem/1085
'''
문제 설명
왼쪽 아래 꼭짓점이 (0,0)이고, 오른쪽 위 꼭짓점이 (w,h)인 직사각형의 경계선에서 좌표 (x,y)의 최소 거리를 출력

첫 번째줄 입력값 : [x] [y] [w] [h]
'''
import sys

'''
시도 1
각 점에서의 거리를 구한다.
'''
# 76ms

if __name__ == '__main__':
    # 입력값 받기
    x, y, w, h = map(int, sys.stdin.readline().rstrip().split())


    # 가장 작은 변 구하기. minDistance에
    minDistance = 0 # 최소 거리가 저장될 공간.

    if x < w-x :
        minDistance = x
    else:
        minDistance = w-x
    if minDistance > y:
        minDistance = y
    if minDistance > h-y:
        minDistance = h-y

    print(minDistance)