class Super:
 def ola(self):
  print("Olá, sou a superclasse!")
class Sub (Super):
 def ola(self):
   print("Olá, sou a subclasse!")
class Subsub (Sub):
 def ola(self):
  print("Olá, sou a subsubclasse!")
teste1 = Super()
teste1.ola()
teste2 = Sub()
teste2.ola()
teste3 = Subsub()
teste3.ola()