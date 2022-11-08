# 숫자의 합 : https://www.acmicpc.net/problem/11720
# 문제 설명 : 첫번째 줄 - 입력될 문자의 개수 N. 두번째 줄 - 숫자로 이루어진 문자열.
# 두번째 줄의 숫자를 모두 더하여 출력.
# 실험 1 : 문제의 오점을 발견. N의 값과 상관없이 입력된 모든 자리 수 더해도 상관 없음.

import sys

if __name__ == '__main__' :
    try:

        N = int(sys.stdin.readline())
        inputStr = sys.stdin.readline().rstrip()
        sum = 0

        for index in range(0, N):
            sum += int(inputStr[index])

        # 실험 1 : for num in inputStr:
        #     sum += int(num)
        print(sum)
    except:
        exit()

