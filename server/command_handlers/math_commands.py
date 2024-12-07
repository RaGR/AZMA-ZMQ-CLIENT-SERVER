import logging
import ast
import operator
import math
from . import CommandHandler

class MathCommandHandler(CommandHandler):
    def __init__(self):
        self.operations = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.USub: operator.neg,
        }

    async def handle(self, request):
        try:
            expression = request['expression']
            logging.info(f"Evaluating math expression: {expression}")
            
            result = self.evaluate(ast.parse(expression, mode='eval').body)
            logging.info(f"Math result: {result}")
            
            return str(result)
        
        except Exception as e:
            error_msg = f"Error evaluating math expression: {str(e)}"
            logging.error(error_msg)
            return error_msg

    def evaluate(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return self.operations[type(node.op)](
                self.evaluate(node.left),
                self.evaluate(node.right)
            )
        elif isinstance(node, ast.UnaryOp):
            return self.operations[type(node.op)](self.evaluate(node.operand))
        elif isinstance(node, ast.Call):
            if node.func.id == 'pow':
                return math.pow(
                    self.evaluate(node.args[0]),
                    self.evaluate(node.args[1])
                )
            else:
                return getattr(math, node.func.id)(
                    *(self.evaluate(arg) for arg in node.args)
                )
        else:
            raise ValueError(f"Unsupported operation: {node}")

