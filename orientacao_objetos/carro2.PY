class Carro:
    #atributos que contem na sua classe:
    tipo= ""
    cor =""
    placa=""
    portas =""
    
    #funcao 
    def andar(self):
      print("o veiculo",self.tipo, self.cor,"esta em movimento ")
    def parar(self):
        print("parar",self.tipo,"precisa parar")

# criando objetos: 
carro1= Carro()
carro1.tipo = "combi"
carro1 .cor="branco"
carro1.placa = "Th2 45474"
carro1.portas = "4"
print ("Tipo:",carro1.tipo)
print ("cor:",carro1.cor)
print ("placa:",carro1.placa)
print ("portas:",carro1.portas)
#chmando a funcao 
carro1.andar ()
carro1.parar ()
