
from dojos_y_ninjas.config.mysqlconnection import connectToMySQL
from dojos_y_ninjas.modelos.model_ninja import Ninja

class Dojo:
    def __init__(self,id,name,created_at):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.ninjas = []

    def addNinja(self,ninja):
        self.ninjas.append(ninja)

    @classmethod
    def getDojos(cls):
        query = "SELECT * FROM dojos"
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query)
        return resultado

    @classmethod
    def createDojo(cls,dojo):
        query = "INSERT INTO dojos(name,created_at) VALUES (%(name)s,now());"
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query,dojo)
        return resultado

    @classmethod
    def ninjasOfDojo(cls,data):
        query = '''
                    SELECT * FROM 
                        (SELECT d.id as dojo_id, d.name, n.id as ninja_id, n.first_name, n.last_name, n.age, n.created_at as created_at_ninja, d.created_at as created_at_dojo
                            FROM dojos d left JOIN ninjas n ON d.id = n.dojo_id) 
                    AUX WHERE AUX.dojo_id = %(dojo_id)s
                '''
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query,data)
        print(len(resultado))
        dojo = None
        if  len(resultado) > 0:
            ninjas = []
            dojo = Dojo(resultado[0]["dojo_id"],resultado[0]["name"],resultado[0]["created_at_dojo"])
            for ninja in resultado:
                if ninja["ninja_id"] != None:
                    ninjas.append(Ninja(ninja["ninja_id"],ninja["first_name"],ninja["last_name"],ninja["age"],ninja["created_at_ninja"],ninja["dojo_id"]))
            dojo.ninjas = ninjas
        return dojo
