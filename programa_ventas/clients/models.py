import uuid #Para generar Ids unicas

class Client:
    def __init__(self,name,company,email,position,uid=None):
        self.name=name
        self.company=company
        self.email=email
        self.position=position
        self.uid=uid or uuid.uuid4() #estandar de la industria para generar IDs unicos

    def to_dict(self):
        return vars(self) #convierte en diccionario

    @staticmethod
    def schema():
        return ["name","company","email","position","uid"]
