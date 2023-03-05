'''
Fix:
# python -m pip install --upgrade pip
# python -m pip install --no-use-pep517 flask-bcrypt
'''
from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisfirstflaskapp'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://devusr:hello123@127.0.0.1:3306/devboxdb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://epiz_32034111:YN8OIc798ESVt@sql308.epizy.com/epiz_32034111_User'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yOknKizheA:oTZYWPHT1I@remotemysql.com/yOknKizheA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ba35104d7b3d3f:b52ef3e2@us-cdbr-east-04.cleardb.com/heroku_13b52dd7911dfd6'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE']=90


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'roam.chat.email'
app.config['MAIL_PASSWORD'] = 'gpsdzuxokokqvftd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True

app.config['TWILIO_ACCOUNT_SID'] = "AC2b28b5edf23b5a2f9dd3d98369acd213"
app.config['TWILIO_AUTH_TOKEN'] = "faf05f27904a454d9cf5ec4aa2c8911a"

mail = Mail(app)


from project import routes
