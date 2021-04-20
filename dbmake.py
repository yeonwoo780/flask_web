import pymysql

db = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1234',
    db = 'busan'
)

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
# cursor.execute(sql)
# cursor.execute('SELECT * FROM users;')   #sql 쿼리문 날림

# sql_1 = "INSERT INTO `busan`.`topic` (`title`, `body`, `author`) VALUES ('부산', '부산와서 갈매기를 못봤네ㅠㅠ', '김태경');"

# cursor = db.cursor()    #sql 쿼리문 쓰기위한 준비
# cursor.execute(sql_1)
# db.commit() #apply
# db.close()  #commit quit
# cursor.execute('SELECT * FROM topic;')


# sql_2 = "INSERT INTO `busan`.`users` (`name`, `email`, `username`, `password`) VALUES ('JUNG', 'dbfltkdwk64@naver.com', 'JUNG', '12345');"
# cursor = db.cursor() 

# cursor.execute(sql_2)
# db.commit() #apply
# db.close()  #commit quit

# cursor.execute('SELECT * FROM users;')   #sql 쿼리문 날림
# users = cursor.fetchall()   # 조회한걸 다 가져와줌
# print(users)

sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
cursor = db.cursor()
title = input('제목을 적으세요')
body = input("내용을 적으세요")
author = input("누구세요?")
input_data = [title,body,author ]
cursor.execute(sql_3,input_data)
db.commit()
# db.close()
cursor.execute('SELECT * FROM topic;')
users = cursor.fetchall()
print(cursor.rowcount, users)

