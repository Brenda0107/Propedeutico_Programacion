import numpy as np

class Ecuaciones_Simultaneas():

    def MenuSimultaneas(self):

        print('\n\n BIENVENIDO. Este es un programa que resuelve sistemas de 2 a 5 ecuaciones simultáneas.')

        # Este ciclo es para verificar que lo que ingrese el usuario es válido
        while True:
            v = input("\n \n ¿Cuántas ecuaciones tiene su sistema?: ")

            if v.isdigit() == False:
                print('\n\n\t OPCIÓN INVÁLIDA, INGRESE UN NÚMERO.')
                # Si el usuario ingresa algo que no es un número se vuelve a reiniciar el ciclo

            elif int(v) < 2 or int(v) > 5:
                print('\n\n\t OPCIÓN INVÁLIDA, INGRESE UN NÚMERO ENTRE 2 Y 5')
                # Si el usuario ingresa un número menor que 2 o mayor que 5 se vuelve a reiniar

            else:
                return v
                break  # El usuario ingreso un valor válido


    def MatrizCoeficientes(self,ec):  # ec = número de ecuaciones del sistema

        matriz_coef = np.zeros((ec, ec))  # Se crea la matriz de ceros


        print('\n\n \t Ingrese el valor de: ')
        for i in range(ec):
            for j in range(ec):
                matriz_coef[i, j] = int(input(f'\n \t X_{j + 1}: '))  # Se cambian los ceros por los valores que ingresa el usuario

        print(f'\n\nLos valores de los coeficientes de sus ecuaciones se han representado en forma matricial:\n {matriz_coef}')

        # Se creó este ciclo para corregir los valores con los que el usuario no esté de acuedo
        while True:

            coef_correctos = input('\n\n ¿Los valores mostrados son correctos? (Si/No) ')

            # Si algún valor es incorrecto, se modifica
            if coef_correctos.lower() == 'no':
                fila = int(input('\n\t ¿En qué fila se encuentra? '))
                col = int(input('\n\t ¿En qué columna se encuentra? '))
                nuevo_valor = int(input('\n ¿Cuál es el valor correcto?'))
                matriz_coef[fila - 1, col - 1] = nuevo_valor

                print(matriz_coef)  # Se muestra la matriz modificada y se vuelve a preguntar si ya es correcta

            else:
                return matriz_coef  # La matriz mostrada es correcta, se continua con el resto del programa
                break

    def ValoresIndependientes(self,ec):

        vector_b = np.zeros(ec)

        print('\n \n \t Ingrese el valor de la variable independiente de la ecuación: ')
        for i in range(ec):
            vector_b[i] = int(input(f'\t {i + 1}: '))  # Se cambian los ceros por los valores de la ecuacion

        print(f'\n\nLos valores de las variables independientes se han representado en forma de vector: {vector_b}')

        # Se creó este ciclo para corregir los valores con los que el usuario no esté de acuedo
        while True:

            ind_correctos = input('\n\n ¿Los valores mostrados son correctos? (Si/No) ')

            # Si algún valor es incorrecto, se modifica
            if ind_correctos.lower() == 'no':
                posicion = int(input('\n\t ¿En qué posición se encuentra? '))
                nuevo_valor = int(input('\n ¿Cuál es el valor correcto? '))
                vector_b[posicion - 1] = nuevo_valor

                print(vector_b)  # Se muestra el vector modificado y se vuelve a preguntar si ya es correcto

            else:
                return vector_b
                break  # El vector mostrado es correcto, se continua con el resto del programa


    def Determinante(self, ec, matriz_co, val_ind):  # Se calcula resultado
        determinante = np.linalg.det(matriz_co)

        if determinante != 0:  # Se determina si el sistema tiene o no solución
            Resultado = np.linalg.solve(matriz_co, val_ind)  # Si tiene solución

            for i in range(ec):
                print(f'\n \n El valor de X_{i + 1} es: {round(Resultado[i],3)}')
        else:
            print('\n\n \n \n Su sistema de ecuaciones no tiene solución ya que el determinante es 0.')