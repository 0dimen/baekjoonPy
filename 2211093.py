# OX퀴즈 : https://www.acmicpc.net/problem/8958
# 문제 설명 : 첫번째 입력값은 테스트 케이스 개수 N. 이후 입력값은 OX 퀴즈 결과 S. 연속된 O의 개수가 해당 문제의 점수가 된다.
# 72ms

import sys

if __name__ == '__main__':
    # get test case number
    N = int(sys.stdin.readline().rstrip())

    # get OX Quiz result without score
    for i in range(0, N):
        S = sys.stdin.readline().rstrip()
        scorePer = 1 # score per quiz
        scoreSum = 0 # sum of score
        for OX in S:
            if OX == 'O':
                scoreSum += scorePer
                scorePer += 1
            else:
                scorePer = 1

        print(scoreSum)




