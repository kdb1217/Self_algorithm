# import sys
# cardnum =[]
# count = int(sys.stdin.readline())
# SearchNum = []
# Searchmax = 0
#
# for a in range(count):
#     cardnum.append(int(sys.stdin.readline()))
#
# for value in cardnum:
#      if value not in SearchNum:
#         SearchNum.append(value)
# max = 0
#
# for i in range(len(SearchNum)):
#     data = cardnum.count(SearchNum[i])
#     if  Searchmax < (data):
#             Searchmax = data
#             max = SearchNum[i]
#     if (Searchmax == data):
#         if (max > SearchNum[i]):
#             max = SearchNum[i]
#             Searchmax = data
# print(max)
# 시간초과
import sys

count = int(sys.stdin.readline())
inputList = []
numCount = 0
input_nums = {}
maxNum = 0
tmp = 0
for i in range(count):
    a = int(sys.stdin.readline())
    if input_nums.get(a):
        input_nums[a] += 1
    else:
        inputList.append(a)
        input_nums[a] = 1

inputList.sort()
for i in range(len(inputList)):
    if numCount < input_nums.get(inputList[i]):
        maxNum = inputList[i]
        numCount = input_nums.get(inputList[i])

print(maxNum)
