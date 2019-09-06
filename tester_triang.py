import unittest 
import progtri 

class testProgtri(unittest.TestProgtri):
      
   def test_notriangulo(self):
       self.asserEqual(progtri.notri(1,1,100),'no es triangulo')

   def test_notri(self):
       self.asserEqual(progtri.notri(3,8,40),'no es triangulo')

   def test_ladosiguales(self):
       self.asserEqual(progtri.sitri(8,8,8),'tres lados iguales')

   def test_noexittri(self):
       self.asserEqual(progtri.notri(1,50,100),'no es tri') 

   def test_ladosdiferentes(self):
       self.asserEqual(progtri.tri_tresdist(30,40,50),'son distintos')

   def test_notri(self):
       self.asserEqual(progtri.notri(5,5,10),'no es triangulo')

   def test_notri(self):
       self.asserEqual(progtri.tri_tresdist(32,44,16),'no es triangulo')

   def test_noestri(self):
       self.asserEqual(progtri.notri(20,80,30),'no es un triangulo')

   def test_unladodiferente(self):
       self.asserEqual(progtri.tri_dosigual(25,10,25),'dos lados iguales')

   def test_ladosdesiguales(self):
       self.asserEqual(progtri.tri_tresdist(32,44,56),'son distintos')

   def test_ladosiguales(self):
       self.asserEqual(progtri.sitri(1,1,1),'tres lados iguales')

   def test_iguales(self):
       self.asserEqual(progtri.sitri(100,100,100),'tres lados igual')

   def test_dosigual(self):
       self.asserEqual(progtri.tri_dosigual(90,46,46),'dos lados iguales')
