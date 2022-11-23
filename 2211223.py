# 상수 : https://www.acmicpc.net/problem/2908
# 문제 : 3자리 정수 A, B를 입력 받는다. 입력받은 두 정수를 역순으로 바꾸고, 두 값 중 더 큰 값을 출력한다.

# 68ms
import sys

def revereseString(input): # 문자열 input을 역순으로 바꾸는 함수
    result = ''
    for n in reversed(input):
        result += n
    return result

if __name__ == '__main__':
    A, B = sys.stdin.readline().rstrip().split()

    # A, B string값 역순, int형 변화
    A = int(revereseString(A))
    B = int(revereseString(B))

    # 값 비교
    if(A > B):
        print(A)
    else:
        print(B)