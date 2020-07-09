import numpy as np

from tensor import Tensor
from graph import Node

class Operation(Node):
	base_name:str=None
	output:Tensor = None
	inputs:list = []
	def __init__(self):
		super().__init__()
		self.inputs=[]
		self.output=None

	def forward(self):
		raise NotImplementedError
	def backward(self, gradOutput: Tensor):
		raise NotImplementedError


class Negative(Operation):
	base_name="Negative"
	def __init__(self, A: Node, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
			
		self.inputs.append(A)
		

	def forward(self):
		A = self.inputs[0]
		self.output = -A.output


class Add(Operation):
	base_name = "Add"
	def __init__(self, A: Node,B:Node, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
		self.inputs.append(A)
		self.inputs.append(B)

	def forward(self):
		A = self.inputs[0]
		B = self.inputs[1]
		self.output = A.output + B.output


class Substract(Operation):
	base_name = "Substract"
	def __init__(self, A: Node,B:Node, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
			
		self.inputs.append(A)
		self.inputs.append(B)

	def forward(self):
		A = self.inputs[0]
		B = self.inputs[1]
		self.output = A.output - B.output

class Divide(Operation):
	base_name = "Divide"
	def __init__(self, A: Node,B:Node, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
			
		self.inputs.append(A)
		self.inputs.append(B)

	def forward(self):
		A = self.inputs[0]
		B = self.inputs[1]
		self.output = A.output/B.output


class Multiply(Operation):
	base_name = "Multiply"
	def __init__(self, A: Node,B:Node, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
		self.inputs.append(A)
		self.inputs.append(B)
	def forward(self):
		A = self.inputs[0]
		B = self.inputs[1]
		self.output = A.output * B.output


class Sum(Operation):
	base_name = "Sum"
	def __init__(self, A: Node,axis:int = -1, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
			
		self.inputs.append(A)
		self.axis = axis

	def forward(self):
		A = self.inputs[0]
		self.output = np.sum(A.output,self.axis)

class MatMul(Operation):
	base_name = "MatMul"
	def __init__(self, A: Node, B:Node, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
			
		self.inputs.append(A)
		self.inputs.append(B)

	def forward(self):
		A = self.inputs[0]
		B = self.inputs[1]
		self.output = np.matmul( A.output , B.output )



class MatMulNaive(Operation):
	base_name = "MatMulNaive"
	def __init__(self, A: Node,B:Node, Name:str=None):
		super().__init__()
		if Name is not None:
			self.name = Name
			
		self.inputs.append(A)
		self.inputs.append(B)

	def forward(self):
		A = self.inputs[0]
		B = self.inputs[1]
		cshape=(A.shape[0],B.shape[1])
		C=Tensor([x for x in range(np.prod(cshape))]).reshape(cshape)
		for i in range(0, A.shape[0]):
			for j in range(0, B.shape[1]):
				C[i,j]=0
				for k in range(0, A.shape[1]):
					C[i,j]+= A[i,k]*B[k,j]
		self.output = C


class sin(Operation):
	base_name = "Sin"

	def __init__(self, A: Node, Name: str = None):
		super().__init__()
		if Name is not None:
			self.name = Name

		self.inputs.append(A)

	def forward(self):
		A = self.inputs[0]
		self.output = np.sin(A.output)

