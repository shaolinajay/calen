class A:
	def __init__(self,l):
		self.l=l
	def display(self):
		print(self.l)
	def double(self):
		self.q=[]
		for i in self.l:
			self.q.append(i*2)
		self.l=self.q
		return self
ob=A([2,3,4])
ob.double().display()
		