from decimal import *
import math

class Vector(object):

    def __init__(self, coordinates):
        try:
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

    def isnull(self):
        f = float(0)
        for x in self:
            f = f + x
        return( f == 0 )
    def size(self):
        f = 0
        for x in self.coordinates:
            f = f + x**2
        f = math.sqrt( f )
        return f

    def addv(self,other ):
        i = int(0)
        myarray = []
        for x in self.coordinates:
            myarray.append( x )
        for x in other.coordinates:
            myarray[i] = myarray[i] + x
            i = i + 1
        return Vector( myarray )

    def subv(self,other ):
        lv = other.sprod(-1)
        return self.addv( lv )

    def direc(self):
        if self.isnull():
            myvector = self
        else:
            myarray = []
            cx      = Decimal( 0 )
            mysze   = Decimal( 0 )
            mysize  = self.size( )
            for x in self.coordinates:
                cx = x
                cx = cx / mysize
                myarray.append( cx )
            myvector = Vector( myarray )

        return myvector

    def sprod(self,scalar):

        myarray = []
        for x in self.coordinates:
            myarray.append( x * scalar )
        return Vector( myarray )

    def inner(self,other):
        i = int(0)
        myarray = []
        res = float(0)
        for x in self.coordinates:
            myarray.append(x)
        for x in other.coordinates:
            res = res + ( myarray[i] * x )
            i = i + 1
        return res

    def vectx(self,other):
        cs = []
        co = []
        cn = []
        for x in self.coordinates:
            cs.append(x)
        for x in other.coordinates:
            co.append(x)
        cn.append(  cs[1]*co[2] - cs[2]*co[1] )
        cn.append(  cs[2]*co[0] - cs[0]*co[2] )
        cn.append(  cs[0]*co[1] - cs[1]*co[0] )
        return( Vector( cn ))

    def angle(self,other,opt):
        res = float( 0 )
        mod = self.size() * oher.size()
        if mod != 0:
            res = self.inner(other)
            res = res / self.size()
            res = res / other.size()
            res = math.acos(res)
            if opt == "d":
                res = res * 180 / math.pi
        return res

    def isortog(self,other):
        res = float( 0 )
        res = self.inner(other)
        return ( res == 0 )

    def isparal(self,other):
        res = float( 0 )
        res = self.inner(other)
        return ( res == self.size() * other.size() )

    def project(self,other):
        u     = other.direc()
        lp    = u.inner(self)
        return( sprod(lp,u))

    def getortog(self,other):
        u     = other.direc()
        vl    = self.project(u)
        return( self.subv(vl))



def sumav(u,v):
    return( u.addv(v))
def restav(u,v):
    return( u.subv(v))
def xvectorial(u,v):
    return( u.vectx(v))
def xinterno(u,v):
    return( u.inner(v))
def xscalar(k,v):
    return( v.sprod(k))
def check():
    u = Vector([1,1,1])
    v = Vector([1,2,-1])
    k = 3.2
    print(u)
    print(v)
    print(k)
    print('Suma  vectorial   :')
    print(sumav(u,v))
    print('Resta vectorial   :')
    print(restav(u,v))
    print('Producto escalar  :')
    print(xscalar(k,u))
    print(xscalar(k,v))
    print('Producto vectorial:')
    print(xvectorial(u,v))
    print('Producto interno  :')
    print(xinterno(u,v))
def help()
    print("MÓDULO ALGEBRA")
