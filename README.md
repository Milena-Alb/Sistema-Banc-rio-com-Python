# 🏦 Sistema Bancário Simples

Este é um programa simples em Python que simula um sistema bancário com funcionalidades de depósito e saque. O sistema permite que o usuário gerencie seu saldo realizando depósitos e saques, garantindo que o saque só ocorra se houver saldo suficiente.

## 🚀 Funcionalidades

- **Depositar dinheiro**: Permite ao usuário adicionar dinheiro ao saldo da conta.
- **Sacar dinheiro**: Permite ao usuário retirar dinheiro da conta, contanto que o valor solicitado não seja maior do que o saldo disponível.
- **Ver saldo atualizado**: Após cada operação de depósito ou saque, o saldo é atualizado e exibido ao usuário.

## 🛠️ Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Faça o download ou clone este repositório.
3. Abra o terminal e navegue até a pasta onde o arquivo está localizado.
4. Execute o comando:

```bash
python index.py
```
5. Siga as instruções no terminal para realizar transações bancárias.

## 💻 Exemplo de uso
Ao iniciar o programa, o usuário será solicitado a inserir o saldo inicial. Em seguida, o menu oferece as opções:
```bash
Digite o valor inicial do saldo: 500
1 - Depositar 
2 - Sacar 
3 - Sair
Digite uma das opções: 1
Digite o valor que deseja depositar: 200
Depósito realizado. Seu saldo atual é de R$ 700.0
```
## 📂 Estrutura do Código

- ClasseConta : Contém as funcionalidades de depósito e saque, além de armazenar o saldo.

- Métododepositar : Atualiza o saldo ao adicionar o valor depositado.

- Métodosacar : Verifique se o valor do saque é menor ou igual ao saldo disponível antes de realizar a operação.

- Funçãomain : Gerenciar a interação com o usuário, permitindo escolher entre as opções de depositar, sacar ou sair.

## 🤝 Contribuições
Contribuições são sempre bem-vindas! Se você tem ideias para melhorar o projeto ou encontrou um bug, sinta-se à vontade para abrir um issue ou enviar um pull request.