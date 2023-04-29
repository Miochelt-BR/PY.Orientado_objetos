
class Carro:
    classe= "Veiculo Leve"
    def __init__(self,tipo,cor,placa,portas):
        self.tipo=tipo
        self.cor=cor
        self.placa=placa
        self.portas=portas
        self. status="Estacionamento"
    
    def andar(self):
        self.status="veiculo em movimento"
        
    def parar(self):
        self.status="parado"
        
 
class Veiculo (Carro):
        combustivel="Gasolina " 
        
carro1 = Veiculo ("gol","preto","GTV-2155858",4)
carro2 = Veiculo ("combi","preto","GTV-1457458",2)
    
carro1.andar()
carro1.parar()
carro2.andar()

print("carro1",carro1.tipo,carro1.cor, carro1.placa,carro1.portas, carro1.status, carro1.combustivel)
print("carro2",carro2.tipo,carro2.cor, carro2.placa,carro2.portas, carro2.status, carro2.combustivel)
                     
    