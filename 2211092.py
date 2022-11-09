# 음계 : https://www.acmicpc.net/problem/2920
# 문제 설명 : 1~8사이의 자연수 값을 랜덤으로 한 번씩 입력받는다.
# 입력된 값이 차례로 입력된 경우, ascending, 반대인 경우, descending, 이외는 mixed
# 68ms

import sys

if __name__ == '__main__' :
    input = sys.stdin.readline().rstrip()

    if(input == "1 2 3 4 5 6 7 8"):
        print("ascending")
    elif(input == "8 7 6 5 4 3 2 1"):
        print("descending")
    else:
        print("mixed")