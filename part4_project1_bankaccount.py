from datetime import datetime, timezone

def increment_transaction_id(transaction_id=0):
    while True:
        transaction_id += 1

        yield transaction_id


class Account:

    _monthly_interest_rate = 0.025
    transaction_id = increment_transaction_id()



    def __init__(self, account_no, first_name, last_name, time_offset, starting_balance=0):
        self._transaction_history = []
        self._account_no = account_no
        self.first_name = first_name
        self.last_name = last_name
        self._time_offset = time_offset
        self._balance = starting_balance




    @property
    def balance(self):
        return self._balance

    @property
    def account_no(self):
        return self._account_no

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def transaction_history(self):
        return self._transaction_history

    @transaction_history.setter
    def transaction_history(self, new_transaction):
        self._transaction_history.append(new_transaction)


    @classmethod
    def get_interest_rate(cls):
        return cls._monthly_interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        cls._monthly_interest_rate = value


    def produce_confirmation_no(self, transaction_type, transaction_id):
        return f"{transaction_type}-{self.account_no}-{transaction_id}"

    def deposit(self, amount):
        self._balance = self._balance + amount
        print(f"{amount} deposited, new balance is: {self.balance}")

        confirm_no = self.produce_confirmation_no("D", next(Account.transaction_id))
        print(f"Confirmation no: {confirm_no}\n")
        self.transaction_history = confirm_no

    def withdraw(self, amount):
        if (self._balance - amount) >= 0:
            self._balance = self._balance - amount
            print(f"{amount} withdrawn, remaining balance is: {self.balance}")


            confirm_no = self.produce_confirmation_no("W", next(Account.transaction_id))
            print(f"Confirmation no: {confirm_no}\n")
            self.transaction_history = confirm_no

        else:
            print(f"Insufficient funds. Max withdrawal is: {self.balance}")


            confirm_no = self.produce_confirmation_no("X", next(Account.transaction_id))
            print(f"Confirmation no: {confirm_no}\n")
            self.transaction_history = confirm_no

    def calculate_interest(self):
        interest_accrued = self._balance * Account.get_interest_rate()
        self._balance = self._balance + interest_accrued
        print(f"Monthly interest accrued: {interest_accrued:.2f}\nNew balance is: {self.balance:.2f}")


        confirm_no = self.produce_confirmation_no("I", next(Account.transaction_id))
        print(f"Confirmation no: {confirm_no}\n")
        self.transaction_history = confirm_no


new = Account(12124, "Tayfur","Eken", -5, 10)
print(new.__dict__)
print(new.balance)

new.deposit(122)
new.deposit(121)
new.deposit(122)

new.withdraw(352222)
new.set_interest_rate(101)

print("new.get_interest_rate()", new.get_interest_rate())

new.calculate_interest()

new2 = Account(53233, "Qrsh", "Qqqq", -66)

new2.deposit(100)
new2.deposit(1111)

print("new2.get_interest_rate()", new2.get_interest_rate())

print(new.transaction_history, new2.transaction_history)

# possible to overwrite
new._first_name = "aaaa"
print(new.full_name)
# possible
