from flask import Flask,g
from flask_restful import reqparse,Api,Resource
from flask_httpauth import HTTPTokenAuth

#flask相关变量声明
app = Flask(__name__)
api = Api(app)

#RESTfulAPI的参数解析 -- put / post参数解析

parser_put = reqparse.RequestParser()
parser_put.add_argument("keyword",type=str,required=True,help="need user data")
parser_put.add_argument("lv",type=str,required=True,help="need user passwd")

# 功能方法部分案例
def to_do(arg1, args2):
    return str(arg1) + str(args2)

# 操作（post / get）资源列表
class TodoList(Resource):
    def post(self):
        args = parser_put.parse_args()

        #构建新参数
        keyword = args['keyword']
        lv = args['lv']
        info = {"info": to_do(keyword,lv)}
        return info, 201

# 设置路由，即路由地址为http://127.0.0.1:5000/users
api.add_resource(TodoList,"/users")

if __name__ == "__main__":
    app.run(debug=True)



















