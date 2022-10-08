#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

hora = float(input())
nhoras = float(input())

total = hora * nhoras
imposto = (total * 0.11)
inss = (total * 0.08 )
sindicato = (total * 0.05)
totalfinal = total - imposto - inss - sindicato


print ("Salário bruto: R$%.2f" %total)
print ("Imposto: R$%.2f" %imposto)
print ("INSS: R$%.2f" %inss)
print ("Sindicato: R$%.2f" %sindicato)
print ("Líquido: R$%.2f " %totalfinal)