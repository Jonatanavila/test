class cafeteria:
    def __init__(self,capacidad_maxima,cantidad_actual):
        self.capacidad_maxima= capacidad_maxima
        self.cantidad_actual= 0
 
    def llenar_cafetera(self):
        lleno = self.capacidad_maxima
        return lleno

    def servir_taza(self,servir):
        servir=self.cantidad_actual + servir
        if servir < self.cantidad_actual:
           print ('me quede sin') 

    def vaciar_cafetera(self,vaciar): 
        vaciar =self.cantidad_actual +  vaciar 
        if vaciar >  self.capacidad_maxima: 
           print ('vaciar') 
        else: 
           print('no vaciar') 

    def agregar_cafe(self,agre_cafe): 
        agre_cafe=self.cantidad_actual + agre_cafe 
        if agre_cafe >  self.capacidad_maxima: 
           print ('te excediste de cafe') 
        else:  
           print ('agregar cafe') 

#como lo ejecute en la terminal
joni=cafeteria(100,0)
 
joni.llenar_cafetera()                                                 
100

joni.servir_taza(-1)                                                  
me quede sin

joni.vaciar_cafetera(102)                                                          
vaciar

joni.vaciar_cafetera(10)
no vaciar

joni.agregar_cafe(101)     
te excediste de cafe 
                                                                                               
joni.agregar_cafe(13) 
agregar cafe
