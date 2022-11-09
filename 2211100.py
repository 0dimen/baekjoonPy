# 단어의 개수 : https://www.acmicpc.net/problem/1152
# 문제 설명 : 문장을 이루는 단어의 개수(중복 포함)을 출력.
# list의 요소 개수를 알기 위해서는 len() 함수를 사용한다. len([리스트])
# 80ms

import sys

if __name__ == '__main__':
    inputStr = list(sys.stdin.readline().split())
    print(len(inputStr))