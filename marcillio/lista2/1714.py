#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

preçoCompra = float(input())

if  preçoCompra < 20.00: 
    valorProduto = preçoCompra * 0.45 + preçoCompra
    print("Valor de venda: R$%.2f" %valorProduto)

else:
    valorProduto2 = preçoCompra * 0.30 + preçoCompra
    print("Valor de venda: R$%.2f" %valorProduto2)