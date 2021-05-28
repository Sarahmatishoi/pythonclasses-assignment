class Account:
    def __init__(self,accountName,owner,ATMcard):
        self.accountName=accountName
        self.owner=owner=owner
        self.ATMcard=ATMcard
    def deposit(self):
        return f"{self.owner} deposited money into {self.accountName} using {self.ATMcard}."
    def withdraw(self):
        return f"{self.owner} withraw cash from {self.accountName} using {self.ATMcard}"
    def checkBalance(self):
        return f"{self.owner} checked balance in {self.accountName} using {self.ATMcard}"



        