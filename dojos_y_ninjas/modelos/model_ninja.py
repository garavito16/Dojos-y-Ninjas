
from dojos_y_ninjas.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, id, first_name, last_name, age, created_at, dojo_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_at = created_at
        self.dojo_id = dojo_id

    @classmethod
    def createNinja(cls,ninja):
        query = "INSERT INTO ninjas(first_name, last_name, age, created_at, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,now(),%(dojo_id)s);"
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query,ninja)
        return resultado