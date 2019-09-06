def sitri(a,b,c):
    if a == b and b == c:
        x = 'tres lados iguales'
        return x 

def tri_tresdist(a,b,c):
    if a < b+c and b < a+c and c < a+b :
    	 if a != b and b!=c and c!=a :
        	x = 'son distintos'
        	return x

def tri_dosigual(a,b,c):
    if a < b+c and b < a+c and c < a+b:
         if a == b != c or b == c != a or a == c != b:
                x = 'dos lados iguales'
                return x

def notri(a,b,c):
    if a < b+c and b < a+c and c < a+b:
         if a == b != c or a == c !=b or b == c !=a:
               	x = 'no triangulo'
                return x 


