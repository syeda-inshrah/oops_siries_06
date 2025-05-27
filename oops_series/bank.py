
class Bank:
    bank_name = "askari bank"


    @classmethod   
    def change_bank_name(cls , name):
        cls.bank_name = name
    
b1 = Bank()

print(f"{b1.bank_name}")
b1.change_bank_name("national bank")
print(b1.bank_name)