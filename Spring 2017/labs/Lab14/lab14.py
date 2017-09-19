class vector(object):
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def __str__(self):
		return str(round(self.x,2))+","+str(round(self.y,2))

	def __repr__(self):
		return str(x)+','+str(y)

	def __add__(self,v):
		return(vector(self.x+v.x,self.y+v.y))
	def __sub__(self,v):
		return(vector(self.x-v.x,self.y-v.y))
	def __mul__(self,f):
		try:
			return (vector(self.x*f.x,self.y*f.y))
		except AttributeError:
			return(vector(self.x*f,self.y*f))
	def __rmul__(self,v):
		try:
			return(vector(self.x*v.x,self.y*y))
		except AttributeError:
			return(vector(self.x*v,self.y*v))
	def __eq__(self,v):
		return (v.x==self.x and v.y==self.y)
	def magnitude(self):
		return((self.x**2 +self.y**2)**.5)
	def unit(self):
		m=self.magnitude()
		if m==0:
			raise ValueError("Cannot convert zero vector to a unit vector")
		else:return(vector((self.x)/m,(self.y)/m))

def main():
	v1=vector(.3,.052)
	v2=vector(1.2,2.4)
	v3=vector(35.4,86.7)
	v4=vector(35.4,86.7)
	v5=vector()
	print(v1+v2)
	print(v1-v2)
	print(v1*2)
	print(2*v1)
	print(v1*v2)
	print(v1==v2)
	print(v3==v4)
	print(v1.magnitude())
	print(v1.unit())
	print(v5.unit())

if __name__ == "__main__":
    main()