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

class Empleado(Persona):
    def __init__(self):
        super().__init__()

    def agregarEmpleado(self):
        super().agregarPersonas()
        self.__salario = float(input("Ingrese su Salario: "))
        self.alimentacion = 0
        self.transporte = 0

        if (self.__salario<2000000):
            self.alimentacion = 80000
            self.transporte = 60000
        
        self.pension = (self.__salario * 0.04)
        self.salud = (self.__salario * 3.375)/100

        self.devengado = self.alimentacion + self.transporte + self.__salario

        self.deduccion = (self.__salario - self.salud - self.pension)
        self.personas[self.id] = (self.cedula, self.nombre, self.apellido, self.direccion, self.telefono, self.__salario, self.alimentacion, self.transporte, self.pension, self.salud, self.devengado, self.deduccion)

    def mostrarEmpleado(self):
        if len(self.personas) == 0:
            print("La lista está vacia")
        else:
            for i, v in self.personas.items():
                print(f"{i}: {v}")

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