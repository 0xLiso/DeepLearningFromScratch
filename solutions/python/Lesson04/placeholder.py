from graph import Node
from tensor import Tensor



class Placeholder(Node):
	def __init__(self, Name: str = None):
		super().__init__()
		if Name is not None:
			self.name = Name
		self.value=None

	def set_value(self,initial_value:Tensor):
		self.value = initial_value

	def forward(self):
		self.output = self.value
