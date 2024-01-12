#Adding Numbers Using Class
class details:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        print(self.x + self.y)

list = []
list.append(details(1,2))
list.append(details(3,4))
list.append(details(5,10)) 

for i in list:
    i.sum()

print('\n')
        