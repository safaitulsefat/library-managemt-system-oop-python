class User:
    def __init__(self,name,roll,password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow = []
        self.return_book = []

class Libray:
    def __init__(self,booklist) -> None:
        self.booklist = booklist
    def borrow_books(self,bookName,user):
        for book in self.booklist:
            if book == bookName:
                if book in user.borrow:
                    print("ager book ferot daw")
                    return
                elif self.booklist[book]==0:
                    print("in this book not avaiable")
                    return
                self.booklist[book]-=1
                user.borrow.append(bookName)
                print("you have borrowed this book")
                return
        print("book not avaiable in this librry")
    
    def return_books(self,bookName,user):
        for book in self.booklist:
            if book == bookName:
                if book in user.borrow:
                    self.booklist[book] +=1
                    user.borrow.remove(bookName)
                    user.return_book.append(bookName)
                    print("thanks for returned book")
                    return
                else:
                    print("onner book nibo na")
                    return
        print("kar book ferot disso")
    
    def check_available(self):
        for book in self.booklist:
            print(book, self.booklist[book])
    
    def donate_book(self,bookName,amount):
        for book in self.booklist:
            if book == bookName:
                self.booklist[book] += amount
                print("thanks for book donate")
                return
            
        self.booklist[bookName]=amount
        print("thanks for donating book")




libray = Libray({"english":2,"bangla":3})
allUser = []
currntuser = None

while True:
    if currntuser == None:
        print("Not logged in\n Please login or create account L/C: ")
        option = input()
        if option == "L":
            roll = int(input("enter roll: "))
            password = input("enter password: ")
            match = False
            for user in allUser:
                if user.roll == roll and user.password == password:
                    currntuser = user
                    match = True
            if match == False:
                print("user not found")
        else:
            name = input("enter your name")
            roll = int(input("enter your roll"))
            found = False
            for user in allUser:
                if user.roll == roll:
                    found = True
            if found:
                print("vai koibar account kolab")
                continue
            password = input("enter password here")
            user = User(name,roll,password)
            currntuser =user
            allUser.append(currntuser)

    else:
        print("----------------")
        print("1.brrow books")
        print("2.return book")
        print("3.borrow list check")
        print("4.returned book check")
        print("5. check book avaiabilty")
        print("6.Dnoate book")
        print("7.logout")
        x = int(input("enter option: "))
        if x==1:
             n = input("enter book name ")
             libray.borrow_books(n,currntuser)
        elif x==2:
            n=input("enter book name ")
            libray.return_books(n,currntuser)
        elif x==3:
            print(currntuser.borrow)
        elif x==4:
             print(currntuser.return_book)
        elif x==5:
            libray.check_available()
        
        elif x==6:
            n= input("enter book name")
            y = int(input("enter book amount: "))
            libray.donate_book(n,y)
        
        elif x==7:
            currntuser = None






        