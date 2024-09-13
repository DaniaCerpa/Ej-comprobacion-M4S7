#Creación de nueva clase de error
class EdadError(Exception):
 def __init__(self, valor, mensaje ="La edad ingresada no corresponde a una edad valida"):
    self.mensaje = mensaje
    self.valor = valor
    super().__init__(f"{mensaje}:'{valor}'")


#Creación de función 
def ingreso_edad ():
    
    """ Esta función busca conseguir la edad del usuario y validar esta a traves de un bloque try-except.
        Si la edad no es valida retornara un error del tipo EdadError
    """
    try:
        edad = input("Ingrese su edad: ")
        edad = int(edad)
        
        if edad < 0 or edad > 120:
            raise EdadError(edad)
        
        elif edad >= 18:
            print("El usuario corresponde a un Adulto")
            
        elif edad >0 and edad < 18:
            print("El usuario no corresponde a un Adulto")
        
    #Por defecto Python lanzará el error de tipo ValueError al intentar volver un string no numerico a un numero entero.
    #Se establece de este modo un remplazo del error lanzado por defecto por nuestro error personalizado, EdadError. 
    except ValueError:
        raise EdadError(edad)
        

#Se personaliza la salida al usuario, estableciendo un mensaje determinado para ambos casos de excepcion en nuestra función.        
try:    
    nueva_edad = ingreso_edad()

except EdadError as e:
        print(f"{type(e).__name__} - {e}.\n Porfavor ingrese una edad valida")
        
