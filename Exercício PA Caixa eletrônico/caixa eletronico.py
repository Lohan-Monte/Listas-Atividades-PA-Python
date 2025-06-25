# Dados do usuário
usuario = ["Alessandro", "12345-6", "123", 1000.49]  # Nome, Conta, Senha, Saldo

# Tela de login
print(" Bem-vindo ao Caixa Eletrônico ")

conta = input("Digite sua conta: ")
senha = input("Digite sua senha: ")

# Verificar se a conta e senha estão corretas
if conta == usuario[1] and senha == usuario[2]:
    print(f"\n Login bem-sucedido. Bem-vindo, {usuario[0]}!")

    while True:
        print("\n--- Menu ---")
        print("1 - Consultar saldo")
        print("2 - Realizar saque")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"\n Seu saldo atual é: R$ {usuario[3]:.2f}")

        elif opcao == "2":
            valor = float(input("\nInforme o valor para saque (múltiplos de R$10, máximo R$1500): R$ "))

            if valor > usuario[3]:
                print(" Saldo insuficiente.")
            elif valor > 1500:
                print(" Valor excede o limite máximo por operação (R$1500).")
            elif valor % 10 != 0:
                print(" O valor deve ser múltiplo de R$10.")
            else:
                # Cálculo das notas
                notas100 = int(valor // 100)
                valor = valor % 100

                notas50 = int(valor // 50)
                valor = valor % 50

                notas20 = int(valor // 20)
                valor = valor % 20

                notas10 = int(valor // 10)

                # Atualizar saldo
                usuario[3] -= (notas100 * 100 + notas50 * 50 + notas20 * 20 + notas10 * 10)

                # Exibir as notas
                print("\nNotas entregues:")
                if notas100 > 0:
                    print(f"R$100: {notas100} nota(s)")
                if notas50 > 0:
                    print(f"R$50: {notas50} nota(s)")
                if notas20 > 0:
                    print(f"R$20: {notas20} nota(s)")
                if notas10 > 0:
                    print(f"R$10: {notas10} nota(s)")

                print(f"\n Saque realizado com sucesso. Novo saldo: R$ {usuario[3]:.2f}")

        elif opcao == "3":
            print("\n Obrigado por usar o Caixa Eletrônico. Até logo!")
            break

        else:
            print(" Opção inválida. Tente novamente.")

else:
    print(" Conta ou senha inválidos. Acesso negado.")
