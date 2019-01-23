from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#flask
#플라스크 서버를 사용하기 위한 기초적인 설정
app = Flask(__name__)

#SQLAlchemy를 사용하기 위한 설정
#키값은 대문자로 써야함.
#어떠한 데이터베이스를 사용할건지? 파일이름을 가리키고 있음. ///는 3개 들어감.
#sql알케미 라이브러리를 쓰면, 파이썬 코드를 통해 테이블 작성등을 할 수 있음.
#파이썬 코드는 쉽게 변경이 될 수 있음. TRACK_MODIFICATION: 자동으로 수정을 반영하는 부분을 끄고,
#테이블 수정, 스키마 변경등은 우리가 추후에 변경을 했다 등의 내용을 입력할것임.

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAchemy 초기화 (플라스크와 연동)
#app은 플라스크 객체가 담긴 변수의 이름임.
db = SQLAlchemy(app)

#migrate 초기화
migrate = Migrate(app,db)


#table 만들기
#파이썬으로 하나의 테이블을 만들어보자. 이를 위해서는 클래스 정의가 필요함
#db. 이하는 sqlalchemy 에서 사용하는 기능임.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    #nullable=False ; Not Null, unique= True; 고유값만 가능, String(숫자); 길이를 의미
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
    
#명령어
#flask db init
#flask db migrate
#flask db upgrade
