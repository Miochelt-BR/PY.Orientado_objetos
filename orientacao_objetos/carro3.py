class Carro:
 tipo = ''
 cor = ''
 placa = ''
 num_portas = 0
 def andar(self):
  print('O veículo', self.tipo, self.cor ,self.placa,'está em movimento')
carro1 = Carro()
carro1.tipo = 'Porsche'
carro1.cor = 'Branco'
carro1.placa = 'MHZ-4345'
carro1.num_portas = 4
print('*** Carro 1 ***')
print('Tipo:',carro1.tipo)
print('Cor:',carro1.cor)
print('Placa:',carro1.placa)
print('Num Portas:',carro1.num_portas)
carro1.andar()
Carro.num_portas = 2
carro2 = Carro()
print('*** Carro 2 ***')
print('Num Portas:',carro2.num_portas)