class libro:
   def __init__(self,ibs,titulo,autor,cantidad_de_pagina,pagina_actual):
       self.ibs=ibs
       self.titulo=titulo
       self.autor=autor
       self.cantidad_de_pagina= cantidad_de_pagina
       self.pagina_actual= 0

   def de_quien_es(self):
       print (self.autor)

   def nombre_del_titulo(self):
       print (self.titulo)
  
   def caracteristicas(self):
       print (self.ibs,self.titulo,self.autor,self.cantidad_de_pagina)
   
   def leer(self,pag_leido):
       self.pagina_actual += pag_leido
       if self.pagina_actual >= self.cantidad_de_pagina:
          print ('felicidades,terminaste')
          self.paginas_actual=0

   def en_que_pagina_me_quede(self):
       return self.pagina_actual

#como lo ejecute en la terminal

joni=libro(11221432,'rambo','jonatan',100,0) 

print('titulo:',joni.nombre_del_titulo())                              
rambo

print(joni.de_quien_es())                                              
jonatan

print(joni.caracteristicas())                                          
11221432 rambo jonatan 100

joni.leer(50) 

print('pagina_actual:',joni.en_que_pagina_me_quede())                  
pagina_actual: 50


print('pagina_actual:',joni.en_que_pagina_me_quede())                  
pagina_actual: 100

joni.leer(101)                                                         
felicidades,terminaste


