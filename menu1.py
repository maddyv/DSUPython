class menu:
    def __init__(self):
        self.names=[]
        self.price=[]
    def add(self,str, pr):
        self.names.append(str)
        self.price.append(pr)
    def show(self):
        print("Item Name     Price")
        for i in range(len(self.names)):
            print(self.names[i],"         ",self.price[i])
m=menu()
m.add("idly",10)
m.add("vada",20)
m.show() 
