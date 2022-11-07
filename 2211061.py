# A + B - 4 : https://www.acmicpc.net/problem/10951
# 꺠달은 점 : readline()이 input()보다 속도가 빠르다. 정상 종료를 위해 try, except 구문이 필요함.
import sys

if __name__ == '__main__':
    while True:
        try:
            A,B = map(int, sys.stdin.readline().split())
            print(A + B)
        except:
            break