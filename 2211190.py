# 단어 공부 : https://www.acmicpc.net/problem/1157
# 문제 설명 : 입력값은 대소문자로 이루어진 단어. 단어에서 가장 많이 사용된 문자를 출력. 만약 가장 많이 사용된 문자가 2개 이상인 경우 ? 출력

'''
    시도해 보려고 한 것
    - set()을 통해 구성된 알파벳으로 이루어진 charList를 만드려고 했다.
    이 경우, section 1 부분에서 해당 소문자 위치를 찾기 위해 charList를 여러번 돌아야하기 때문에 숫자 index를 사용하는 것이 적절할 것이라 생각했다.
    그러나 튜플을 사용한다면 큰 연산 없이 할 수 있을 것 같다.
    다음에 다시 시도해 볼 것이다.
'''

import sys

if __name__ == '__main__':
    # 알파벳 개수 26개
    charList = [0 for i in range(26)]
    inputStr = sys.stdin.readline().rstrip()

    # 대문자 : 65 ~ 90, 소문자 : 97 ~ 122
    # section 1 : inputStr에 들어간 알파벳 개수 세기
    for s in inputStr :
        index = ord(s) - 65 # 대문자인 경우

        if index > 25: # 소문자인 경우
            index -= 32
        charList[index] += 1


    maxValue = max(charList)
    maxIndex = charList.index(maxValue)

    # max 값을 가진 알파벳이 여러개인 경우 ? 출력 후 종료
    for value in charList[maxIndex+1: ]:
        if value == maxValue:
            print("?")
            sys.exit(0)

    # 결과 출력
    print(chr(maxIndex+65))