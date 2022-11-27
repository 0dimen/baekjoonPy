# 체스판 다시 칠하기 : https://www.acmicpc.net/problem/1018
'''
문제 설명
M*N짜리 색이 일정하지 않은 체스판을 8*8의 체스판으로 자를 것이다.
정사각형의 색을 가장 적게 칠했다고 했을 때,칠한 정사각형의 개수를 출력한다.
입력
- 첫번째 줄 : [M] [N]
    M == 열 수
    N == 행 수
- 나머지 줄 : M*N의 BW 조합
'''

# value++1은 value+=1과 다르다는 것을 깨달았다.
# list의 값이 잘 참조되지 않는다고 느낄 때는, 주저 말고 print해보자.
# 다음에 시도해 보고 싶은 것 : array 생성 시, numpy를 사용히여 현재 작성한 코드와 장단점을 비교해보고 싶다.
# 104ms

import sys

if __name__ == '__main__':
    # 입력값 받기
    M, N = map(int,sys.stdin.readline().rstrip().split())

    chessBoard = [[] for i in range (M)] # 체스판 M열의 2차원 배열 선언 및 초기화.

    # 체스판 값 받기.
    for colNum in range(M):
        input = sys.stdin.readline().rstrip()
        for value in input:
            chessBoard[colNum].append(value)


    # 체스판 탐색
    minNum = 65 # 칠해야하는 가장 적은 정사각형의 개수. 0 <= minNum <= 64 이므로, 초기 값은 65로 지정.

    for colStart in range(M-7):

        for rowStart in range(N-7):
            bFirstNum = 0  # 0,0이 B로 시작하는 체스판에서, 칠해야하는 정사각형 개수.
            wFirstNum = 0  # 0,0이 W로 시작하는 체스판에서, 칠해야하는 정사각형 개수.

            originColor = 'W' # 원래 체스판에 칠해져야하는 색상 (0,0에 B부터 시작하기 위해 W로 초기화.)

            for colNum in range(colStart, colStart +8):

                # 다음 줄 처음 칠해질 값 초기화
                if originColor == 'B':
                    originColor = 'W'
                else:
                    originColor = 'B'

                chessColumn = chessBoard[colNum]
                # 각 요소가 올바른 값인지 확인
                for value in chessColumn[rowStart: rowStart+8]:
                    # 0,0이 B로 시작하는 체스판
                    if value != originColor:
                        bFirstNum+=1

                    # 다음칸에 와야하는 색상으로 그리고, 0,0이 W로 시작하는 체스판에서 비교하기 위해 값 변경.
                    if originColor == 'B':
                        originColor = 'W'
                    else:
                        originColor = 'B'

                    # 0,0이 W로 시작하는 체스판
                    if value != originColor:
                        wFirstNum+=1

            # 가장 작은 값 갱신
            if bFirstNum < minNum :
                minNum = bFirstNum
            if wFirstNum < minNum :
                minNum = wFirstNum
    # 결과 값 출력
    print(minNum)