#Una funcion es un bloque de codigo que solo corre cuando se  le llama. En python no usamos corchetes, usamos indentacion con tabs o espacios

#Crear a function, esta funcion no regresa nada solo imprime
def decirHola(nombre=''):
    print('Hola {0}'.format(nombre))

decirHola('Andres')
decirHola()

#Funcion que me regresa un valor
def hacerSuma(num1, num2):
    total = num1 + num2
    return float(total)

hacerSuma(2,3)
print(hacerSuma(2,3),type(hacerSuma(2,3)))

x = 2
y = 2
total = hacerSuma(x,y)
print(total,type(total),"**lo mismo pero mas cool**")


# #FUNCION lambda
# # Una funcion lambda es una funcion anonima
# # Una funcion lambda puede tomar cualquier numero de argumentos, pero tener solo una expresion

# print("--------")
# hacerSuma2 = lambda num1, num2 : num1 + num2

# print(hacerSuma2(10,3))

