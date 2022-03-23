
def menu():
    men = 0
    em = empleado()
    while men != 4:
        print("")
        print("  ╔════════════════════════╗")
        print("  ║    ----  MENÚ  ----    ║")
        print("  ╚════════════════════════╝")
        print("  ║ 1. AGREGAR EMPLEADO    ║")
        print("  ║ 2. MOSTRAR EMPLEADO    ║")
        print("  ║ 3. ELIMINAR EMPLEADO   ║")
        print("  ║ 4. Salir               ║")
        print("  ╚════════════════════════╝")
        print("")
        men = int(input(" Ingrese una opcion por favor "))

        if men == 1:
            print("")
            limpiar()
        
        elif men == 2:
            print("")
            em.mostrarEmpleado()
            limpiar()
           

        elif men == 3:
            print("Opcion 3")
            em.eliminarEmpleado()

            

        elif men == 4:
            print("")
            print(" -----   Has salido   -----")
            print(" ***** Muchas Gracias *****")
        
        else:
            print("")
            print(" -----  Opcion no valida  -----")
            print(" ----- Intente Nuevamente -----")
            print("")
            input(" -- Presione una tecla para continuar")
            print("")
            limpiar()

if __name__ == "__main__":
    menu()