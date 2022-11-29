# 팰린드롬수 : acmicpc.net/problem/1259
'''
문제 설명
테칼코마니 숫자를 입력받으면 yes를, 그렇지 않다면 no를 출력한다.

입력
나머지 줄 : [N]
    - N : 0으로 시작하지 않는 자연수
종료 조건 : '0' 입력
'''

# 해결 방안 : 자연수 N을 string으로 받는다. N의 길이를 반으로 나누어 앞 부분은 순차적으로, 뒷 부분은 역순으로 비교한다.
# 68ms

import sys

if __name__ == '__main__':
    while(True):
        # 입력값 받기
        N = sys.stdin.readline().rstrip()

        # 종료 조건 확인
        if N == '0':
            exit()

        nMaxIndex = len(N) - 1 # N이 갖는 최대 인덱스
        flag = True # 펠린드롬수인지 확인하기 위한 변수. True : 펠린드롬수. False : 일반적인 수.

        # 펠린드롬수 확인
        for indexR in range(0, int(nMaxIndex/2)+1):
            if N[indexR] != N[nMaxIndex-indexR]:
                flag = False
                break


        if flag == True:
            print("yes")
        else:
            print("no")


