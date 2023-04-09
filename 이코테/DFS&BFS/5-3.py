# 5-3.py 재귀 함수 예제
def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()
recursive_function()

## 오류 메세지가 초대된다. 호출횟수에 제한이 있는데 이 한계를 벗어났기 때문이다.