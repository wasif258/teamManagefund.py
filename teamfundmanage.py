class teamfundmanageapp:
    def __init__(self,fund):
        self.availablefund=fund
    def showavailablefund(self):
        print(f"Available Fund: {self.availablefund}")
    def enterfund(self,enter):
        self.availablefund=self.availablefund+enter
    def spendfund(self,spend):
        self.availablefund=self.availablefund-spend
obj=teamfundmanageapp(5000)
while True:
    uc=input('''
    1 Show available fund
    2 Enter the fund
    3 Spend the fund
    4 Exit the program       
             ''')
    
    if uc=="1":
        obj.showavailablefund()
    elif uc=="2":
        input=input("Who is giving these fund: ")
        enter=int(input("enter the fund which you want to add"))
        obj.enterfund(enter)
        print("Now your fund is :",obj.enterfund)
    elif uc=="3":
        spend=int(input("enter the value which you want to spend"))
        reason=input("why you want to spend the fund")
        obj.spendfund(spend)
        print(f"Now your fund is: {obj.availablefund}")
    elif uc=="4":
        print("Exit the program")
        break
    else:
        print("invalid value")
