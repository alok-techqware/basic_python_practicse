class Circle:
    pi=3.14
    #set default radius=1 next we change it
    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    #assigign radius new value
    def setRadius(self,new_radius):
        self.radius=new_radius
        self.area=new_radius*new_radius*self.pi
    
    #calculate circumference
    def getCircumference(self):
        return self.radius*self.pi*2
    
c=Circle()
print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

#let assign our desired radius
c.setRadius(2)
print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
