# 문자열 반복 : https://www.acmicpc.net/problem/2675
# 문제 설명 : 첫번째 줄 : 테스트 케이스 개수 N, 테스트 케이스 줄 : [반복 횟수 R] [반복할 문자열 S].
# 문자열의 character가 반복횟수만큼 반복된다. ex) 3 abc : aaabbbccc
# 64ms
import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for i in range(0, N):
        R, S = sys.stdin.readline().split()
        R = int(R)
        string = ''
        for char in S:
            for j in range(0, R):
                string += char

        print(string)