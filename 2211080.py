# A + B - 5 : https://www.acmicpc.net/problem/10952
import sys

if __name__ == '__main__':
    while True:
        A, B = map(int, sys.stdin.readline().split())
        if(A == 0 and B == 0):
            break
        print(A + B)