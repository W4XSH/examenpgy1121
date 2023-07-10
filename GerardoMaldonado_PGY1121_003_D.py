from os import system
system("cls")

cant=0
asientos=list(range(1,101))
reservas=[None]*101

Asi_Platinum=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Asi_Gold=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
Asi_Silver=[51,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]

valor_Platinum= int(120000)
valor_Gold= int(80000)
valor_Silver= int(50000)



def pausa():
    input("Presione una tecla para continuar...")
    system("cls")

def mostrar_asientos():
    print("____________________ESCENARIO____________________")
    print("| ", end="")
    for asiento in asientos:
        print(asiento, end=" | ")
    print()

def reservado_por():
    for i in range(len(asientos)):
        if reservas[i]!=None:
            print(f"{i+1} - RUT:{reservas[i]}")

def reservar(rut:str):
    while True:
        mostrar_asientos()
        asiento=input("Indique el número de sala a reservar o X para salir: ")
        if asiento.lower()=="x":
            return

        if asiento in "12345678910121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162646566676869707172737475767778798081828384858687888990919293949596979899100" and len(asiento)==1 and asientos[(int(asiento))-1]!="X":
            asientos[(int(asiento))-1]="X"
            reservas[(int(asiento))-1]=rut
            print("Sala reservada exitosamente!!!.....")
            return

        else:
            print("Número del asiento no válido o asiento ocupado")

def ganancias():
    print(f"""
    _______Tipo Entrada_______|__Cantidad__|______Total______|
    Platinum ${valor_Platinum}|            |
    Gold     ${valor_Gold}    |            |
    Silver   ${valor_Silver}  |            |
    Total                     |            |          
    """)

while True:
    system("cls")
    print("""
    ***** Operaciones *****

    1. Comprar Entradas
    2. Mostrar Ubicaciones Disponibles
    3. Ver Listado de Asistentes
    4. Mostrar Ganancias Totales
    5. Salir
    """)

    op=input("Ingrese opción: ")

    match op:
        case "1":
            print(f"""
            Lista de Precios:
            Platinum: ${valor_Platinum}. (Asientos del 1 al 20)
            Gold: ${valor_Gold}. (Asientos del 21 al 50)
            Silver: ${valor_Silver}. (Asientos del 51 al 100)
            """)
            rut=input("Para Reservar\nIngrese su Rut: ")
            reservar(rut)

        case "2":
            mostrar_asientos()
        case "3":
            reservado_por()
        case "4":
            ganancias()
        case "5":
            print("SALIDA DE SISTEMA\nGerardo Maldonado\n10/07/2023")
            pausa()
            break
        case other:
            print("Opcion no valida...")

    pausa()

#https://github.com/W4XSH/examenpgy1121
