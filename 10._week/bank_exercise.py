class Customer:
    def __init__(asd, *args):
        if len(args) == 2:
            self.name = args[0]
            self.cpr = args[1]
        elif len(args) == 1:
            self.name = args[0]
        else:
            raise NotImplemented

    def printCustomer(self):
        print("{} has this CPR: {}.".format(self.name, self.cpr))


class Account:
    def __init__(self, *args):
        if len(args) == 2:
            self.customer = args[0]
            self.accountNo = str(self.customer.cpr) + "0000"
            self.availableMoney = args[1]
        elif len(args) == 1:
            self.customer = args[0]
            self.accountNo = str(self.customer.cpr) + "0000"
            self.availableMoney = 0
        else:
            raise NotImplemented

    def printAccount(self):
        print("Account {} has {} $ that can be used by customer {} ".format(
            self.accountNo, self.availableMoney, self.customer.name))


class Bank:
    accounts = {}

    def __init__(self, *args):
        for arg in args:
            Bank.accounts[arg.customer] = arg

    def printBank(self):
        for key in self.accounts:
            print("{} owns this account {} which has {} available dollars".format(
                key.name, Bank.accounts[key].accountNo, Bank.accounts[key].availableMoney))


c1 = Customer("John", 12345678)
c2 = Customer("Jane", 87654321)

bank = Bank(Account(c1, 10000), Account(c2))

bank.printBank()
