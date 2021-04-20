import pymysql

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)

# cursor = db.cursor()
# db.commit()
# cursor.execute('SELECT * FROM users;')
# users = cursor.fetchall() 
# print(users)

sql = '''
    CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
# cursor = db.cursor()
# cursor.execute(sql)
# db.commit()
# users = cursor.fetchall() 
# print(users)

sql_1 = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봤네ㅠㅠ', '정연우');"

# cursor = db.cursor()
# cursor.execute(sql_1)
# db.commit()
# users = cursor.fetchall()
# print(users)

sql_2 = "INSERT INTO `busan`.`users` (`name`, `email`, `username`, `password`) VALUES ('Jung', 'dbfltkdwk64@naver.com', 'Jung', '12345');"

# cursor = db.cursor()
# cursor.execute(sql_2)
# db.commit()

# cursor.execute('SELECT * FROM busan.users;')
# users = cursor.fetchall()
# print(users)

sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
cursor = db.cursor()
title = input('제목을 적으세요 : ')
body = input('내용을 적으세요 : ')
author = input('저자를 적으세요 : ')

input_data = [title, body, author ]
cursor.execute(sql_3,input_data)
db.commit()
cursor.execute('SELECT * FROM topic;')
users = cursor.fetchall()
print(cursor.rowcount, users)