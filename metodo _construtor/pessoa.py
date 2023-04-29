class Pessoa (object):
    
    def __init__(self,nome , cpf , email ):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        print ("seu nome é ",self.nome, "seu cpf é:",self.cpf, "seu email é ",self.email)
p1 =Pessoa("thiago", 2252558822,"thiago.arica@ gmail.com")
p2 =Pessoa("mestre ", 2252558822,"mestre@mestrepy.com")
        
        
