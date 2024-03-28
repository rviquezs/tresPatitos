import pymongo


class Asignar:
    def __init__(self, cedula, nombre, apellidos, telefono, bienAsignado):
        self.cedula = cedula
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.bienAsignado = bienAsignado

    def guardar(self):
        estado=0
        #abrir la conexión mediante un objeto cliente
        bienAsignado= pymongo.MongoClient("mongodb://localhost:27017")
        #seleccionar la tabla a utilizar
        bd=bienAsignado["Empresa"]
        try:
            #definir la tabla a utilizar
            tbl=bd["bienes asignados"]
            #crear diccionario
            doc={"_id":self.cedula,
                "nombre":self.nombre,
                "apellidos":self.apellidos,
                "telefono":self.telefono,
                "bien asignado": self.bienAsignado}
            #insertar en la tabla
            tbl.insert_one(doc)
            estado=1
        except Exception:
            print("error al guardar")
            estado=0
        finally:
            bienAsignado.close        
        return estado

    def actualizar(self):
        estado = 0
        # abrir la conexión mediante un objeto cliente
        bienAsignado = pymongo.MongoClient("mongodb://localhost:27017")
        # seleccionar la tabla a utilizar
        bd = bienAsignado["Empresa"]
        try:
            # definir la tabla a utilizar
            tbl = bd["bienes asignados"]
            # filtro
            filtro = {"_id": self.cedula}
            # crear diccionario
            doc = {
                "$set": {
                    "nombre": self.nombre,
                    "apellidos": self.apellidos,
                    "telefono": self.telefono,
                    "bien asignado": self.bienAsignado
                }
            }
            # modifcar en la tabla
            tbl.update_one(filtro,doc)
            estado = 1
        except Exception:
            print("error al modificar")
            estado = 0
        finally:
            bienAsignado.close
        return estado

    def eliminar(self):
        estado = 0
        # abrir la conexión mediante un objeto cliente
        bienAsignado = pymongo.MongoClient("mongodb://localhost:27017")
        # seleccionar la tabla a utilizar
        bd = bienAsignado["Empresa"]
        try:
            # definir la tabla a utilizar
            tbl = bd["bienes asignados"]
            # filtro
            filtro = {"_id": self.cedula}
            # modifcar en la tabla
            tbl.delete_one(filtro)
            estado = 1
        except Exception:
            print("error al eliminar")
            estado = 0
        finally:
            bienAsignado.close
        return estado