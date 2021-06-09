from datetime import datetime
class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transactionfee=100
        self.loan=0
        self.loan_limit=20000
        self.transaction=[]
    def deposit(self,amount):
       
        if amount <= 0:
            return "please deposit a valid amount"

        else:
            self.balance += amount
            transaction={"amount":amount,"balance":self.balance,"narration":"you deposited","time":datetime.now()}
            self.transaction.append(transaction)
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"

    def withdraw(self,withdraw_amount):
        total=withdraw_amount+self.transactionfee
        transaction={"amount":withdraw_amount,"balance":self.balance,"narration":"you withdrew","time":datetime.now()}
        self.balance-=total
        self.transaction.append(transaction)
        
        if withdraw_amount <=0:
            return "please deposit valid amount"
        elif total >self.balance: 
            return " invalid balance " 
        else:
            self.balance -=total
            return f"Hello {self.name} you have sufficient balance you can now borrow {withdraw_amount} and your balance is {self.balance}"
    def borrow(self,amount):
        if amount>=self.loan_limit:
            return f"you will not be able to borrow the money"
        elif amount<0:
            return f"you can't borrow"
        elif self.loan>0:
            return f"sorry {self.name} you have an already existing loan "
        else:
            loan_fee=amount*0.05
            self.loan=loan_fee+amount
            transaction={"amount":amount,"balance":self.balance,"narration":"you borrow","time":datetime.now()}
            self.transaction.append(transaction)
            return f"Hello {self.name} you have received {amount} and you will pay {self.loan}"
    def repay(self,amount):
        different=amount-self.loan

        transaction={"amount":amount,"balance":self.balance,"narration":"you repaid","time":datetime.now()}
        self.transaction.append(transaction)
        if amount>self.loan:
            return f"{self.name} you have paid {amount} and your current balance {different}"
        elif amount>=self.loan:
            return f"{self.name} your have repaid your loan and you can now borrow"
        else:

            different=self.loan-amount
            return f"{self.name} you have paid {amount} and your existing loan is {different}"


    def statement(self):
        for transaction in self.transaction:
            amount=transaction["amount"]
            narration=["narration"]
            balance=["balance"]
            time=transaction["time"]
            date=time.strftime("%D")
            print(f"{date}....{narration}....{amount}.... balance {balance}")

    