#  파일읽고쓰기

def 파일쓰기(filepath):
# 파일 만들고 쓰기(txt)
    f = open(filepath,'w',encoding='UTF-8')
    f.write('안녕하세요 반갑습니다 감사합니다ㅎ\n')               # \n : 엔터키, 한줄 바꾸기
    f.close()

# 파일 읽기(txt)
def 파일읽기(filepath):
    f = open(filepath,'r',encoding='UTF-8')                    
    lines = f.readlines()        #전체를 읽음
    print(lines)
    for line in lines:
        print(line,end='')
    f.close

# 파일 추가쓰기(txt)
def 파일추가(filepath):
    f = open(filepath, 'a+',encoding='UTF-8')
    f.write('다시만나요')
    f.close()