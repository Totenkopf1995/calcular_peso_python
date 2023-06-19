# Calculadora de IMC
# IMC = Peso / (Altura x Altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad

def calcularIMC(peso, alturaEnMetros):
    imc = peso / (alturaEnMetros * alturaEnMetros)
    return imc

def pedirElIMC():
    peso = float(input('Ingrese su peso'))
    alturaEnCM = int(input('Ingrse su altura en cm'))
    alturaEnMetros = alturaEnCM / 100
    imc = calcularIMC(peso, alturaEnMetros)

    print('Su IMC es de ' + str(imc))

    if imc < 20:
        print('Estado de delgadez')
    if imc >= 20 and imc < 26:
        print('Peso normal')
    if imc >= 26 and imc < 30:
        print('Estado de sobre peso')
    if imc >= 30:
        print('Estado de obesidad')

print('Calcular el INC de la primer persona')
pedirElIMC()
print('Calcular el INC de la segunda persona')
pedirElIMC()
print('Calcular el INC de la tercer persona')
pedirElIMC()