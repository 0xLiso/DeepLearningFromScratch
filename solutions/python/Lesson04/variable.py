from graph import Node
from tensor import Tensor


class Variable(Node):
	def __init__(self,initial_value:Tensor, Name: str = None):
		super().__init__()
		if Name is not None:
			self.name = Name
		self.value = initial_value
	def forward(self):
		self.output = self.value