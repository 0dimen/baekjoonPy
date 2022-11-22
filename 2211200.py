# 평균 : https://www.acmicpc.net/problem/1546
# 문제 설명 : N개의 테스트 점수를 받고, 모든 점수의 평균에 테스트 점수 중 가장 큰 값을 나누고 100을 곱한 값을 출력한다.
'''
시도 1 : 시험 점수를 받을 때, map만 사용을 했을 때, sum이나 max와 같이 배열 전체를 돌아야 하는 함수를 사용하는 경우, 이후에 배열 참조가 되지 않았다.
그래서 scoreList의 타입을 알아보았고, map 객체가 있음을 알았다.
'''

'''
시도 2 : map 타입이 참조 후에 다음 값을 참조하지 못한다는 특징이 포인터와 비슷한 역할을 할 수 있는지 확인하기 위해 시도 2를 사용해보았다.
포인터와 같이 head에 map의 주소값을 넣었다.
이후 scoreList의 값을 모두 참조하고 다시 scoreList에 head 값을 넣고 참조해보았는데, 이미 끝에 다다랐다.
그래서 두 변수의 값을 print 해보았고, 두 값이 모두 같은 주소를 가리킨다는 것을 알았다.
즉, 포인터와 같이 주소값을 활용히여 이전의 값을 참조할 수 없다는 것이었다.
'''

'''
시도 3 : 모든 값을 참조하고나면 map의 메모리는 free가 되는가 확인해보았다.
free가 되지 않았고, 각각의 map은 서로 다른 주소값에 값이 저장되었다. 이는 map 객체가 변수에 저장되었기 때문인 것 같다.
또한 list1에 2번의 map을 실행했을 때, 각자 다른 주소를 갖는다는 점을 보아, 메모리를 재활용하지 않음을 알 수 있다.
'''

'''
221210.py에서 아래를 적용해 봄.
list에 대한 연산이 한 번만 있는 수는 map을 이용하면 효율적일 것 같다. 한 번만 값을 참조하고 사라지면 되기 때문이다. ex) lamda.
'''

# 이전 값을 다시 참조할 수 없는 문제는 list(map())을 사용하면 해결할 수 있다.
# 72ms



import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline()) # 입력할 시험 점수 개수

    # 시도 1
    ''' 시도 1
    
    scoreList = map(int, sys.stdin.readline().rstrip().split()) # 시험점수 받기
    print(type(scoreList))
    '''

    # 시도 2
    ''' 시도 2
    scoreList = map(int, sys.stdin.readline().rstrip().split())  # 시험점수 받기

    head = scoreList
    print("scoreList 주소 1: ")
    print(scoreList)
    print("head 주소 1: " )
    print(head)
    print(sum(scoreList))

    scoreList = head
    print("scoreList 주소 2: " )
    print(scoreList)
    print("head 주소 2: " )
    print(head)
    print(sum(scoreList))
    '''

    # 시도 3
    '''
    list1 = map(int, sys.stdin.readline().rstrip().split())

    print(list1)
    sum(list1)
    print(list1)

    list2 = map(int, sys.stdin.readline().rstrip().split())
    print(list2)

    list1 = map(int, sys.stdin.readline().rstrip().split())
    print(list1)

    '''


    scoreList = list(map(int, sys.stdin.readline().rstrip().split()))  # 시험점수 받기
    M = max(scoreList)

    result = sum(scoreList)*100/M/N
    print(result)