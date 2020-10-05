import Account

cliente1 = Account.Account(3785, 48308312 - 2, "Gabriel Santos da Silva", "123.123.123-87", 300.00)
cliente2 = Account.Account(1971, 1062376 - 6, "Andrea Bruna Castro", "056.051.919-26", 100.00)

object_dictionary = vars(cliente1)
for item in object_dictionary:
    print(item, ':', object_dictionary[item])

print("-----------")

object_dictionary = vars(cliente2)
for item in object_dictionary:
    print(item, ':', object_dictionary[item])
print("-----------")

cliente2.transfer_balance_to(cliente1, 15.00)
print("-----------")


