menu = f"""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

dinheiroAtual = 5000.00
quantidadeSaques = 0
rodando = True
operacoes = {}

while rodando == True:
    selecao = input(f"{menu}\n")
    try:
        
        if selecao == "d":
            deposito = int(input("Quantidade a ser depositado: "))
            try:
                dinheiroAtual += deposito
                operacoes[len(operacoes)+1] = f"Deposito de: {deposito}, Saldo: {dinheiroAtual}"
                print(f"Deposito executado!, Saldo atual: {dinheiroAtual}")
            except:
                print("Valor Invalido!")  
        elif selecao == "s":
            saque = int(input("Quantidade a ser sacada: "))
            try:
                if dinheiroAtual >= saque:
                    if quantidadeSaques < 3:
                        if saque <= 500:
                            dinheiroAtual -= saque
                            quantidadeSaques += 1
                            operacoes[len(operacoes)+1] = f"Saque de: {saque}, Saldo: {dinheiroAtual}"
                            print(f"Saque executado!, Salto atual: {dinheiroAtual}")
                        else: 
                            print(f"Valor Maximo de Saque: R$500.00")
                    else:
                        print(f"Alcançou limite diario!")
            except:
                print("Valor acima do Saldo ou Invalido!")
        elif selecao == "e":
            i = 1
            while i <= len(operacoes):
                print(f"\n{operacoes[i]}")
                i += 1
        elif selecao == "q":
            rodando = False                                           
    except:
        print("Opção Invalida!")            

