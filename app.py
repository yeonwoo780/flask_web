from flask import Flask , render_template
from data import Articles


app = Flask(__name__)

app.debug = True # 내폴더구조가 모두보임 기본값은 false false로 해놓으면 안보임

@app.route('/', methods=['GET']) 
# http://localhost:5000/data
#methods=['GET'] get쓸때는 생략가능 default값
def index():
    # return "Hello World"
    return render_template("index.html", data="KIM")
    #render_template 는 html문서로 바꿔줌

@app.route('/about')
def about():
    return render_template("about.html", hello="Gary Kim")

@app.route('/articles')
def articles():
    articles = Articles()
    #print(articles[0]['title'])
    return render_template("articles.html", articles=articles)

if __name__ == "__main__": # 처음 서버 띄울때
    app.run() # http://localhost:5000/ default
