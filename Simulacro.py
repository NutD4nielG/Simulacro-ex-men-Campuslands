def consultarsaldo(saldo_a):
    saldo = saldo_a     
    return saldo

def depos(deposito,saldo_a):
    if deposito <= 0:
        print("Valor introducido no es válido")
    else:
        print("Deposito exitoso")
    return deposito + saldo_a

def sacar(retirar, saldo_a):
    nuevo_saldo = saldo_a
    if retiro <= 0:
        print("Valor introducido no es válido")
    elif retiro > saldo_a:
        print("Saldo insuficiente ")
    else:
        print("Retiro exitoso")
        nuevo_saldo = saldo_a - retirar
    return nuevo_saldo

def menu():
    print(
"""
=====> MENÚ <=======
1. Consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir
""")
    
saldo_a = 1000

while True:
    menu()
    opcion = int(input("Seleccione una opción: "))
    match opcion:
        case 1:
            print(f"Su saldo actual es: {consultarsaldo(saldo_a)}")
        case 2:
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            saldo_a = depos(cantidad,saldo_a)
        case 3:
            retiro = float(input(f"Ingrese el monto de dinero que desea retirar: "))
            saldo_a = sacar(retiro,saldo_a)
        case 4:
            print("Gracias por usar nuestros servicios!, vuelva pronto")
            break
