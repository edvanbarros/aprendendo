salario = float(input("Digite o seu salário bruto: "))
dizimo = salario * 0.10
print(f"Seu Dízimo é R$ {dizimo:0.2f}")

pergunta_oferta = int(input("Vai ofertar? \n DIGITE ( 1 = Sim 2 = Não ) \n"))

if pergunta_oferta == 1:
    oferta = float(input("Qual o valor da Oferta? "))
else:
    oferta = 0

total = dizimo + oferta

print(30 * "#")
print(f"\nTotal da sua Adoração: R$ {total:0.2f}\n")