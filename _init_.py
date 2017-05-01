from flask import Flask
from Controller.index import main
app = Flask(__name__)

app.register_blueprint(main)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.run(debug=True)
