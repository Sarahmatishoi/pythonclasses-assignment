class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction=100
        self.loan=0
        self.loan_limit=20000
    def deposit(self,amount):
       
        if amount <= 0:
            return "please deposit a valid amount"

        else:
            self.balance += amount
            return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"

    def withdraw(self,withdraw_amount):
        total=withdraw_amount+self.transaction
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
            return f"Hello {self.name} you have received {amount} and you will pay {self.loan}"


    