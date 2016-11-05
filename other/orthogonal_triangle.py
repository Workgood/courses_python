'''
Checks if triangle is orthogonal.

Args:
cath1,2: cathetuses of the suppositional orthogonal triangle
hyp: hypotenuse.

Returns:
msg: Orthogonal or not.

'''
def isOrthogonal(cath1,cath2,hyp):
    if hyp == cath1 +cath2:
        return "Triangle is orthogonal"
    else:
        return "Triangle isn't orthogonal"



class Point:
    def __init__(self,x,y):
        self.xcoord = x
        self.ycoord = y

x1 = int(input("Enter coords of 3 points on a coordinate plane x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))

a = Point(x1,y1)
b = Point(x2,y2)
c = Point(x3,y3)


ab = (a.xcoord - b.xcoord)**2 + (a.ycoord-b.ycoord)**2
bc = (b.xcoord - c.xcoord)**2 + (b.ycoord-c.ycoord)**2  # we take squares of 
ac = (a.xcoord - c.xcoord)**2 + (a.ycoord-c.ycoord)**2  # sides to avoid errors in extraction 

cathetuses = [ab,bc,ac]
hypotenuse = max(cathetuses)
cathetuses.remove(hypotenuse)

if hypotenuse <= sum(cathetuses):
    print(isOrthogonal(cathetuses[0],cathetuses[1],hypotenuse))
else:
    print("Points dont form triangle!")
