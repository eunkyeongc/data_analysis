# 타입 어노테이션(annotation)
# --> 파이썬은 자료형 선언없이 변수나 함수를 자유롭게 사용할 수 있다는 특징이 있다.
# --> 자료형을 파악하기 어려운 경우가 종종 발생하게 된다.
# --> 파이썬 3.5버전 이상에서 사용가능
# --> 강제성이 없는 자료형에 관한 힌트를 알려준다. --> 꼭 지킬 필요가 없다.!
# --> 코드 자체에도 영향을 미치지 않는다. --> 에러도 나지 않는다.

# =============================================================================
# ex) 일반적으로 지금까지 공부한 파이썬 변수 선언 방법
num = 1 # 정수 값을 담은 변수
li = [1, 2, 3, 4] 
dic = {'name':'pubio', 'age': 5} 
print(num, li, dic, sep='\n')
print(type(num), type(li), type(dic), sep='\n')

print('='*50)
# =============================================================================
# ex) 어노테이션을 넣은 변수 선언 방법
# 변수이름: 자료형 = 값
num: int = 0     # 변수이름은 num, 자료형은 int
li: list = [1,2,3,4]
d: dict = {'name':'pubio', 'age': 5}
print(num, li, dic, sep='\n')
print(type(num), type(li), type(dic), sep='\n')
print()

# ==============================================================================
#  ex) 일반적인 함수 정의 방법
def add(a, b):
    return a + b

result = add(1, 2)
print(result)
print(type(result))
print()

result2 = add(1.5, 2.5)
print(result2)
print(type(result2))
print()

result3 = add('Hi! ', 'World')
print(result3)
print(type(result3))
print()

result4 = add([1,2], [3,4])
print(result4)
print(type(result4))


print('='*50)
# ==============================================================================
# ex) 어노테이션 적용한 함수 정의
# def 함수명(매개변수명: 자료형) -> 반환형의 자료형:
# 함수본체
def sub(a: int, b: int) -> int: 
    return a - b

result =sub(10,2)
print(result)
print(type(result))
print()

result2 =sub(10, 2.5) 
print(result2)
print(type(result2))
print()

result3 =sub('이주일과 심순애', '이주일')
print(result3)
print(type(result3))
