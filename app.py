from flask import Flask, request,render_template,flash,request,url_for,redirect
import couchdb



app = Flask(__name__)


couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch['test2']

a = db['af0a87fa1f89e2a0d6f56b429d0012e3']
#a = db.get_attachment('af0a87fa1f89e2a0d6f56b429d0012e3','aboutme.jpg')
#db['123'] = {'irwin','andrew'} 

print("a : ", a["Andy"] )



@app.route('/')
def index():
    return render_template('index.html', a = a)

@app.route('/page/')
def page():

    return("Andrew Irwin")    
    #return render_template('index.html', a = a)

@app.route('/test/', methods=["GET","POST"])
def test():

    return render_template('test.html')  
   

    if request.method == "POST":
        print("posted")
        
         
        

@app.errorhandler(404)
def page_not_found(e):
    return ("page does not")


if __name__ == '__main__':
    app.run()
