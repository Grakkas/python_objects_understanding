class Account:

    def __init__(self, bank_agency, account_number, client_name, client_cpf, account_balance):
        self.account_agency = bank_agency
        self.account_number = account_number
        self.account_balance = account_balance
        self.client_name = client_name
        self.client_cpf = client_cpf

    def get_account_agency(self):
        return self.account_agency

    def get_account_number(self):
        return self.account_number

    def get_account_balance(self):
        return self.account_balance

    def get_client_name(self):
        return self.client_name

    def get_client_cpf(self):
        return self.client_cpf

    def transfer_balance_to(self, account, value):
        self.account_balance -= value
        account.account_balance += value
        print("account_balance after transfer:", self.get_account_balance(),
              "transfered value of", value,
              "to:", self.get_client_name(), self.get_client_cpf())
