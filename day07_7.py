class 학생:
    이름 = ''
    번호 = 0
    키 = 0
    def __init__(self,이름,번호,키):
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키
    def 학생정보보기(self):
        print('이름',self.이름,'번호',self.번호,'키',self.키)
    def 학생정보입력(self,이름,번호,키):
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키        





# 다른사람들이 학생 클래스를 사용
# 클래스 업데이트 요청

# 상속 : 사람이 복붙을 하면 사람이 고쳐야하기 때문에, 컴퓨터가 북붙을해서 컴퓨터가 고치게 한다 (클ㄹ래스 복붙)
class 학생2(학생):
    pass
    # 학생 클래스의 변수와 메서드를 복붙해줌
    def __del__(self):
        print('프로그램 종료')

class 학생3(학생):
    # 학생 클래스가 복붙됨
    print(f'==이름: {self.이름}, 번호: {self.번호},키:{self.키},몸무게:{self.몸무게}==')
a = 학생2('철수',4,177,80)
a.학생정보보기()