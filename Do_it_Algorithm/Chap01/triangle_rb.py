#오른쪽 아래가 직각인 이등변 삼각형으로 *출력하기

n = int(input("제일 짧은 변을 입력해 주세요"))

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for z in range(i+1):
        print("*",end="")
    print()

#파이썬의 변수와 객체는 다음과 같이 정리할 수 있다.
#변수는 객체를 참조하는 객체에 연결된 이름에 불과하다.
#모든 객체는 메모리를 차지하고, 자료형뿐만 아니라 식별 번호(identity)를 가집니다.