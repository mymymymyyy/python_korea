# 문자열 = 'hello world, my name is python'
# 정수 = 314
# 실수 = 3.14

# for i in 문자열:
#     print(i, end=' ')

# i = 0
# while i < len(문자열):
#     print(문자열[i], end=' ')
#     i += 1



# 문제 : 문자열에서 알파벳 o 의 갯수를 알려주세요
문자열 = 'hello world, my name is python'
a = 0
for i in 문자열:
    if i == 'o':
        a += 1
print(a)


month = int(input('1~12월중에서 아무 월이나 입력하세요>>'))
for i in range(1,13):
    if i == month:
        continue
    print(i,'월',end=(' '))


월 = int(input('1~12월중에서 아무 월이나 입력하세요>>'))
for i in range(1,월):
    print(i,'월')
print()








#str,int,float,list,tuple,dict,set
# 리스트
# 지하철 3칸, [10,15,12]
subway1 = 10
subway2 = 15
subway3 = 12
print()
# 리스트(list) : 같은 주제의 변수들을 묶음으로 보관 (전체 출력이 가능)
리스트 = [10,15,12,11,22,33,44,55,66]
for i in 리스트:
    print(i, '명')