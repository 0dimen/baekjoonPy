#코칭스터디 9기 1주차 / 이샥

# Q1. num_list 홀수만 출력

num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    for index in reversed(range(len(num_list)-1)): # num_list의 마지막 인덱스 ~ 0번째 인덱스까지 탐색. (뒤에서 부터 탐색하는 이유 : 값이 삭제되어 인덱스 값의 변화가 있기 때문.
        if num_list.__getitem__(index) % 2 == 0: # 짝수이면, 해당 인덱스의 값 삭제.
            num_list.pop(index)
    return num_list


# Q2. sentence 역순 출력
sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    words = list(sentence.split()) # str -> list 형변환
    words = words[::-1] # list element 역순으로 배치
    result = ' '.join(s for s in words) # list -> str 형변환
    return result

# Q3. 힉셍별 평균(with. 리스트와 반복문)

score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    index = 1
    for score1, score2 in score:
        print("%d 번, 평균 : %.1f" %(index, (score1 + score2)/2))
        index++1


# Q4. 딕셔너리 객체 합침.

dict_first = {'사과' : 30, '배' : 15, '감' : 10, '포도' : 10}
dict_second = {'사과' : 5, '감' : 25, '배' : 15, '귤' : 25}

def merge_dict(dict_first, dict_second):
    for key, val in dict_first.items():
        if key in dict_second: # dict_second에 key값이 있으면,
            dict_second[key] += val # 해당 키 값에 값 합침.
        else: # dict_second에 key이 없으면,
            dict_second[key] = val # 아이템 추가.
    print(dict_second)

# Q5. 숫자 제외한 string 리스트 출력

inputs = "cat32dog16cow5"

def find_string(inputs):
    for N in range(10): # 문자열의 숫자 " "으로 치환.
        inputs = inputs.replace(str(N), " ")

    inputs = list(inputs.split()) # 문자열 " "로 나눔.

    print(inputs)

    # inputs = list(inputs)
    # inputs_index = 0
    # for c in inputs:
    #     if 48 <= ord(c) <= 57:
    #         inputs[inputs_index] = ' '
    #     inputs_index += 1
    # result = list(str(inputs).)





if __name__ == '__main__':
    print(get_odd_num(num_list))
    print(reverse_sentence(sentence))
    get_avg(score)
    merge_dict(dict_first, dict_second)
    find_string(inputs)