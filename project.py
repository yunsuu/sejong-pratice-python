
UserTable = []

# 유저 정의
'''
User = {
    'Name' : '',
    'Id' : '',
    'Pass' : '',
    'BuyList' : [],
}
'''

ItemList = [
    'A상품',
    'B상품',
    'C상품',
    'D상품',
    'E상품',
]

def CheckItemList( LoginIdx ):
    print("/****************************/")
    print("     [로그인]%s님 반갑습니다       " % (UserTable[LoginIdx].get('Name')))
    print("/****************************/")
    print('장바구니 목록 :')

    for item in UserTable[LoginIdx].get('BuyList') :
        print(item)

def BuyItem( LoginIdx ):
    print("/****************************/")
    print("     [로그인]%s님 반갑습니다       " % (UserTable[LoginIdx].get('Name')))
    print("/****************************/")

    for idx, item in enumerate(ItemList) :
        print('%d : %s' % (idx, item))

    print('구매 : ', end="")

    buying = int(input())

    if buying >= 0 and buying <= 5:
        UserTable[LoginIdx]['BuyList'].append( ItemList[buying] )
    else :
        print('없는 상품입니다')

def AfterLogin( LoginIdx ):

    while True:
        print("/****************************/")
        print("     [로그인]%s님 반갑습니다       " % (UserTable[LoginIdx].get('Name')))
        print("/****************************/")
        print("1. 장바구니 확인")
        print("2. 상품 장바구니에 넣기")
        print("3. 돌아가기")

        selection = int(input())

        if selection == 1 :
            CheckItemList(LoginIdx)
        elif selection == 2 :
            BuyItem(LoginIdx)
        else:
            return

def UserRegister():
    print("이름 : ", end="")
    NAME = input()
    print("아이디 : ", end="")
    ID = input()
    print("패스워드 : ", end="")
    PASS = input()
    print("패스워드 확인 : ", end="")
    PASS_CONFIRM = input()

    if PASS_CONFIRM != PASS:
        print("패스워드가 다릅니다")
        return


    newUser = {
        'Name': '',
        'Id': '',
        'Pass': '',
        'BuyList': [],
    }


    newUser['Name'] = NAME
    newUser['Id'] = ID
    newUser['Pass'] = PASS

    UserTable.append(newUser)


def CheckUserList():
    for user in UserTable:
        print("[ 이름 : %s, 아이디 : %s, 비밀번호 : %s ]" % (user['Name'], user['Id'], user['Pass']))

def UserLogIn():

    print("아이디 : ", end="")
    ID = input()
    print("패스워드 : ", end="")
    PASS = input()

    LogIn_idx = -1

    for idx, user in enumerate(UserTable):
        if user.get('Id') == ID and user.get('Pass') == PASS :
            LogIn_idx = idx

    if LogIn_idx == -1 :
        print('아이디와 비밀번호가 맞지 않습니다')
    else :
        AfterLogin(LogIn_idx)


def ProgramStart():
    while True :
        print("/****************************/")
        print("          쇼핑몰 프로그램         ")
        print("/****************************/")
        print("1. 회원 가입")
        print("2. 회원 리스트 확인")
        print("3. 회원 로그인")
        print("커맨드 : ", end="")
        selection = int(input())

        if selection == 1:
            UserRegister()
        elif selection == 2:
            CheckUserList()
        elif selection == 3:
            UserLogIn()


def ProgramOutLine():
    print("안녕하세요 파이썬 첫 프로젝트입니다")
    print("프로젝트 개요 : 쇼핑몰 프로그램 ")
    print("프로젝트 기능 :")
    print("1. 회원 가입")
    print("2. 회원 로그인")
    print("3. 회원 로그인 후 상품 구매")
    print("4. 회원 로그인 후 장바구니 확인")

ProgramOutLine()
ProgramStart()
week-1.py
week-1.py 표시 중입니다.
