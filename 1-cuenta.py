class cuenta():
     def __init__(self,titular,cantidad=0):
         self.titular=titular
         self.cantidad=cantidad

     def ingresar(self,ingr_plata):
         if ingr_plata > 0:
            self.cantidad= ingr_plata

     def retirar(self,ret_cantidad):
         cuen_actual=self.cantidad - ret_cantidad
         if cuen_actual < 0:
             self.cantidad= 0
         else:
             self.cantidad=cuen_actual




cuentajoni=cuenta('jonii',100)                                          

print(cuentajoni.cantidad)                                              
100

cuentajoni.ingresar(12500)                                             

print(cuentajoni.cantidad)                                             
12500

cuentajoni.retirar(2000)                                               

print(cuentajoni.cantidad)                                             
10500

print(cuentajoni.titular)  
