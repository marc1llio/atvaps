#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

qtdNmr = int(input(""))
valAcum = 0 

if qtdNmr <=0:
    print("Informe uma quantidade >0!")

else:
    while qtdNmr > 0:
        nmr = float(input(""))
        valAcum = valAcum + nmr 
        qtdNmr = qtdNmr - 1
    print("Soma dos números informados: %.2f" %(valAcum)) 