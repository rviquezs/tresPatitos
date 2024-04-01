import pymongo

class Empleados:
    def __init__(self,cedula=0, nombre=1, telefono=2,apellidos=3,direccion=4,puesto=5,ingreso=6,jefatura=7):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion= direccion
        self.puesto=puesto
        self.ingreso=ingreso
        self.jefatura=jefatura

    def guardarEmpleados(self):
        empleados=pymongo.MongoClient("mongodb://localhost:27017")
        bd=empleados["Empresa"]
        try:
            #definir la tabla a utilizar
            tbl=bd["Empleados"]
            #crear diccionario
            doc={"_id":self.cedula,"Nombre":self.nombre,"Apellidos":self.apellidos,"Telefono":self.telefono,"Direccion":self.direccion,"Puesto":self.puesto,"Ingreso":self.ingreso,"Jefatura":self.jefatura}
            #insertar en la tabla
            tbl.insert_one(doc)
            estado=1
        except Exception:
            print("error al guardar")
            estado=0
        finally:
            empleados.close
        return estado
    
    def actualizarEmpleados(self):
        #abrir la conxion mediante un objeto cliente
        empleados=pymongo.MongoClient("mongodb://localhost:27017")
        bd=empleados["Empresa"]
        try:
            #definir la tabla a utilizar
            tbl=bd["Empleados"]
            #filtro sirve para ver que quiero modificar
            filtro={"_id":self.cedula}
            #crear diccionario
            doc={"$set":{"Nombre":self.nombre,"Apellidos":self.apellidos,"Telefono":self.telefono,"Direccion":self.direccion,"Puesto":self.puesto,"Ingreso":self.ingreso,"Jefatura":self.jefatura}}
            #insertar en la tabla
            tbl.update_one(filtro,doc)
            estado=1
        except Exception:
            print("error al guardar")
            estado=0
        finally:
            empleados.close
        return estado
    
    def eliminarEmpleados(self):
        empleados=pymongo.MongoClient("mongodb://localhost:27017")
        bd=empleados["Empresa"]
        try:
            #definir la tabla a utilizar
            tbl=bd["Empleados"]
            #filtro sirve para ver que quiero modificar
            filtro={"_id":self.id}
            tbl.delete_one(filtro)
            estado=1
        except Exception:
            print("error al Eliminar")
            estado=0
        finally:
            empleados.close
        return estado
    
    def getEmpleados(self):
        empleados=pymongo.MongoClient("mongodb://localhost:27017")
        bd=empleados["Empresa"]
        tbl=bd["Empleados"]
        return tbl.find()
    
    def getRegistrosEmpleados(self):
        empleados=pymongo.MongoClient("mongodb://localhost:27017")
        bd=empleados["Empresa"]
        size=bd.command("collstats","Empleados")
        return size["count"]