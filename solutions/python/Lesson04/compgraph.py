#import graph 
from graph import Graph,Node
#import all operations
from tensor import Tensor
from variable import Variable
from placeholder import Placeholder
from operations import *


class Compgraph(object):
	name = "unnamed"
	graph = None
	nvariables = 0
	nplaceholders = 0
	nops = 0
	def __init__(self,name:str="anonymous"):
		self.name = name
		if not self.graph:
			self.graph=Graph()

	def to_dot(self):
		return self.graph.to_dot()
	def add_operation(self,op:Operation):
		if not op.name:
			op.set_name("{}_{}".format(op.base_name,self.nops))
		self.graph.add_node(op)
		self.nops+=1
		for input in op.inputs :
			self.graph.add_edge(input,op)
		return op
	def add_placeholder(self,ph:Placeholder) -> Placeholder:
		if not ph.name:
			ph.set_name("Placeholder_{}".format(self.nplaceholders))
		self.graph.add_node(ph)
		self.nplaceholders += 1
		return ph
	def add_variable(self,v:Variable) -> Variable:
		if not v.name:
			v.set_name("Variable_{}".format(self.nvariables))
		self.graph.add_node(v)
		self.nvariables += 1
		return v
	def run(self,toNode:Node) -> Tensor:
		order = self.graph.reverse_bfs(toNode)
		for node in order:
			node.forward()

		return toNode.output
