#  20세 이상은 성인
# 14세 이상은 청소년
#14세 미만은 어린이

나이 = int(input('당신의 나이는?-->'))
if 나이 >= 20:
    print('성인')
if 나이 < 20 and 나이 >= 14:
    print('청소년')
if 나이 <14 and 나이 >= 1:
    print('어린이')
if 나이 < 1:
    print('^_^')


if 나이 >= 23:
    print('회사원')
elif 나이 >= 20:
    print('대학교')
elif 나이 >= 17:
    print('고등학교')
elif 나이 >= 14:
    print('중학교')
elif 나이 >= 8:
    print('초등학교')
elif 나이 >= 6:
    print('유치원')
elif 나이 >= 1:
    print('어린이집')
elif 나이 < 1:
    print('@_@')