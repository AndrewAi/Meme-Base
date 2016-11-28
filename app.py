from flask import Flask, request, render_template, flash, url_for, redirect, jsonify
import couchdb, json, requests
from werkzeug.utils import secure_filename

app = Flask(__name__)

couch = couchdb.Server('http://127.0.0.1:5984/')

db = couch['test2']

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
img = "http://127.0.0.1:5984/test2/adbd28419a7d61231cf9ce72f000362f/aboutme.png"
print("img: ", img)
print("img: ", "http://localhost:5984/test2/5b5b558c24f1cc3213ccd3214100c7ac/aboutme.jpg")


#doc = "http://localhost:5984/test2/2/aboutme.jpg"
# print("doc: ", doc.content)
# doc = db.get_attachment('2', 'aboutme.jpg', default=None)
# print("doc: ", doc)

# j = {"irwin": "andyir"}
# requests.post('http://127.0.0.1:5984/test2/', data=None, json=j)











# return jsonify({'name': "yes"})

# return jsonify({'error': 'Missing data!'})
#"VGhpcyBpcyBhIGJhc2U2NCBlbmNvZGVkIHRleHQ="



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    name = request.form['name'],
    file = request.form['data']


    if file:

         print(file)
         ja = "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"
         name = "aboutme.png"
         jj = {
             "_attachments":
                 {
                     name:
                         {
                             "content_type": "image/png",
                             "data": file
                         }
                 }
         }
         requests.post('http://127.0.0.1:5984/test2/', data=None, json=jj)



    return jsonify({'name': "yes"})




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
