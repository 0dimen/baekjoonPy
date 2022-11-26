# 나머지 : https://www.acmicpc.net/problem/3052
# 문제 설명 : 자연수를 10개 입력받고, 이를 42로 나누어 나머지를 구한다. 구해진 나머지들의 서로 다른 값을 개수를 출력한다.

# 중복되는 원소 삭제하기 위해 set 함수를 사용했다.
# 68ms

import sys

if __name__ == '__main__' :
    remainderList = [] # 나머지 값이 저장될 배열
    for i in range (0, 10): # 값 10번 입력 반복.
        remainderList.append(int(sys.stdin.readline().rstrip())%42) # 나머지 값 배열에 append.
    print(len(set(remainderList)))