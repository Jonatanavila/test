class comercial:
   def __init__(self,nombre,edad,salario,comision):
       self.nombre=nombre
       self.edad=edad
       self.salario=salario
       self.comision=comision

   def plus(self,plus_porcentaje):
       if self.edad > 30 and self.comision > 200:
           self.salario= (self.salario * plus_porcentaje) + self.salario
          print ('recibi plus')


#como lo ejecute en la terminal

masplus=comercial('jonatan',43,24000,250)                             
 
masplus.plus(0.1)                                                      
recibi plus

 print(masplus.salario)                                                 
26400.0


