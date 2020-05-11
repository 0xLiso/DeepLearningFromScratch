import numpy as np

from Tensor import Tensor


class Operation:
	result = None
	def forward(self):
		raise NotImplementedError
	def backward(self, gradOutput: Tensor):
		raise NotImplementedError


class Negative(Operation):
	def __init__(self, A: Tensor,B:Tensor):
		self.A = A
		

	def forward(self):
		self.result = -self.A 


class Add(Operation):
	def __init__(self, A: Tensor,B:Tensor):
		self.A = A
		self.B = B

	def forward(self):
		self.result = self.A + self.B


class Substract(Operation):
	def __init__(self, A: Tensor,B:Tensor):
		self.A = A
		self.B = B

	def forward(self):
		self.result = self.A - self.B

class Divide(Operation):
	def __init__(self, A: Tensor,B:Tensor):
		self.A = A
		self.B = B
	def forward(self):
		self.result = self.A/self.B


class Multiply(Operation):
	def __init__(self, A: Tensor,B:Tensor):
		self.A = A
		self.B = B
	def forward(self):
		self.result = self.A * self.B


class Sum(Operation):
	def __init__(self, A: Tensor,axis:int = -1):
		self.A = A
		self.axis = axis

	def forward(self):
		self.result = np.sum(self.A,self.axis)

class MatMul(Operation):
	def __init__(self, A: Tensor,B:Tensor):
		self.A = A
		self.B = B

	def forward(self):
		self.result = np.matmul( self.A , self.B )



class MatMulNaive(Operation):
	def __init__(self, A: Tensor,B:Tensor):
		self.A = A
		self.B = B

	def forward(self):
		cshape=(self.A.shape[0],self.B.shape[1])
		C=Tensor([x for x in range(np.prod(cshape))]).reshape(cshape)
		for i in range(0, self.A.shape[0]):
			for j in range(0, self.B.shape[1]):
				C[i,j]=0
				for k in range(0,self.A.shape[1]):
					C[i,j]+=self.A[i,k]*self.B[k,j]
		self.result = C













