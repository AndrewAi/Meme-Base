from flask import Flask, request,render_template
import couchdb



app = Flask(__name__)


couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch['test2']

a = db['af0a87fa1f89e2a0d6f56b429d0012e3']
#db['123'] = {'irwin','andrew'} 

#print("a : ", a["Andy"] )



@app.route('/')
def index():
    return render_template('index.html', a = a['Andy'])


if __name__ == '__main__':
    app.run()
