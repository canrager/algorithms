"""
Simple simulation of banking interactions

Objective: Banking with 
1. Opening bank account
2. Deposit
3. Pay
4. Open transfer
5. Accept transfer
6. Transfers not accepted in a given time frame are cancelled
"""

from time import time
from typing import Union, Dict
import functools


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
        self.customers = dict()
        self.transfers: Dict[
            str, Dict[Union[str, str, float, float, bool]]
        ] = dict()  # transfer_id: sender, receiver, amount, time, is_accepted
        self.next_transfer_id: int = 0
        self.max_duration_pending_transfer: int = 100

    def open_account(
        self,
        name,
        balance=0,
    ) -> BankAccount:
        assert name not in self.customers, "Name already taken"
        assert (
            balance >= 0
        ), "You cannot open an account with debt. Only non-negative balances possible."
        self.customers[name] = BankAccount(name, balance)
        return self.customers[name]

    def check_pending_transfers(self):
        # TODO
        # print("Check pending transfers not implemented yet.")
        pass

    def checker(func):
        @functools.wraps(func)
        def wrapper_decorator(*args, **kwargs):
            args[0].check_pending_transfers()  # args[0] is self object
            return func(*args, **kwargs)

        return wrapper_decorator

    @checker
    def deposit(
        self,
        name: str,
        amount: float,
    ) -> bool:
        assert name in self.customers, "Unknown name."
        assert amount > 0, "Can only deposit positive amounts."

        self.customers[name].balance += amount
        return True

    @checker
    def pay(
        self,
        name: str,
        amount: float,
    ) -> bool:
        assert name in self.customers, "Unknown name."
        assert amount > 0, "Can only pay out positive amounts."

        self.customers[name].balance -= amount
        return True

    @checker
    def open_transfer(
        self,
        sender: str,
        receiver: str,
        amount: str,
    ) -> bool:
        assert amount > 0, "Can only transfer positive amounts."
        assert sender in self.customers, "Unknown sender."
        assert receiver in self.customers, "Unknown receiver."
        assert (
            self.customers[sender].balance >= amount,
            "The sender balance is too low to open this transaction",
        )

        self.transfers[self.next_transfer_id] = dict(
            sender=sender,
            receiver=receiver,
            amount=amount,
            time=time(),
            is_accepted=False,
        )
        self.next_transfer_id += 1
        self.pay(sender, amount)
        return True

    @checker
    def accept_transfer(
        self,
        id,
    ) -> bool:
        ts = time()
        assert id in self.transfers, "Unknown transfer ID."
        assert (
            ts - self.transfers[id]["time"] < self.max_duration_pending_transfer
        ), "The transfer timed out. Please open a new transfer."
        assert (
            self.transfers[id]["is_accepted"] is not True
        ), "The transfer has been accepted already."

        self.transfers[id]["is_accepted"] = True
        self.deposit(self.transfers[id]["receiver"], self.transfers[id]["amount"])
        return True


class TestBanking:
    def __init__(self) -> None:
        self.bank = Bank()
        self.eps = 1e-10
        self.run()

    def run(self):
        self.open_accounts()
        print(
            "alex' balance after opening account", self.bank.customers["alex"].balance
        )
        self.deposit()
        print("alex' balance after deposit", self.bank.customers["alex"].balance)
        self.payout()
        print("alex' balance after payout", self.bank.customers["alex"].balance)
        self.open_transfer()
        print(
            "alex' balance after opening transfer", self.bank.customers["alex"].balance
        )
        self.accept_transfer()
        print(
            "alex' balance after accepting transfer",
            self.bank.customers["alex"].balance,
        )
        self.check_pending_transfers()
        print("\nAll tests passed!")

    def open_accounts(self):
        self.bank.open_account("alex", balance=100)
        self.bank.open_account("berta", balance=0)

        assert "alex" in self.bank.customers
        assert self.bank.customers["alex"].balance == 100, "Opening account failed."
        return True

    def deposit(self):
        amt = 50
        old = self.bank.customers["alex"].balance
        self.bank.deposit("alex", amt)

        assert (
            old + amt - self.bank.customers["alex"].balance
        ) < self.eps, "Deposit failed."
        return True

    def payout(self):
        amt = 50
        old = self.bank.customers["alex"].balance
        self.bank.pay("alex", amt)

        assert (
            old - amt - self.bank.customers["alex"].balance
        ) < self.eps, "Payout failed."
        return True

    def open_transfer(self):
        sender = "alex"
        receiver = "berta"
        amt = 80
        self.bank.open_transfer(sender, receiver, amt)

        # TODO: add tests
        print("List of transfers: ", self.bank.transfers)
        print("berta: ", self.bank.customers["berta"].balance)
        return True

    def accept_transfer(self):
        id = 0
        self.bank.accept_transfer(id)

        # TODO: add tests
        print("List of transfers: ", self.bank.transfers)
        print("berta: ", self.bank.customers["berta"].balance)
        return True

    def check_pending_transfers(self):
        # TODO: add tests
        pass


if __name__ == "__main__":
    TestBanking()
