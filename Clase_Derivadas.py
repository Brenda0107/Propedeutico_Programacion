import sympy as sp


class Calculo_Derivadas():

    def MenuDerivadas(self):
        print('''\n\n BIENVENIDO. Este es un programa que realiza derivadas simbólicas
                para ecuaciones de entre 1 y 5 términos de la forma: 
                \n \t \t f(x) = ax + bx^2 + ... + cx^5''')

        while True:  # Este ciclo es para verificar que lo que ingrese el usuario es válido
            terminos = input('\n \n ¿Cuántos terminos tiene su ecuación? ')

            if terminos.isdigit() == False:
                print('\n\n\t OPCIÓN INVÁLIDA, INGRESE UN NÚMERO')

            elif int(terminos) < 1 or int(terminos) > 5:
                print('\n\n\t OPCIÓN INVÁLIDA, INGRESE UN NÚMERO ENTRE 2 Y 5')

            else:
                return int(terminos)
                break


    def Derivadas(self, term_d,coef_a=0,coef_b=0, coef_c=0, coef_d=0, coef_e=0 ): # Se establecen por default los coef a 0

        lista = [0, 0, 0, 0, 0] # Se define una lista inicial con ceros

        for i in range(term_d):  # Se agregan cuantos terminos el usuario haya configurado en el paso anterior
            p = int(input(f'\n Ingrese el coeficiente para x^{i + 1}: '))
            lista[i] = p  # Se generan la lista inicial de los coeficientes

        while True:  # El bucle es para saber si los valores son correctos o el usuario desea cambiar algo

            correcto = input(f'''\n \n A continuación se muestran los coeficientes de la función.
             \n ¿La función mostrada es correcta?\n  {lista} \n (SI/NO): ''')

            if correcto.lower() == 'no':
                cambio = int(input('\n\n ¿En qué posición se encuentra el término que desea cambiar? '))
                valor_nuevo = int(input('\n ¿Cuál es el nuevo valor? '))
                lista[cambio-1] = valor_nuevo  # Se muestran los nuevos coeficientes
            else:
                break  # Los coeficientes son correctos, se continúa con el programa

        # Ahora los coeficientes toman los valores de la lista ya corregida, si el usuario ingresó menos
        # de 5 coeficientes, estos ya tienen asignado el valor de 0
        coef_a, coef_b, coef_c, coef_d, coef_e = lista[0], lista[1], lista[2], lista[3], lista[4]

        # Se define la variable simbólica
        x = sp.symbols('x')

        #  Se crea la función con los coeficientes que ingresó el usuario
        funcion = (coef_a * x + coef_b * x ** 2 + coef_c * x ** 3 + coef_d * x ** 4 + coef_e * x ** 5)

        # Se calcula la derivada y se muestra el resultado en pantalla
        derivada = print(f'\n\n La derivada de la función:\n {funcion} \t es \n {sp.diff(funcion, x)}')