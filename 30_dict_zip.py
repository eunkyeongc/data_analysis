# dict
# --> 딕셔너리 자료형

# 딕셔너리 만들 때
d = {'a':1, 'b':2, 'c':3}
print(d)        #{'a': 1, 'b': 2, 'c': 3}
print(type(d))  # <class 'dict'>

d2 = [('a', 1),('b', 2),('c', 3)]
print(d2)        #[('a', 1), ('b', 2), ('c', 3)]
print(type(d2))  #  <class 'list'>

#딕셔너리로 형 변환
d2 = dict(d2)
print(d2)
print(type(d2)) # <class 'dict'>

# 또 다른 딕셔너리 생성 방법
d3 = dict(a=1, b=2, c=3)
print(d3)
print(type(d3)) # <class 'dict'>

print('='*70)
#===============================================
# zip() 함수
# --> 키는 키끼리, 값은  값끼리 묶는다. (딕셔너리)
# --> 같은 인덱스 번호낄 묶는다. (리스트, 튜플)
d4 = dict(zip(['a','b','c'], [1, 2, 3]))
print(d4)       # {'a': 1, 'b': 2, 'c': 3}
print(type(d4)) # <class 'dict'>

li = ['a','b','c']          #list
tu = (1, 2, 3)              #tuple
result_zip = zip(li, tu)
print(result_zip)
print(type(result_zip))     #<class 'zip'>

for i in result_zip:
    print(i)             # 튜플 형태로 읽어드림
# ('a', 1)
# ('b', 2)
# ('c', 3)

print(list(zip(li, tu))) # 리스트로 형 변환 --> [('a', 1), ('b', 2), ('c', 3)]
print(type(list(zip(li, tu)))) #<class 'list'>

li1 = [1, 2]
li2 = ['a','b','c','d']
li3 = ['가','나','다']
print(list(zip(li1,li2,li3)))  #[(1, 'a', '가'), (2, 'b', '나')]

for i in zip(li1,li2,li3):
    print(i)
# (1, 'a', '가')
# (2, 'b', '나')

print('='*70)
# ===============================================
# 튜플은 쪼갤수 있다 (각각의 변수로 담는다) --> 튜플 언패킹
# 튜플을 묶는다 --> 튜플 패킹
for z1, z2, z3 in zip(li1,li2,li3):
    print(f'z1:{z1}, z2:{z2}, z3:{z3}')
# z1:1, z2:a, z3:가
# z1:2, z2:b, z3:나

print('='*70)
# ===============================================
# enumerate()  index number 동반
for i in enumerate(li2):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for index, value in enumerate(li2):
    print(f'index:{index}, value: {value}')
# index:0, value: a
# index:1, value: b
# index:2, value: c
# index:3, value: d

print('='*70)
# ===============================================
# 딕셔너리와 for
print(d4)           # {'a': 1, 'b': 2, 'c': 3}

for i in d4:
    print(i)  # 키(key) 출력
# a
# b
# c

for i in d4:
    print(d4[i])  # 값(value) 출력
# 1
# 2
# 3

print('='*70)
# ===============================================
# .keys() --> 키(key)만
print(d4)               # {'a': 1, 'b': 2, 'c': 3}

for i in d4.keys():
    print(i)
# a
# b
# c
print(d4.keys())        # dict_keys(['a', 'b', 'c']) --> type형이 dict_keys이므로 list형으로 형 변환이 필요하다.
print(list(d4.keys()))  # ['a', 'b', 'c']

print('='*70)
# ===============================================
# .values() --> 값(value)만
for i in d4.values():
    print(i)
# 1
# 2
# 3

print(d4.values())          # dict_values([1, 2, 3]) --> type형이 dict_values이므로 list형으로 형 변환이 필요하다.
print(list(d4.values()))    # [1, 2, 3]

print('='*70)
# ===============================================
# .items() -->  키와 값을 같이 묶어서 보여준다.

print(d4)               # {'a': 1, 'b': 2, 'c': 3}

for i in d4.items():
    print(i)
# ('a', 1)
# ('b', 2)
# ('c', 3)

for k, v in d4.items():
    print(f'k:{k}, v:{v}')
# k:a, v:1
# k:b, v:2
# k:c, v:3

print('='*70)
# ===============================================
# 튜플을 묶는다 --> 튜플 패킹 --> def func(*args):
# *args --> 가변 매개변수
def func(*args):
    total = 0
    for i in args:
        total += i 
    return total

result1 = func(1, 2)
result2 = func(1, 2, 3)
result3 = func(1, 3, 5, 2)
result4 = func(10, 2, 5, 1, 8, 99)

print(result1, result2,result3, result4)

print('='*70)
# ===============================================
def func2(name, *args):
    total = 0
    for i in args:
        total += i
    print(f'{name}이(가) 더한 값은 {total}입니다.')

func2('pubao', 1, 2, 3)
func2('chunsici', 10, 20)