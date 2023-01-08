# 정수형태의 변수는 연산이 가능함
변수1 = 10
변수2 = 5

print(변수1 + 변수2)
print(변수1 - 변수2)
print(변수1 * 변수2)
print(변수1 / 변수2)
print(변수1 % 변수2)         #나머지구하기

덧셈 = 변수1 +변수2
뺄셈 = 변수1 - 변수2
곱셈 = 변수1 * 변수2
나눗셈 = 변수1 / 변수2
나머지구하기 = 변수1 %변수2

print (덧셈)
print(뺄셈)
print(곱셈)
print(나눗셈)
print(나머지구하기)\

print()
print('==================')
# 사과의 가격을 구하기
#price, count
#사과의 가격은 OOOO원 입니다.
price = input('사과의 가격:')
print('사과의 가격은',price,'원 입니다.')
# 사과의 갯수는 OO개 입니다
count = input('사과의 갯수:')
print('사과의 갯수는',count,'개 입니다.')
# 총 가격은 OOOOO원 입니다.
print('총 가격은',int(price) * int(count),'입니다.')



