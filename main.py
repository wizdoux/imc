
print("Olá, este programa é responsável por calcular o seu índice de massa corporal.")

peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)
print("O seu IMC é:", round(imc, 2))

if imc < 18.5:
    print("Abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Peso normal.")
elif 25 <= imc < 30:
    print("Sobrepeso.")
elif 30 <= imc < 35:
    print("Obesidade Grau I.")
elif 35 <= imc < 40:
    print("Obesidade Grau II.")
elif imc >= 40:
    print("Obesidade Grau III.")

print("Espero ter ajudado!")

