# seq_serach()함수를 사용하여 특정 인덱스 검색하기

from sserach_while import  seq_serach

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS','AAC','FLAC']

print(f'{t}에서 5.6의 인덱스는 {seq_serach(t,5.6)}입니다.')
print(f'{s}에서 "n"의 인덱스는 {seq_serach(s, "n")}입니다.')
print(f'{a}에서 "DTS"의 인덱스는 {seq_serach(a, "DTS")}입니다.')