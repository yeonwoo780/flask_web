import pymysql
from flask import Flask , render_template, request, redirect
from data import Articles 
from passlib.hash import sha256_crypt

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
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall() # 튜플 가로 두개라 for문 필수
    # print(topics)
    # articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles=topics)

@app.route('/article/<int:id>') #params
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic where id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone() # 튜플 가로 하나 for문 안써줘도 됨
    # print(topic)
    # articles = Articles()
    # article = articles[id - 1]
    # print(articles[id - 1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods=["GET","POST"])
def add_articles():
    cursor = db.cursor()
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc, author ]
        # print(author, title, desc)

        cursor.execute(sql, input_data)
        db.commit()
        # print(cursor.rowcount)
        # db.close()
        return redirect('/articles')
    
    else:
        # return "<h1>글쓰기 페이지</h1>"
        return render_template('add_articles.html')
    
@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    cursor = db.cursor()
    # sql = "DELETE FROM topic WHERE id = %s;" #format쓰면 밑에 2줄 id 필요없음
    # id = [id]
    # cursor.execute(sql , id)
    sql = "DELETE FROM topic WHERE id = {};".format(id)
    cursor.execute(sql)
    db.commit()

    return redirect('/articles')


@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit(id):
    cursor = db.cursor()
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        author = request.form['author']
        
        sql = "UPDATE topic SET title = %s, body = %s, author = %s WHERE id = {};".format(id)
        input_data = [title, desc, author]
        cursor.execute(sql, input_data)
        db.commit()
        print(request.form['title'])

        return redirect('/articles')
    
    else:
        sql = "SELECT * FROM topic WHERE id = {}".format(id)
        cursor.execute(sql)
        topic = cursor.fetchone()
        # print(topic,'\n')

        # print(topic[1])
        return render_template("edit_article.html", article = topic)


@app.route('/register', methods=["POST","GET"])
def register():
    cursor = db.cursor()
    if request.method == "POST":
        
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        # userpw = (request.form['userpw'])
        userpw = sha256_crypt.encrypt(request.form['userpw'])
        sql = "INSERT INTO users (name, email, username, password) VALUES (%s, %s, %s, %s);"
        input_data = [name, email, username, userpw]
        cursor.execute(sql, input_data)
        db.commit()
        return redirect('/')

    else:
        return render_template("register.html")


@app.route('/login', methods = ["GET", "POST"])
def login():
    cursor = db.cursor()
    if request.method == "POST":
        usersname = request.form['username']
        userpw_1 = request.form['userpw']
        # print(request.form['username'])
        # print(userpw_1)
        
        sql = 'SELECT password FROM users WHERE email = %s;'
        input_data = [usersname]
        cursor.execute(sql, input_data)
        userpw = cursor.fetchone()
        # print(userpw[0])#cursor.fetchone()[0]
        print(userpw[0])
        if sha256_crypt.verify(userpw_1, userpw[0]):
            return "Success"
        else:
            return userpw[0]
           


if __name__ == "__main__": # 처음 서버 띄울때
    app.run() # http://localhost:5000/ default
