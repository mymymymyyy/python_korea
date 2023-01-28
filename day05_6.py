# 외부 함수를 사용하는 법 : import
# 모듈 : 부품

# import 모듈명
# import 모듈명 as 별명
# from 모듈명 import 함수명

import matplotlib.pyplot as plt
# 모듈중에 font_manager, rc 만 가져옴
from matplotlib import font_manager, rc

font = font_manager.FontProperties(fname='gulim.ttc').get_name()

lst = [10,22,33,44,50,60,77,80,99,100]
plt.title('분포도')        # 제목
plt.xlabel('점수')         # x축 제목
plt.ylabel('갯수')         # y축 제목
plt.hist(lst)             # 막대그래프 그려주어
plt.show()                # 보여줘