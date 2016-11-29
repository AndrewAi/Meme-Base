from flask import Flask, request, render_template, flash, url_for, redirect, jsonify
import couchdb, json, requests, random
from werkzeug.utils import secure_filename

app = Flask(__name__)

#couch = couchdb.Server('http://127.0.0.1:5984/')

#db = couch['test2']

# a = db['af0a87fa1f89e2a0d6f56b429d0012e3']
# r = requests.get('http://127.0.0.1:5984/_all_dbs')
# print("r:", r)

# db['123'] = {'irwin','andrew'}
# print("a : ", a["Andy"] )







# BELOW CODE IS HOW TO POST A NON IMAGE DOCUMENT
# j = {"_id": "FishStew"}
# requests.post('http://127.0.0.1:5984/test2/',data=None,json=j)
# doc = requests.get('http://127.0.0.1:5984/test2/')



# http://127.0.0.1:5984/test2/_design/design1/_view/_all_attachments?limit=20&reduce=false










c = requests.get('http://127.0.0.1:5984/test2/_design/_design1/_view/_all_attachment_names?limit=20&reduce=false')
parsed_json = json.loads(c.text)

e = parsed_json['rows']
f = e[0]
print("f: ", f['key'])
# print("c1: ", c.content['_id'])
#img = "http://localhost:5984/test2/5b5b558c24f1cc3213ccd3214100c7ac" + f['key']
img = "http://127.0.0.1:5984/test2/abcasa/meme.png"
print("img: ", img)
print("img: ", "http://localhost:5984/test2/5b5b558c24f1cc3213ccd3214100c7ac/aboutme.jpg")


#doc = "http://localhost:5984/test2/2/aboutme.jpg"
# print("doc: ", doc.content)
# doc = db.get_attachment('2', 'aboutme.jpg', default=None)
# print("doc: ", doc)

# j = {"irwin": "andyir"}
# requests.post('http://127.0.0.1:5984/test2/', data=None, json=j)



#iandata = {"_id":"ian"}
#requests.post('http://127.0.0.1:5984/test2/', data=None, json= iandata)

#j = {"height": "aaa"}
#requests.post('http://127.0.0.1:5984/test2/',data=None,json=j)



# return jsonify({'name': "yes"})

# return jsonify({'error': 'Missing data!'})
#"VGhpcyBpcyBhIGJhc2U2NCBlbmNvZGVkIHRleHQ="



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    memeName = request.form['memeName']
    memeBaseName = request.form['memeBaseName']
    file = request.form['data']


    if file:

         print("file: ",file)
         memeName += ".png"
         print("memeName: ", memeName)
         print("memeBaseName: ", memeBaseName)



         jj = {
             "_id": memeBaseName,
             "_attachments":
                 {
                     memeName:
                         {
                             "content_type": "image/png",
                             "data": file
                         }
                 }
         }
         requests.post('http://127.0.0.1:5984/test2/', data=None, json=jj)



    return jsonify({'name': "Meme Uploaded"})




@app.route('/imgurl/')
def imgurl():
    return render_template('imgurl.html', img=img)


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']

        return render_template('test.html', age=age)


@app.route('/page/')
def page():
    return ("Andrew Irwin")
    # return render_template('index.html')


@app.route('/test/', methods=["GET", "POST"])
def test():
    return render_template('test.html')

    if request.method == "POST":
        print("posted")


@app.errorhandler(404)
def page_not_found(e):
    return ("page does not exist")


if __name__ == '__main__':
    app.run(debug=True)
