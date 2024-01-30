# Programa de acompanhamento de Dieta
# Autor: Antônio Augusto Bezerra Sandes Martins

# Receber dados do usuário

# Nome do usuário
name = input("Qual o seu nome?\n")

# Peso do usuário
weight = float(input("Qual o seu peso em quilos? ex: 65.6\n"))

# Altura do usuário
height = float(input("Qual a sua altura em metros? ex: 1.75 \n"))

# Idade do usuário
age = int(input("Qual a sua idade?\n"))

# Sexo do usuário
type = input("Qual o seu sexo ? (M/F) \n")

# Calcular IMC
imc = weight / (height * height)

# Calcular TMB (METABOLISMO BASAL)
if type == "M" or type == "m":
    tmb = 88.362 + (13.4 * weight) + (4.799 * height * 100) - (5.677 * age)
elif type == "F" or type == "f":
    tmb = 447.593 + (9.247 * weight) + (3.1 * height * 100) - (4.3 * age)
else:
    print("Sexo inválido!")

# Calcular Quantidade de água por dia
water = weight * 35
# Calcular NCD
ncd = tmb * 1.6

# Calcular calorias para emagrecer
caloriesdown = ncd - 500

# Calcular calorias para manter
calories = ncd

# Calcular calorias para engordar
caloriesup = ncd + 500

# Exibir dados do usuário

print("Olá, " + name + "!")
print("Seu IMC é: " + str(imc))
print("Seu Metabolismo Basal é: " + str(tmb))
print("Seu Necessidade Calórica Diária é: " + str(ncd))
print("\n\n")

# Exibir menu de opções
print("Escolha uma opção:\nn")
print("MENU:\n")
print("0 - Engordar")
print("1 - Emagrecer")
print("2 - Manter o peso")
print("3 - Sair")
print("\n\n")


option = int(input("Digite a opção desejada: \n"))

if option == 0:
    print("Você precisa consumir " + str(caloriesup) + " calorias por dia para engordar!")
    print("Você precisa consumir " + str(water) + " ml de água por dia!")

elif option == 1:
    print("Você precisa consumir " + str(caloriesdown) + " calorias por dia para emagrecer!")
    print("Você precisa consumir " + str(water) + " ml de água por dia!")
elif option == 2:
    print("Você precisa consumir " + str(calories) + " calorias por dia para manter o peso!")
    print("Você precisa consumir " + str(water) + " ml de água por dia!")
elif option == 3:
    print("Até logo!")
else:
    print("Opção inválida!")

