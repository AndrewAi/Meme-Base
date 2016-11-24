from flask import Flask, request,render_template
import couchdb



app = Flask(__name__)


couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch.create('test2')

doc = {'Irwin': 'Irwin'}
db.save(doc)




@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
