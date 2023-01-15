import matplotlib.pyplot as plt          #그래프 그려주는 라이브러리(부속품)

# 문제
시험점수 = [71,85,77,81,99,23,55,100,0]
_80점이상 = []

# 80점 이상 사람들의 수 구하셈

for i in 시험점수:
    if i >= 80:
        _80점이상.append(i)
갯수 = len(_80점이상)
print(갯수,'명')

# 데이터 시각화
plt.hist(시험점수)          # 막대그래프
plt.xlabel('score')
plt.show()           # 그려줘
plt.ylabel('person')
plt.title('test')