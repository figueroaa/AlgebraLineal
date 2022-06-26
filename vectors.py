from decimal import *
import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            getcontext().prec = 4
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('Las cordenadas no deben estar vacias')

        except TypeError:
            raise TypeError('Las coorenadas tienen que ser un iterable')


    def __str__(self):
        return '{}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
# Comprobación de si un vector es el vector nulo
    def isnull(self):
        f = Decimal(0)
        for x in self.coordinates:
            f = f + Decimal(x)
        return( f == Decimal(0))
# Módulo del vector
    def size(self):
        f = Decimal(0)
        for x in self.coordinates:
            f = f + Decimal(x**2)
        f = math.sqrt( f )
        return f
# Añadir un vector
    def addv(self,other ):
        i = int(0)
        myarray = []
        for x in self.coordinates:
            myarray.append( Decimal(x) )
        for x in other.coordinates:
            myarray[i] = myarray[i] + Decimal(x)
            i = i + 1

        return Vector( myarray )

# Restar un vector
    def subv(self,other):
        lv = other.xk(-1)
        return self.addv( lv )

# Obtener el vector director de uno dado
    def direc(self):
        if self.isnull():
            myvector = self
        else:
            myarray = []
            cx      = Decimal( 0 )
            mysize  = self.size( )
            for x in self.coordinates:
                cx = Decimal(x)
                cx = cx / Decimal(mysize)
                myarray.append( cx )
            myvector = Vector( myarray )

        return myvector
# Multiplicar por un vector
    def xk(self,scalar):

        myarray = []
        for x in self.coordinates:
            myarray.append( Decimal( x ) * Decimal( scalar ) )
        return Vector( myarray )
# Producto interno o producto escalar
    def xinterno(self,other):
        i = int(0)
        myarray = []
        res = Decimal(0)
        for x in self.coordinates:
            myarray.append(Decimal(x))
        for x in other.coordinates:
            res = res + ( myarray[i] * Decimal(x) )
            i = i + 1
        return res
# Producto vectorial
    def xvectorial(self,other):
        cs = []
        co = []
        cn = []
        for x in self.coordinates:
            cs.append(x)
        for x in other.coordinates:
            co.append(x)
        cn.append(  Decimal(cs[1])*Decimal(co[2]) - Decimal(cs[2])*Decimal(co[1]) )
        cn.append(  Decimal(cs[2])*Decimal(co[0]) - Decimal(cs[0])*Decimal(co[2]) )
        cn.append(  Decimal(cs[0])*Decimal(co[1]) - Decimal(cs[1])*Decimal(co[0]) )
        return( Vector( cn ))

# Ángulo con otro vector
    def ang(self,other,opt):
        res = Decimal( 0 )
        mod = self.size() * other.size()
        if mod != 0:
            res = self.xinterno(other)
            res = res / Decimal( self.size() )
            res = res / Decimal( other.size() )
            res = math.acos(res)
            if opt == "d":
                res = Decimal( res * 180) / Decimal(math.pi)
        return res
# Proyección sobre un vector
    def project(self,other):
        u     = other.direc()
        lp    = u.xinterno(self)
        return( kxv(lp,u))

# Complemento ortoganal sobre un vector
    def ortogon(self,other):
        u     = other.direc()
        vl    = self.project(u)
        return( self.subv(vl))


def setprec(decleng):
    getcontext().prec = decleng
def sumav(u,v):
    return( u.addv(v))
def restav(u,v):
    return( u.subv(v))
def xvectorial(u,v):
    return( u.xvectorial(v))
def xinterno(u,v):
    return( u.xinterno(v))
def kxv(k,v):
    return( v.xk(k))
def angulo(u,v,opt):
    return(u.ang(v,opt))
def check():
    u = Vector([4.05,1,1])
    v = Vector([4.019,2,-1])
    k = 3.2
    print(u)
    print(v)
    print(k)
    print('Suma  vectorial   :')
    print(sumav(u,v))
    print('Resta vectorial   :')
    print(restav(u,v))
    print('Producto escalar  :')
    print(kxv(k,u))
    print(kxv(k,v))
    print(kxv(7,v))
    print('Producto vectorial:')
    print(xvectorial(u,v))
    print('Producto interno  :')
    print(xinterno(u,v))

def help():
    print("MÓDULO ALGEBRA")
