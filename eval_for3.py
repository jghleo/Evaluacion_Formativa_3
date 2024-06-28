import os
import time
sis = os.system("cls")
reg = []

def menu():
    print("1. Registrar trabajador \n2. Listar los todos los trabajadores \n3. Imprimir planilla de sueldos \n4. Salir del Programa")

def registro():
    while True:
        sis
        try: 
            nom = input("Ingrese el nombre del trabajador: ")
            car = input("Ingrese el cargo del trabajador: ")
            sulB = int(input("Ingrese el sueldo bruto del trabajador: "))
            desS = round(sulB* 0.08)
            desA = round(sulB * 0.12)
            sulL = round(sulB * 0.8)
            reg.append([nom,car,sulB,desS,desA,sulL])
            wh = input("Deseas continuar si(1) no(2)")
            if wh != 1:
                break
            return registro
        except ValueError:
            print("Error: en introducir el sueldo, utilisaste letras")

def Lista():
    if reg == None:
        print("Antes de ver lista tienes que registrar los trabajadores")
        time.sleep("")
    else:
        sis
        for i in reg:
            for element in i:
                print(element, n='')
                time.sleep(0.4)
            return(Lista)
def imprimir():
    with open('trava.txt','w',n='') as tar:
        tar.write("Trabajador", "Cargo", "Desc. Salud", "Desc. AFP", "Líquido a pagar")
        tar.writelines(reg)

def salir():
    sis
    print("Saliendo del programa \n Gracias")
    time.sleep(0.8)
    exit()
while True:
    sis
    try:
        menu()
        op = int(input("Selecione: "))
        if op == 1:
            registro
        elif op == 2:
            Lista
        elif op == 3:
            imprimir
        elif op == 4:
            salir
        else:
            print("Error: selecionar las opciones, opcion inválida")
            time.sleep(0.8)
    except ValueError:
        print("Error: selecionar las opciones, opcion inválida")
        time.sleep(0.8)