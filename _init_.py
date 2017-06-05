from flask import Flask
from Controller.index import main
from Controller.dict import zdb
from Controller.kjfp import kjfp

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(zdb)
app.register_blueprint(kjfp)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


app.config.setdefault('MYSQL_HOST', '47.92.37.219')
app.config.setdefault('MYSQL_USER', 'root')
app.config.setdefault('MYSQL_PASSWORD', '13Yeyepaodecha')
app.config.setdefault('MYSQL_DB', 'dzfp')
app.config.setdefault('MYSQL_PORT', 3306)

app.run(debug=True)
