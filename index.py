from datetime import datetime
from abc import ABC, abstractmethod
class Usuario:
    lista_usuarios = [] #atributo da class
    def __init__(self, endereco=""): #atributos do objeto
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print(f"Conta número {conta.corrente.numero_conta} adicionada ao usuário {self._nome}.")

    @classmethod
    def listar_usuarios(cls):
        if not cls.lista_usuarios:
            print("Não há usuários cadastrados")
        else:
            for usuario in cls.lista_usuarios:
               print(f"Nome: {usuario['nome']} \nCPF: {usuario['cpf']} \nEndereço: {usuario['endereco']}")
    
    def listar_contas(self):
        if not self._contas:
            print("Nenhuma conta cadastrada para este usuário.")
        else:
            for conta in self._contas:
              print(f"Conta número: {conta.corrente.numero_conta} | Saldo: R$ {conta.saldo}")

class PessoaFisica():
    def __init__(self, nome="", data_nascimento="", cpf=0 ):   
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf   

    def idade(self):
        dia, mes, ano = map(int, self._data_nascimento.split('/'))
        nascimento = datetime(ano, mes, dia)
        data_atual = datetime.now()
        idade = data_atual.year - nascimento.year - ((data_atual.month, data_atual.day) < (nascimento.month, nascimento.day))
        return idade >= 18, idade

    def adicao_usuario(self):
       maior_idade, idade = self.idade()
       if not maior_idade:
          print(f"Usuário menor de idade. Idade: {idade}. Para criar a conta é necessário ser acima de 18 anos.")
          return False

       for usuario in Usuario.lista_usuarios:
          if usuario["cpf"] == self._cpf:
              print("Erro: Este CPF já foi cadastrado.")
              return False
       Usuario.lista_usuarios.append({
          "nome": self._nome,
          "data_nascimento": self._data_nascimento,
          "cpf": self._cpf,
       })
       print(f"Usuário {self._nome} adicionado com sucesso!")
       return True

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

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self.transacoes = []
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)
        print(f"Trasnsação de {transacao.__class__.__name__} adicionada ao histórico.")

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    def registrar(self, conta):
        conta._saldo += self._valor
        conta._historico.adicionar_transacao(self)
        print(f"Depósito de R${self._valor:.2f} realizado com sucesso.")
       
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, conta):
        if self._valor > conta._saldo:
            print("Saldo insuficiente para realizar o saque.")  
        else:
            conta._saldo -= self._valor
            conta._historico.adicionar_transacao(self)
            print(f"Saque de R${self._valor:.2f} realizado com sucesso.")
             
class Conta:
    numero_conta_sequencial = 1
    _AGENCIA = "0001"
    def __init__(self, saldo=0):
        self._saldo = saldo
        self._usuario = Usuario()
        self._historico = Historico()

    def depositar(self, valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

    def sacar(self, valor):
        sacar = Saque(valor)
        sacar.registrar(self)

    def extrato(self):
        print(f"Saldo atual: R${self._saldo:.2f}")

def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = str(input("Digite o nome do usuário: "))
    data_nascimento = str(input("Digite a data de nascimento (dd/mm/aaaa): "))
    cpf = int(input("Digite o CPF: "))
    endereco = input("Digite o endereço: ")
    pessoa = PessoaFisica(nome, data_nascimento, cpf)
    if pessoa.adicao_usuario():
        return Usuario(endereco)
    return None

def adicionar_conta():
    cpf = str(input("Digite o CPF do usuário que deseja adicionar uma conta: "))
    usuario_encontrado = None
    for usuario in Usuario.lista_usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break
    if usuario_encontrado:
        print(f"Usuário {usuario_encontrado['nome']} encontrado. Adicionando nova conta.")
        corrente = Corrente(usuario_encontrado)
        nova_conta = Conta(float(input("Digite o valor inicial do saldo: ")))
        print("Nova conta adicionada com sucesso!")
        return nova_conta
    else:
        print("Usuário não encontrado.")
        return None
        
def listar_contas_usuario():
    cpf = input("Digite o CPF do usuário que deseja listar as contas: ")
    usuario_encontrado = None
    for usuario in Usuario.lista_usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        usuario_obj = Usuario(usuario_encontrado['endereco'])
        usuario_obj.listar_contas()
    else:
        print("Usuário não encontrado.")

def menu_transacoes(conta):
    LIMITE_SAQUES = 3
    count_saques = 0

    while True:
        print("\n--- Menu de Transações ---")
        opcao = int(input("1 - Depositar \n2 - Sacar \n3 - Extrato Bancário \n4 - Voltar \nDigite a opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor que deseja depositar: "))
            deposito = Deposito(valor)
            deposito.registrar(conta)
        
        elif opcao == 2:
            if count_saques >= LIMITE_SAQUES:
                print("Você atingiu o limite de saques.")
            else:
                valor = float(input("Digite o valor que deseja sacar: "))
                saque = Saque(valor)
                saque.registrar(conta)
                count_saques += 1
        
        elif opcao == 3:
            conta.extrato()
        
        elif opcao == 4:
            break
        
        else:
            print("Opção inválida. Tente novamente.")

def main():
   while True:
        print("\n--- Menu Principal ---")
        opcao = int(input("1 - Adicionar novo usuário \n2 - Adicionar conta a usuário existente \n3 - Listar usuários cadastrados\n4 - Listar contas do usuário\n5 - Encerrar sistema\nDigite a opção: "))

        if opcao == 1:
            usuario = cadastrar_usuario()
            if usuario:
                corrente = Corrente(usuario)
                conta = Conta(float(input("Digite o valor inicial do saldo: ")))
                menu_transacoes(conta)
        elif opcao == 2:
            conta = adicionar_conta()
            if conta:
                menu_transacoes(conta)
        elif opcao == 3:
            print("\n--- Lista de Usuários ---")
            Usuario.listar_usuarios()
        
        elif opcao == 4:
            listar_contas_usuario()
        
        elif opcao == 5:
            print("Sistema encerrado.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()