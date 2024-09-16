class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saque não realizado, valor maior que o saldo")
        else:
            self.saldo -= valor
            print(f"Saque realizado. Seu saldo atual é de R$ {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito realizado. Seu saldo atual é de R$ {self.saldo}")

def main():
    conta = Conta(float(input("Digite o valor inicial do saldo: ")))
    
    escolha = True
    while escolha:
        print("\n1 - Depositar \n2 - Sacar \n3 - Sair")
        escolha = int(input("Digite uma das opções: "))
        
        if escolha == 1:
            valor = float(input("Digite o valor que deseja depositar: "))
            conta.depositar(valor)
        elif escolha == 2:
            valor = float(input("Digite o valor que deseja sacar: "))
            conta.sacar(valor)
        elif escolha == 3:
            print("Sistema encerrado.")
            escolha = False
        else:
            print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    main()
