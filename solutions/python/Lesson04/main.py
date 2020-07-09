from compgraph import Compgraph

from placeholder import Placeholder
from variable import Variable
import operations as op
from tensor import Tensor


if __name__ == '__main__':
    #nuestros tensores para las variables de entrada y el placeholder
    X = Tensor([x for x in range(0,10)]).reshape((10))
    dos = Tensor(2)

    c = Compgraph()
    v_1=c.add_variable(Variable(dos,"DOS"))
    x_1=c.add_placeholder(Placeholder("X"))
    o_1=c.add_operation(op.sin(x_1))
    e_1=c.add_operation(op.Multiply(o_1,v_1))

    print(c.to_dot())
    x_1.set_value(X)
    res = c.run(e_1)
    print(res)
    exit(0)
