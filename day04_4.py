# 문자열을 저장하는 리스트를 만드셈         #추가할 값을 입력   #수정할 값을 입력?       #삭제할 값 입력      #전체조회       # 프로그램 종료
lst = []
num = 0
수정 = 0
수정할값 = 0

# 사용자에게 입력을 받아 리스트를 구성
# 1: 추가하기, 2: 수정하기, 3: 삭제하기, 4: 전체보기
while True:
    num = int(input('1: 추가, 2: 수정, 3: 삭제, 4: 조회, 5: 종료>>' ))
    if num == 1:          
        lst.append(input('추가할 값을 입력>>'))
        print('추가한 값',lst)

    elif num == 2:
            수정 = int(input('수정할 위치를 입력하시요>>'))
            수정할값 = (input('무엇으로 바꾸겠 습니까?'))
            lst[수정-1] = 수정할값 

    elif num == 3:
        lst.remove(input('삭재할 값을 입력>>'))
        print('남은 숫자',lst)

    elif num == 4:
        for i in lst:
            print(i)

       
    elif num == 5:
        print('프로그램 종료')
        print('프로그램 종료')
        print('프로그램 종료')
        print('프로그램 종료')
        print('프로그램 종료')
        print('프로그램 종료')
        print('프로그램 종료')
        print('프로그램 종료')
        print('프로그램 종료')


        break           
    else:
        print('없는 번호입니다')
        print('없는 번호입니다')
        print('없는 번호입니다')