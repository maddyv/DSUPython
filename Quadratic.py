import cmath
class Quadratic:
    def __init__(self,ac,bc,cc,dcr):
        self.ac=0
        self.bc=0
        self.cc=0
        self.dcr=0.1
        self.rt1=0
        self.rt2=0
        self.rtz=0
        complex(self.rtz)
    def input(self):
        self.ac=int(input("Enter co-efficient a"))
        self.bc=int(input("Enter co-efficient b"))
        self.cc=int(input("Enter co-efficient c"))
    def compute(self):            
            self.dcr=(self.bc*self.bc)-(4*self.ac*self.cc)
            if self.dcr==0.0:
                self.rt1=-((self.bc)/(2.0*(self.ac)))
            elif self.dcr>0.0:
                self.rt1=(-self.bc +cmath.sqrt(self.dcr))/(2.0*(self.ac))
                self.rt2=(-self.bc-cmath.sqrt(self.dcr))/(2.0*(self.ac))
            else:
                self.rtz=complex(-(self.bc/(2.0*(self.ac))),cmath.sqrt(-self.dcr)/(2*(self.ac)))
    def output(self):
        if self.dcr==0.0:
            print("There is one root and it is "+str(self.rt1)+"\r")
        elif self.dcr>0.0:
            print("There are two real roots i.e. "+str(self.rt1)+" and "+str(self.rt2))
        else:
            print("There are two complex roots i.e. {} + {}i and {} - {}i".format(self.rtz.real,self.rtz.imag,self.rtz.real,self.rtz.imag))   
def main():
    a=0
    b=0
    c=0
    dcrm=0
    float(a)
    float(b)
    float(c)
    float(dcrm)
    obj=Quadratic(a,b,c,dcrm)
    obj.input()
    obj.compute()
    obj.output()
main()
