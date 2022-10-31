#Restful API 其實就是開放一個 EndPoit 的網路接口給其他人使用，並將要做的事情封裝在該接口內，不需要知道真實運作狀況，只要得到答案即可

#载入flask 套件
from flask  import Flask

# 创建Flask app对象
app = Flask(__name__)

# 建立根目錄路由，並輸出文字
@app.route("/")
def hello():
    return "<h1>Hello , This a Restful Api Server by Flask...</h1>"

# 創建 output 输出內容
output = [
    {
        "pid": "1",
        "tittle": "Example01",
        "price": 10,
        "img":  "https://picsum.photos/id/999/1200/600",
        "isAvailable": True
    },
    {
        "id": "2",
        "title": "Example02",
        "price": 60,
        "img": "https://picsum.photos/id/1070/1200/600",
        "isAvailable": True
    }
]

# 建立products路由，回传 output，及狀態 200
@app.route("/products")
def products():
    return {"products": {"Message": "Get all products..", "output": output}},200



if  __name__ == "__main__":
# Port 監聽30880，並啟動除錯模式。
    app.run(port=30880,debug=True)