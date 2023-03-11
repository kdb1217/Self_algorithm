# 세 정수를 입력받아 최댓값 구하기

print("세 정수를 입력 받습니다.")

first_num = int(input("첫 번째 정수를 입력해주세요 :"))
second_num = int(input("두 번쨰 정수를 입력해주세요 :"))
third_num = int(input("세 번쨰 정수를 입력해주세요"))

max = first_num
if ( max < second_num):
    max = second_num


if ( max < third_num):
    max = third_num

print(f'최댓값은 {max}입니다.')  
