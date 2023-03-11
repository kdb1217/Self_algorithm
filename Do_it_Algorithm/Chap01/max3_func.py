def find_max(fir, sec, thr):
    max = fir
    if(max < sec):
        max = sec
    if(max < thr):
        max = thr
    print(f'최댓값은 {max}입니다 ')


find_max(1,2,3)
find_max(2,3,3)
find_max(1,3,2)
find_max(2,3,2)
find_max(2,3,1)
find_max(2,2,3)
find_max(3,3,3)
find_max(3,3,2)
find_max(2,1,3)
find_max(3,2,3)
find_max(3,1,2)
find_max(3,2,2)
find_max(3,2,1)
       