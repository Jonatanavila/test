class repartidor:
   def __init__(self,nombre,edad,salario,zona):
       self.nombre=nombre
       self.edad=edad
       self.salario=salario
       self.zona=zona

   def plus(self,plus_porcentaje):
       if self.edad < 25 and self.zona == 'zona3' :
           self.salario= (self.salario * plus_porcentaje) + self.salario
           print ('recibi plus')
 
#como lo ejecute en la terminal
      
zonaplus=repartidor('jonatan',35,12000,3)                              

zonaplus.plus(0.1)                                                      
recibi plus

print(zonaplus.salario)                                                
12000
 

