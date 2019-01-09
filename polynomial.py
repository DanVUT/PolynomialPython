import types

class Polynomial:
    '''Inicializacia pola, osetrenie args a kwargs'''
    def __init__(self, *arg, **kwargs):
        if kwargs == {}:
            self.number=(arg)
            if type(self.number[0]) is list:
                self.number=self.number[0]
            else:
                self.number=[]
                for element in arg:
                    self.number.append(element)
        else:
            self.number=[]
            list1=[]
            list2=[]
            for i in kwargs:
                list1.append(i)
            list1.sort()
            list1.reverse()
            for i in range(int(list1[0][1]),-1,-1):
                list2.append("x{0}".format(i))
            for elm in list2:
                try:
                    self.number.append(kwargs[elm])
                except:
                    self.number.append(0)
            self.number.reverse()
    '''Vytvorenie a vratenie polynomu'''
    def __str__(self):
        for elm in self.number:
            if type(elm) is not int:
                return "Zle zadane argumenty"
        polynom=""
        x=""
        index=""
        for i in range(len(self.number)-1,1,-1):
            if self.number!=0:
                if self.number[i]==1:
                    x=str("+ x")
                    index=str("{0} ".format(i))
                elif self.number[i]>0:
                    x=str("+ {0}x".format(self.number[i]))
                    index=str("{0} ".format(i))
                    
                if self.number[i]==-1:
                    x=str("- x")
                    index=str("{0} ".format(i))
                    
                elif self.number[i]<0:
                    x=str("- {0}x".format(abs(self.number[i])))
                    index=str("{0} ".format(i))
            if x!="":         
                polynom+=x
                polynom+="^"
                polynom+=index
            x=""
            index=""

        x=""
        index=""
        if len(self.number)>=2:
            if self.number[1] != 0:
                if self.number[1]==1:
                    x=str("+ x ")
                elif self.number[1]>0:
                    x=str("+ {0}x ".format(self.number[1]))
                if self.number[1]==-1:
                    x=str("- x ")
                elif self.number[1]<0:
                    x=str("- {0}x ".format(abs(self.number[1])))
                if x!="": 
                    polynom+=x
        x=""
        index=""
        if len(self.number)>=1:
            if self.number[0] != 0:
                if self.number[0]>0:
                    x=str("+ {0}".format(self.number[0]))
                if self.number[0]<0:
                    x=str("- {0}".format(abs(self.number[0])))
                if x!="":
                    polynom+=x
        if polynom != "":
            if polynom[0]=="+" and polynom[1]==" ":
                polynom = polynom[:0] + polynom[1:]
                polynom = polynom[:0] + polynom[1:]
        return polynom
    '''Odcitanie vysledkov dvoch polynomov'''
    def at_value(self,*arg):
        values=[]
        result=[]

        for i in arg:
            values.append(i)

        if len(arg)==1 or len(arg)==2:
            for value in values:
                tmp=0
                for index in range(len(self.number)-1,-1,-1):
                    if index!=0:
                        tmp+=(self.number[index])*(value**index)
                    else:
                        tmp+=self.number[index]
                result.append(tmp)
        else:
            return("Zly pocet argumentov")
        if len(result)==1:
            return (result[0])
        else:
            return (result[1]-result[0])
    '''Vytvorenie prvkov po zderivovani'''
    def derivative(self):
        self.derivate=[]
        for i in range(len(self.number)-1,0,-1):
            self.derivate.append(self.number[i]*i)
        self.derivate.reverse()
        return Polynomial(self.derivate)
    '''Scitanie dvoch polynomov'''
    def __add__(self,other):
        if len(self.number)>len(other.number):
            for i in range(len(self.number)-len(other.number)):
                other.number.append(0)
        if len(self.number)<len(other.number):
            for j in range(len(other.number)-len(self.number)):
                self.number.append(0)
        for k in range(len(self.number)):
            self.number[k]+=other.number[k]
        return Polynomial(self.number)
    '''Umocnenie polynomu'''
    def __pow__(self,power):
        self.power=self.number
        
        for i in range(power-1):
            tmp=[]
            for j in range(len(self.power) + len(self.number)-1):
                tmp.append(0)
            for k in range(len(self.power)):
                for l in range(len(self.number)):
                    tmp[k+l]+=self.power[k]*self.number[l]
            self.power=tmp
        return Polynomial(self.power)



