# 아스키 코드 : https://www.acmicpc.net/problem/11654
# 문자 하나를 입력 받으면 아스키 코드값
# 실험 1 : ord에는 1글자 짜리 string 타입이 들어가야 함.
# 실험 2 : rstrip()을 사용하면 개행 문자를 제외한 하나의 문자를 받을 수 있다.
# 아래의 경우 input()과 rstrip은 같은 시간이 걸린다.

if __name__ == '__main__':
    try:
        print(ord(input()))

        # 실험 1 : print( type(input()))
        # 실험 2 : print(ord(sys.stdin.readline().rstrip()))
    except:
        exit()
