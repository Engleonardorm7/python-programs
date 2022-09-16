class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad=edad

    def info1(self):
        
        print("mi nombre es: ", self.nombre, "mi edad es: ", self.edad)
        

class Doctor(Persona):
    def __init__(self, nombre, edad,especialidad):
        
        super().__init__(nombre, edad)
        self.especialidad=especialidad
    
    def info(self):
        
        print("mi especialidad es: ", self.especialidad)
        

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        
        super().__init__(nombre, edad)
        self.carrera=carrera

    def info(self):
        
        print("mi carrera es: ", self.carrera)

def main():
    estudiante=Estudiante("Leonardo",29,"ingeniero")
    doctor=Doctor("Carlos",54,"Cardiologo")
    doctor.info1()
    doctor.info()
    estudiante.info1()
    estudiante.info()


if __name__=="__main__":
    
    main()
