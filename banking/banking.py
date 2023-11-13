"""
Simple simulation of banking interactions

Objectives:
1. Bank account classes
2. Enable transactions
3. Adaptable limits
4. Some kind of transaction history?

"""
# Ensure there's only uniqe names:
# Some unique identifiers?
# A list containing all names taken for now.


class BankAccount:
    def __init__(
        self,
        name,
        balance,
    ) -> None:
        self.name = name
        self.balance = balance

    def send(self, reciever, amount):
        assert self.balance >= amount, "Not enough money on the bank."

        self.balance -= amount
        reciever.balance += amount


class Bank:
    def __init__(self) -> None:
        self.customers = []

    def open_account(
        self,
        name,
        balance=0,
    ) -> BankAccount:
        assert name not in self.customers, "Name already taken"
        assert (
            balance >= 0
        ), "You cannot open an account with debt. Only non-negative balances possible."
        self.customers.append(name)
        return BankAccount(name, balance)


def main():
    coba = Bank()
    acc1 = coba.open_account("alex", balance=100)
    acc2 = coba.open_account("berta", balance=0)

    print(coba.customers)

    print(acc1.balance)
    print(acc2.balance)

    acc1.send(reciever=acc2, amount=80)

    print(acc1.balance)
    print(acc2.balance)


if __name__ == "__main__":
    main()
