#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

salarioMinimo = 1192.40

valorHoraExtra = 10.00



nome = input("")

horasExtras = float(input(""))




salarioHoraExtra = horasExtras * valorHoraExtra

salarioBruto = 3 * salarioMinimo + salarioHoraExtra







if salarioBruto > 2000:



    if salarioBruto >2500:

        descontoImpostoRenda20 = 0.20 * salarioBruto

        descontoInss = 0.12 * salarioBruto

        salarioLiquido = salarioBruto - descontoInss - descontoImpostoRenda20

    else:

        descontoInss = 0.12 * salarioBruto

        salarioLiquido = salarioBruto - descontoInss




else:

    descontoInss = 0.05 * salarioBruto

    salarioLiquido = salarioBruto - descontoInss





print("Nome: %s" %(nome))

print("Salário Bruto: R$%.2f" %salarioBruto)

print("Salário líquido: R$%.2f" %salarioLiquido)