# 단어 정렬 : https://www.acmicpc.net/problem/1181
'''
N개의 소문자로 이루어진 단어를 입력받고, 아래와 같은 조건에 따라 정렬한다.
1. 길이가 짧은 순
2. 길이가 같으면 사전 순으로

입력값
첫번째 줄 : [N]
나머지 줄 : [단어]
'''

'''
시도 1
정렬 순서를 길이순 정렬 -> 사전순 정렬을 했다.
사전순 정렬은 길이순 정렬과 달리 단어의 모든 부분을 기준으로 비교한다.
즉, 단어 하나하나를 분류하는 것이라고 생각할 수 있다.
따라서 이전의 단어 정렬과 상관없이 모든 단어를 재배열 하게 될 수 있다.

반면, 길이순은 길이에 따라 그룹을 짓기 때문에, 이전의 정렬 형태를 유지한 채로 조건에 맞게 배열할 수 있다.

여러가지 조건이 있는 정렬을 할 때에는, 비교하는 세밀도에 따라서 순서를 달리해줄 필요가 있다.
세밀도가 높을 수록 먼저 정렬을 해주어야 다음 조건에서도 이전 정렬을 유지한 채로 비교할 수 있다. 
'''

# 배운 점 : 비교 기준의 세밀도가 높은 순으로 먼저 정렬을 해주면, 각각의 정렬 기준이 유지될 가능성이 높다.
# 100ms


import sys

if __name__ == '__main__':
    inputWord = [] # 입력된 단어 저장될 리스트

    N = int(sys.stdin.readline())

    # 단어 입력
    for i in range(N):
        inputWord.append(sys.stdin.readline().rstrip())

    # 중복값 제거
    inputWord = list(set(inputWord))

    '''
    시도 1
    
    # 길이순 정렬 정렬
    inputWord.sort(key=len)
    
    # 사전순 정렬
    inputWord.sort()
    '''

    # 사전순 정렬
    inputWord.sort()

    # 길이순 정렬 정렬
    inputWord.sort(key=len)

    # 출력
    for s in inputWord:
        print(s)