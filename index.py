from datetime import datetime
class Usuario:
    lista_usuarios = [] #atributo da class
    def __init__(self, nome="", data_nascimento="", cpf=0, endereco=""): #atributos do objeto
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
    @classmethod
    def idade(cls):
        dia, mes, ano = map(int, cls.data_nascimento.split('/'))
        nascimento = datetime(ano, mes, dia)
        data_atual = datetime.now()
        idade = data_atual.year - nascimento.year - ((data_atual.month, data_atual.day) < (nascimento.month, nascimento.day))
        if cls.maior_idade(idade):
            return f"Idade: {idade}."
        else:
            return f"Idade: {idade}. Para criar a conta é necessário ter acima de 18 anos"
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
    def adicao_usuario(self):
        for usuario in Usuario.lista_usuarios:
            if usuario["cpf"] == self.cpf:
                print("Erro: Este CPF já foi cadastrado.")
                return
        Usuario.lista_usuarios.append({
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "cpf": self.cpf,
            "endereco": self.endereco
        })
        print(f"Usuário {self.nome} adicionado com sucesso!")

    
class Corrente:
    numero_conta_sequencial = 1
    AGENCIA = "0001"
    def __init__(self, usuario):
        self.numero_conta = Corrente.numero_conta_sequencial
        Corrente.numero_conta_sequencial +=1
        self.usuario = usuario
    def informacoes_conta(self):
        return{
            "agencia": Corrente.AGENCIA,
            "numero_conta": self.numero_conta,
            "usuario": self.usuario.nome

        }

class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.transacoes = []

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saque não realizado, valor maior que o saldo")
            return False
        else:
            self.saldo -= valor
            self.transacoes.append({"Tipo":"Saque", "valor": valor})
            print(f"Saque realizado. Seu saldo atual é de R$ {self.saldo}")
            return True

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        self.transacoes.append({"Tipo": "Deposito", "valor": valor})
        print(f"Depósito realizado. Seu saldo atual é de R$ {self.saldo}")
    def extrato(self):
        print("\n--- Extrato Bancário ---") 
        if not self.transacoes:
            print("Nenhuma transação foi realizada.")
        else:
            for transacao in self.transacoes:
                print(f"{transacao["Tipo"]}: R$ {transacao["valor"]}")
        print(f"Saldo atual: R$ {self.saldo}")
        print("--------------------------\n")


def main():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF: ")
    endereco = input("Digite o endereço: ")
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuario.adicao_usuario()
    conta = Conta(float(input("Digite o valor inicial do saldo: ")))
    escolha = True
    count = 0
    LIMITE_SAQUES = 3
    while escolha:
        print("\n1 - Depositar \n2 - Sacar \n3 - Extrato Bancário \n4 - Sair")
        escolha = int(input("Digite uma das opções: "))
        
        if escolha == 1:
            valor = float(input("Digite o valor que deseja depositar: "))
            conta.depositar(valor)
        elif escolha == 2:
            if count == LIMITE_SAQUES:
                print("Você atingiu o limite de saques.")
            else:
                valor = float(input("Digite o valor que deseja sacar: "))
                conta.sacar(valor)
                count += 1
        elif escolha == 3:
            conta.extrato()
        elif escolha == 4:
            print("Sistema encerrado.")
            escolha = False
        else:
            print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    main()
