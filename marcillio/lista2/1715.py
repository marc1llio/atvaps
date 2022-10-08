#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

codigoFuncionario = input()
salarioAtual = float(input())


if codigoFuncionario == "A":
    soma1 = 0.10 * salarioAtual + salarioAtual
    print("Novo salário: R$%.2f" %soma1)

elif codigoFuncionario == "B":
    soma2 = 0.15 * salarioAtual + salarioAtual 
    print("Novo salário: R$%.2f" %soma2)

elif codigoFuncionario == "C":

    soma3 = 0.20 * salarioAtual + salarioAtual
    print("Novo salário: R$%.2f" %soma3)
