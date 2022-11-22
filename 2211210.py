# 검증수 : https://www.acmicpc.net/problem/2475
# 문제 설명 : 5자리 양의 숫자를 받고, 각 숫자를 제곱한 값들의 합을 10으로 나눈 나머지를 출력한다.
''' 시도 1 -> 결과
2211200에서 배운 것 처럼, list의 일회성 연산에 효율성을 높이기 위해 map을 활용해 보았다.
map은 lamda 식을 사용할 수 있을 뿐 아니라, 따로 list를 선언해주지 않아도 된다.
따라서 list 메모리를 차지 하지 않아 효율적일 것 같다.
'''

# 다음에 시도해볼 부분 : 여러 값의 일회성 연산을 위해 각각의 값을 list 객체와 map 객체에 저장했을 때, 두 객체 사이의 메모리, 시간 차이를 알아보고 싶다.
# 68ms

import sys

if __name__ == '__main__':
    # 시도 1
    '''
    inputNum =  map(lambda x: int(x)**2 ,sys.stdin.readline().rstrip().split())
    print(sum(inputNum)%10)
    '''

    print(sum(map(lambda x: int(x)**2 , sys.stdin.readline().rstrip().split()))%10)