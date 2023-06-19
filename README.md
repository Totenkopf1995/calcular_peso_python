# calcular_peso_python

Calculadora de IMC
Este es un programa simple que calcula el Índice de Masa Corporal (IMC) de una persona y determina su estado de peso. El IMC se calcula utilizando la fórmula IMC = Peso / (Altura x Altura).

El programa solicita al usuario ingresar su peso y altura en centímetros. Luego, se convierte la altura a metros y se utiliza la función calcularIMC para calcular el IMC. A continuación, se muestra el IMC calculado y se imprime el estado de peso correspondiente según los rangos establecidos:

Si el IMC es menor a 20, se muestra el mensaje "Estado de delgadez".
Si el IMC está entre 20 y 25 (inclusive), se muestra el mensaje "Peso normal".
Si el IMC está entre 26 y 30 (inclusive), se muestra el mensaje "Estado de sobrepeso".
Si el IMC es mayor o igual a 30, se muestra el mensaje "Estado de obesidad".
El programa se ejecuta tres veces para calcular el IMC de tres personas diferentes. Cada vez que se ejecuta la función pedirElIMC(), se solicita al usuario que ingrese su peso y altura, y se muestra el resultado correspondiente.
