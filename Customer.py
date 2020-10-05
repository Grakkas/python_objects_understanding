import ConnectorDB as ConnectorDB


def create_customer():
    name = input("Digite o nome do cliente: ")
    cpf = input("Digite o cpf do cliente: ")
    dob = input("Digite a data de nascimento do cliente: ")
    phone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente (não obrigatorio): ")
    occupation = input("Digite o cargo do cliente (não obrigatorio): ")
    city = input("Digite a cidade do cliente:")
    address = input("Digite o endereco do cliente: ")
    adnumber = input("Digite o numero do cliente: ")
    adcomplement = input("Digite um complemento para o endereco: ")
    zipcode = input("Digite o cep do cliente :")
    ConnectorDB.execute_script(
        f"INSERT into customer (fullname, cpf, dob, phone, email, occupation, city, address, adnumber, adcomplement, "
        f"zipcode) VALUES ('{name}', '{cpf}', '{dob}', '{phone}', '{email}', '{occupation}', '{city}', '{address}', "
        f"'{adnumber}', '{adcomplement}', '{zipcode}')")


def read_all_customer():
    for i in ConnectorDB.read_script("SELECT * from customer"):
        print(i)


def find_customer_by_cpf(cpf):
    for i in ConnectorDB.read_script(f"SELECT * from customer where cpf = '{cpf}'"):
        print(i)


def delete_customer_by_cpf(cpf):
    ConnectorDB.execute_script(f"delete from customer where cpf = '{cpf}'")
