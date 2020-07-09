
#BLL
import math
class Calc:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.res = 0

    def add(self):
        self.res=self.n1+self.n2
    def sub(self):
        if self.n1 > self.n2:
            self.res = self.n1-self.n2
        else:
            self.res = self.n2-self.n1
    def mul(self):
        self.res=self.n1*self.n2
    def div(self):
        self.res=self.n1//self.n2
    def log(self):
        self.res=math.log(self.n1,self.n2)
    def pow(self):
        self.res = math.pow(self.n1,self.n2)
#PL
print("welcome to my Calculator")

ob = Calc()
ob.n1 = int(input("enter a num"))
ob.n2 = int(input("enter second num"))

print("press 1 for add","2 for sub","3 for mul","4 for div","5 for log","6 for pow")

choice = int(input("enter a choice:"))

if choice == 1:
            ob.add()
            print(ob.res)
elif choice == 2:
            ob.sub()
            print(ob.res)
elif choice == 3:
            ob.mul()
            print(ob.res)
elif choice == 4:
            ob.div()
            print(ob.res)
elif choice == 5:
            ob.log()
            print(ob.res)
elif choice == 6:
            ob.pow()
            print(ob.res)
else:
            print("you have entered wrong choice")
