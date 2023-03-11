
def find_mid(fir,sec,thr):
    if fir >= sec:
        if sec >= thr:
            return sec
        elif fir <= thr:
            return fir
        else:
            return thr
    elif fir > thr:
        return fir
    elif sec > thr:
        return thr
    else:
        return sec

print(' 세 정수의 중앙값을 구합니다.')
fir = int(input('첫 번쨰 정수의 값을 입력하세요.:'))
sec = int(input('두 번째 정수의 값을 입력하세요.:'))
thr = int(input('세 번쨰 정수의 값을 입력하세요.:'))

print(f'중앙값은 {find_mid(fir,sec,thr)} 입니다')

#다른 표현방식
def med3(a,b,c):
    if (b>= a and c <= a) or (b <= a and c>= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c