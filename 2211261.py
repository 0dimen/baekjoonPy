# 알파벳 찾기 : https://www.acmicpc.net/problem/10809
# 문제 설명 : 소문자로 이루어진 영어 단어 S를 입력받는다. S에서 a~z 까지의 알파벳이 각각 먼저 등장한 index의 값을, 그리고 포함되지 않은 경우는 -1을 출력한다.

# list를 대괄호 없이 출력하기 위해 print(*list, sep='')을 사용했다.
# 68ms

import sys

if __name__ == '__main__':
    S = sys.stdin.readline().rstrip()
    alphabetList = [-1 for i in range(26)] # 각 알파벳의 index -1로 초기화.

    sIndex = 0 # 영어 단어 S에서 참조하는 index 값
    for s in S:
        index = ord(s) - 97
        if alphabetList[index] == -1:
            alphabetList[index] = sIndex
        sIndex +=1

    print(*alphabetList, sep=' ')