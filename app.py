import pymysql
from flask import Flask , render_template, request, redirect
from data import Articles


app = Flask(__name__)

app.debug = True # 내폴더구조가 모두보임 기본값은 false false로 해놓으면 안보임

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)

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
    # articles = Articles()
    # print(articles[0]['title'])
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall() # 튜플 가로 두개라 for문 필수
    print(topics)
    return render_template("articles.html", articles=topics)

@app.route('/article/<int:id>') #params
def article(id):
    # articles = Articles()
    # article = articles[id - 1]
    # print(articles[id - 1])
    cursor = db.cursor()
    sql = 'SELECT * FROM topic where id = {};'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods=['GET', 'POST'])
def add_articles():
    cursor = db.cursor()
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc, author]

        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        return redirect('/articles')
    
    else:
        return render_template('add_articles.html')

@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    cursor = db.cursor()
    # sql = "DELETE FROM topic WHERE id = %s;" #format쓰면 밑에 2줄 id 필요없음
    # id = [id]
    # cursor.execute(sql , id)
    sql = 'DELETE FROM topic WHERE id = {};'.format(id)
    cursor.execute(sql)
    db.commit()

    return redirect('/articles')

@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        return "Success"
    
    else:
        return render_template('edit_article.html')

if __name__ == "__main__": # 처음 서버 띄울때
    app.run() # http://localhost:5000/ default