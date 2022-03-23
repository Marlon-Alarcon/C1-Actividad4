import os

class Persona:

    def __init__(self):
        self.personas = {}

    def agregarPersonas(self):
        self.id = input("ID: ")
        if self.id in self.personas:
            print("Este codigo ya existe.")
        else:
            self.cedula = input("Ingrese su cedula: ")
            self.nombre = input("Ingrese su nombre: ")
            self.apellido = input("Ingrese su apellido: ")
            self.direccion = input("Ingrese su direccion: ")
            self.telefono = input("Ingrese su telefono: ")
            self.personas[self.id] = (self.cedula, self.nombre, self.apellido, self.direccion, self.telefono)

    def menu (self, opciones):
        while(True):
            os.system("clear")
            for item in range (len(opciones)):
                print (opciones[item])

            opcion = input("Digite una opcion correcta: ")

            if opcion == "1":
                os.system("clear")
                self.agregarEmpleado()

            elif opcion == "2":
                os.system("clear")
                self.mostrarEmpleado()
                input("Digite enter para continuar")
            
            elif opcion == "3":
                break

            elif opcion == "4":
                print("")
                print(" -----   Has salido   -----")
                print(" ***** Muchas Gracias *****")
                break
def menuPrincipal():
    os.system("clear")
    opciones = ( #menu en forma de tupla
        " ╔════════════════════════╗",
        " ║    ----  MENÚ  ----    ║",
        " ╚════════════════════════╝",
        " ║ 1. AGREGAR EMPLEADO    ║",
        " ║ 2. MOSTRAR EMPLEADO    ║",
        " ║ 3. ELIMINAR EMPLEADO   ║",
        " ║ 4. Salir               ║",
        " ╚════════════════════════╝"
    )
    emp = Empleado ()
    emp.menu(opciones)

def main():
    menuPrincipal()


if __name__ == "__main__":
    main()