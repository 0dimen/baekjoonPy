# 숫자의 개수 : https://www.acmicpc.net/problem/2577
# 문제 설명 : 100 <= N < 1000의 자연수 N 3개를 입력받아 곱한다. 결과값에 0~9까지의 숫자가 각각 몇 번 사용되었는지 출력한다.

''' 시도 1 : 정수가 사용된 횟수 계산. (string 분리)
68 ms
'''


''' 시도 2 : 정수가 사용된 횟수 계산. (int 분리 시도)
각 자리 수를 나머지 연산을 통해 수행해 보았다.

입력값으로 150, 266, 427을 넣었더니 0이 사용된 횟수가 326이 나왔다.
resultInt의 값이 0이 아니면서, 나머지 값이 0인 횟수가 323번이라는 의미이다.

시도 2-1
resultInt의 값 출력을 통해 resultInt가 0이 아닌지 확인해보았다.
그 결과 1.703..e-n과 같은 값이 323회 나왔다.

시도 2-2
이러한 문제가 생긴 이유는 resultInt가 int형으로 저장되지 않았기 때문이다.
나눗셈 연산을 통해 float 형태로 변환 됨을 확인할 수 있었다.
또한 곱셈 연산에서는 자료형이 변하지 않았다.

결과
while문에서의 resultInt의 값을 int형으로 참조하여 값을 확인하여, resultInt가 float 형태가 되는 것을 막았다.

68 ms
'''

# 68ms
# 느낀 점 : 파이썬에서 나눗셈을 하면 값이 float형으로 저장됨을 조심해야겠다.
# 더 알아보고 싶은 점 : 왜 e는 323개까지 표현되는지 확인해보고 싶다.

import sys

if __name__ == '__main__':
    resultList = [0 for i in range(10)] # 출력될 결과값 list. 정수가 사용된 횟수.
    resultInt = 1 # 3자리 수를 곱한 결과값이 저장될 공간. 1,000,000 <= resultInt <= 997,002,999

    for i in range(0, 3): # 3줄 받고 연산하는 반복문
        resultInt *= int(sys.stdin.readline())

    # 시도 1 : 정수가 사용된 횟수 계산. (string 분리)
    '''
    for s in str(resultInt):
        resultList[int(s)] ++1

    for resultN in resultList:
        print(resultN)
    '''


    # 시도 2 : 정수가 사용된 횟수 계산. (int 분리)
    '''
    print("나눗셈 연산 전 resultInt의 타입 : " + str(type(resultInt))) # 시도 2-2 : resultInt 연산 전 후의 타입 변화 확인
    
    while(resultInt != 0):
        resultList[int(resultInt%10)] +=1
        resultInt /= 10
        
        
        print(resultInt) # 시도 2-1 : resultInt값 확인

    print("나눗셈 연산 후 resultInt의 타입 : " + str(type(resultInt))) # 시도 2-2 : resultInt 연산 전 후의 타입 변화 확인

    for resultN in resultList:
        print(resultN)
    '''

    #시도 2 : 정수가 사용된 횟수 계산. (int 분리 결과)
    while (resultInt != 0):
        resultList[int(resultInt % 10)] += 1
        resultInt = int(resultInt/10)

    for resultN in resultList:
        print(resultN)