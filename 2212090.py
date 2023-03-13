# 카드2 : https://www.acmicpc.net/problem/2164
'''
문제 설명 :
1~N 까지의 숫자가 순서대로 나열되어 있다.
가장 앞의 숫자를 버리고, 그 다음 숫자를 가장 마지막으로 보낸다.
위의 과정을 숫자 하나가 남을 때 까지 반복한다.
가장 마지막 숫자를 출력한다.

입력 :
[N]
    - N : 마지막 자연수
'''



if __name__ == '__main__':
    N = int(input())

    if N == 1 :
        result = 1
    elif 1 < N <= 5:
        result = 2
    elif N%2 == 0:
        result = N
    else:
        cardList = [N]
        for i in range(2, N-1, 2):
            cardList.append(i)
        while(len(cardList)==2):
            cardList.pop()
            cardList.append()



    print(result)

