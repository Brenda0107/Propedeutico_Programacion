import os
from Clase_Derivadas import *
from Clase_Simultaneas import *
from Clase_Integrales import *

###################################################################################
#                                  MENÚ GENERAL
####################################################################################

regresar = 0

while regresar == 0:

    os.system('cls')  # Limpiar pantalla para cuando se elija reiniciar el programa

    print('''Bienvenido. Este es un programa que puede realizar lo siguiente:
    \n \t 1. Resolver ecuaciones simultáneas
    \n \t 2. Realizar derivadas
    \n \t 3. Realizar integrales''')

    # Se realiza este bucle para que si el usuario elige una opción incorrecta el
    # usuario pueda corregir y no se termine el programa
    while True:
        opcion = int(input('\n Por favor, seleccione la opción que desea realizar: '))

        if opcion < 1 or opcion > 3:
            print('\n \t OPCIÓN INVÁLIDA, INTENTE DE NUEVO')  # El usuario corrige

        else:
            break  # El programa continua

#################################################################################
#                   SISTEMAS DE ECUACIONES SIMULTÁNEAS
##################################################################################
    if opcion == 1:
        ec_sim = Ecuaciones_Simultaneas()  #Se manda a llama a la clase
        menu_simul = ec_sim.MenuSimultaneas()  # Se manda a llamar al menú

        ec = int(menu_simul)  # Se convierte a int la salida del menú

        matriz_co = ec_sim.MatrizCoeficientes(ec)  # Se manda a llamar al método para realizar la matriz de coef

        val_ind = ec_sim.ValoresIndependientes(ec)  # Se manda a llamar al método para crear el vector de valores ind

        resul_sim = ec_sim.Determinante(ec, matriz_co, val_ind)  # Se manda a llamar al método que resuelve el sistema

###################################################################################
#                             DERIVADAS
#################################################################################
    if opcion == 2:
        derivadas = Calculo_Derivadas()  # Se manda a llamar a la clase
        menu_int = derivadas.MenuDerivadas()  # Se llama al menú

        term_d = menu_int  # Se pasa la variable luego de haber comprobado que es un número entre 1 y 5

        resul_der = derivadas.Derivadas(term_d)  # Se manda a llamar al método que resuelve la función

#####################################################################################
#                               INTEGRALES
####################################################################################

    if opcion == 3:
        integrales = CalculoIntegrales()  # Se manda a llamar a la clase
        menu_int = integrales.menu_integrales()   # Se llama al menú

        term_d = menu_int   # Se guarda la salida del método anterior en una nueva variable

        result_int = integrales.Integral(term_d)  # Se manda a llamar al método que integra la función

#####################################################################################
#                         REINICIAR EL PROGRAMA (SI/NO)
#####################################################################################

    volver = input('\n \n ¿Desea volver a ejecutar el programa? (Si/No) ')

    if volver.lower() == 'si':
        regresar = 0

    else:
        print('\n \n \t Gracias por utilizar el programa')
        break