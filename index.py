from datetime import datetime
class Usuario:
    lista_usuarios = [] #atributo da class
    def __init__(self, nome="", data_nascimento="", cpf=0, endereco=""): #atributos do objeto
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []
    def idade(self):
        dia, mes, ano = map(int, self.data_nascimento.split('/'))
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
          if usuario["cpf"] == self.cpf:
              print("Erro: Este CPF já foi cadastrado.")
              return False
       Usuario.lista_usuarios.append({
          "nome": self.nome,
          "data_nascimento": self.data_nascimento,
          "cpf": self.cpf,
          "endereco": self.endereco
       })
       print(f"Usuário {self.nome} adicionado com sucesso!")
       return True

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta número {conta.corrente.numero_conta} adicionada ao usuário {self.nome}.")

    def listar_usuarios(self):
        if not Usuario.lista_usuarios:
            print("Não há usuários cadastrados")
        else:
            for usuario in Usuario.lista_usuarios:
               print(f"Nome: {usuario['nome']} \nCPF: {usuario['cpf']} \nEndereço: {usuario['endereco']}")
    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada para este usuário.")
        else:
            for conta in self.contas:
              print(f"Conta número: {conta.corrente.numero_conta} | Saldo: R$ {conta.saldo}")

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
    def __init__(self, usuario, corrente, saldo=0):
        self.saldo = saldo
        self.usuario = usuario
        self.corrente = corrente
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
        print(f"Nome: {self.usuario.nome} \nCPF: {self.usuario.cpf} \nEndereço: {self.usuario.endereco}")
        print(f"Agência: {self.corrente.informacoes_conta()['agencia']} \nConta: {self.corrente.informacoes_conta()['numero_conta']}")
        if not self.transacoes:
            print("Nenhuma transação foi realizada.")
        else:
            for transacao in self.transacoes:
                print(f"{transacao['Tipo']}: R$ {transacao['valor']}")
        print(f"Saldo atual: R$ {self.saldo}")
        print("--------------------------\n")


def main():
    usuario_novo = True
    LIMITE_SAQUES = 3

    while usuario_novo:
        count = 0
        escolha = True
        print("\n--- Menu Principal ---")
        adicionar_usuario = int(input("1 - Adicionar novo usuário \n2 - Adicionar mais uma conta ao usuário \n3 - Listar usuários cadastrados\n4 - Listar contas do usuário\n5 - Encerrar sistema \n"))
        if adicionar_usuario == 1:
            print("\n--- Cadastro de Usuário ---")
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Digite o CPF: ")
            endereco = input("Digite o endereço: ")
            usuario = Usuario(nome, data_nascimento, cpf, endereco)
            corrente = Corrente(usuario)
            if not usuario.adicao_usuario():
                print("Usuário não cadastrado")
                continue
            else:
                conta = Conta(usuario, corrente, float(input("Digite o valor inicial do saldo: ")))

        elif adicionar_usuario == 2:
            cpf = input("Digite o CPF do usuário que deseja adicionar uma conta: ")
            usuario_encontrado = None
            for usuario in Usuario.lista_usuarios:
                if usuario['cpf'] == cpf:
                    usuario_encontrado = usuario
                    break
            if usuario_encontrado:
                print(f"Usuário {usuario_encontrado['nome']} encontrado. Adicionando nova conta.")
                corrente = Corrente(usuario_encontrado)
                nova_conta = Conta(usuario_encontrado, corrente, float(input("Digite o valor inicial do saldo: ")))
                print("Nova conta adicionada com sucesso!")
            else:
                print("Usuário não encontrado. Tente novamente.")
                continue
        elif adicionar_usuario == 3:
            usuario_lista = Usuario()
            usuario_lista.listar_usuarios()
            continue
        elif adicionar_usuario == 4:
            #lista as contas
            cpf = input("Digite o CPF do usuário que deseja listar as contas: ")
            usuario_encontrado = None
            for usuario in Usuario.lista_usuarios:
                if usuario["cpf"] == cpf:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                usuario_obj = Usuario(usuario_encontrado['nome'], usuario_encontrado['data_nascimento'], usuario_encontrado['cpf'], usuario_encontrado['endereco'])
                usuario_obj.listar_contas()
            else:
                print("Usuário não encontrado. Tente novamente.")
                continue
        elif adicionar_usuario == 5:
            # Encerrar sistema
            usuario_novo = False
            print("Sistema encerrado.")
        else:
            print("Opção inválida. Tente novamente.")
            break

        while escolha:
            print("\n1 - Depositar \n2 - Sacar \n3 - Extrato Bancário \n4 - Sair \n")
            opcao = int(input("Digite uma das opções: "))
            if opcao == 1:
                valor = float(input("Digite o valor que deseja depositar: "))
                conta.depositar(valor)
            elif opcao == 2:
                if count == LIMITE_SAQUES:
                    print("Você atingiu o limite de saques.")
                else:
                    valor = float(input("Digite o valor que deseja sacar: "))
                    conta.sacar(valor)
                    count += 1
            elif opcao == 3:
                conta.extrato()
            elif opcao == 4:
                print("Sistema encerrado para o usuário.")
                escolha = False
            else:
                print("Opção inválida. Tente novamente")
if __name__ == "__main__":
    main()