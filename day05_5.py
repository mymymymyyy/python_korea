# return : 함수의 결과를 활용할수 있게해줌
# def 절댓값더하기(a,b):
#     if a < 0:
#         a*= -1
#     if b < 0:
#         b *= -1
#     return a+b # retune 옆에있는 값이 사용한 곳으로 전달
    
# 결과1 = 절댓값더하기(3,7)           # 10
# 결과2 = 절댓값더하기(-4,결과1)         # 7
# print(결과2)
# print(절댓값더하기(-1,-1))

# 문제 1   총합,평균 구하기
# lst = [10,20,30,40,50]


# def 총합(a_lst):
#     d = 0             # 함수 안에서 만든 변수는 함수가 끝나면 사라진다(지역변수)
#     for i in a_lst:
#         print(i)
#         d += i
#     return d
    
   

# sum = 총합(lst)
# avg = sum/len(lst)

# print('총합은',sum)
# print('평균은',avg)

# 문제2 : 입력한 갯수만큼 *을 표시하는 함수
def star(num):
    d = ''
    for i in range(num):
        d += '*'
    return d 
s1 = star(3)
s2 = star(5)
print(s1)
print(s2)