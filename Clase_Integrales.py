import sympy as sp


class CalculoIntegrales:

    def menu_integrales(self):
        print('''\n\n BIENVENIDO. Este es un programa que realiza integrales simbólicas
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


    def Integral(self, term_d):

        lista = [0, 0, 0, 0, 0]  # Se crea una lista de ceros

        for i in range(term_d):  # Se ingresan de 1 a 5 elementos
            p = int(input(f'\n Ingrese el coeficiente para x^{i + 1}: '))
            lista[i] = p

        while True:  # Se modifica cualquier valor que el usuario decida

            correcto = input(f'''\n \n A continuación se muestran los coeficientes de la función.
             \n ¿La función mostrada es correcta?\n  {lista} \n (SI/NO): ''')

            if correcto.lower() == 'no':
                cambio = int(input('\n\n ¿En qué posición se encuentra el término que desea cambiar? '))
                valor_nuevo = int(input('\n ¿Cuál es el nuevo valor? '))
                lista[cambio-1] = valor_nuevo
            else:
                break

        # Los coeficientes toman los valores de la lista con los valores ya correctos
        coef_a, coef_b, coef_c, coef_d, coef_e = lista[0], lista[1], lista[2], lista[3], lista[4]

        # Se define la variable simbólica
        x = sp.symbols('x')

        #  Se crea la función con los coeficientes
        funcion = (coef_a * x + coef_b * x ** 2 + coef_c * x ** 3 + coef_d * x ** 4 + coef_e * x ** 5)

        # Calcular derivada
        derivada = print(f'\n\n La integral de la función:\n {funcion} es \n {sp.integrate(funcion, x)}')