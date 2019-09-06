class Electrodomestico():
      def __init__(self,precio,tipo,color,peso,horas_de_uso,consumo_energetico):
          self.precio=precio
          self.tipo=tipo
          self.color=color
          self.peso=peso
          self.horas_de_uso= 0
          self.consumo_energetico= consumo_energetico

      def tipo_de_electrodomestico(self):
          self.tipo

      def caracteristica(self):
          print (self.color, self.tipo, self.peso, self.precio)

      def usar(self,use):
          self.horas_de_uso +=  use

      def costo_hasta_ahora(self,gastado):
          gaste= self.horas_de_uso * gastado
          consumo= self.horas_de_uso * self.consumo_energetico
          print (gaste,consumo)

#como lo ejecute en la terminal
con_electr=Electrodomestico(200,'horno_electrico','negro',4000,0,100) 

print(con_electr.tipo)                                                
horno_electrico

con_electr.caracteristica()                                           
negro horno_electrico 4000 200

con_electr.usar(3) 

con_electr.usar(54) 

print (con_electr.horas_de_uso)
57

con_electr.costo_hasta_ahora(20)                                      
1140 5700





