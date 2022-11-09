# 최댓값 : https://www.acmicpc.net/problem/2562
# max는 자연수이기 때문에, 가장 작은 초깃값은 0으로 지정한다.
# 72ms

import sys

if __name__ == '__main__':
    max = 0
    maxIndex = 0
    for index in range(1, 10):
        input = int(sys.stdin.readline())
        if(max <input):
            max = input
            maxIndex = index

    print(max)
    print (maxIndex)