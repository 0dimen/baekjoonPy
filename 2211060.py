# 별 찍기 : https://www.acmicpc.net/problem/2438

def writeStar(N):
    for lineNum in range (N):
        output = ""
        for repeatNum in range (0, lineNum+1):
            output += "*"
        print(output)

if __name__ == '__main__':
    writeStar(int(input()))