import zipapp

#
# class FlaskBother():
#     def __init__(self):
#         self.routes={}
#     def route(self,route_str):
#         def decorator(f):
#             self.routes[route_str] = f
#             print(self.routes)
#             return f
#         return decorator
#     def server(self,path):
#         view_function = self.routes.get(path)
#         if view_function:
#             return view_function()
#         else:
#             raise ValueError('Route "{}" has not been registered'.format(path))
#
# app = FlaskBother()
#
# @app.route('/')
# def hello():
#     return "Hello World!!"

# if __name__ == '__main__':
#     hello()
#     print(app.server("/"))

