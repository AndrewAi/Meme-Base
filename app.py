from flask import Flask, request, render_template, flash, url_for, redirect, jsonify
import couchdb, json, requests, random
from werkzeug.utils import secure_filename

app = Flask(__name__)


# r = requests.get('http://127.0.0.1:5984/_all_dbs')
# print("r:", r)




# BELOW CODE IS HOW TO POST A NON IMAGE DOCUMENT
# j = {"_id": "FishStew"}
# requests.post('http://127.0.0.1:5984/test2/',data=None,json=j)
# doc = requests.get('http://127.0.0.1:5984/test2/')



# http://127.0.0.1:5984/test2/_design/design1/_view/_all_attachments?limit=20&reduce=false



#c = requests.get('http://127.0.0.1:5984/test2/_design/_design1/_view/_all_attachment_names?limit=20&reduce=false')
#c = requests.get('http://127.0.0.1:5984/test2/abcasa')
#parsed_json = json.loads(c.text)
#print("parsed_json: ", parsed_json)


#e = parsed_json['_attachments']
#pop = e.keys()

#for key in pop:
 #   print('key: ', key)
  #  imgName  = key





#c = requests.get('http://127.0.0.1:5984/test2/_design/_design1/_view/_all_attachment_names?limit=20&reduce=false')


'''c = requests.get('http://127.0.0.1:5984/test2/abcasa')
parsed_json = json.loads(c.text)
print("parsed_json: ", parsed_json)


e = parsed_json['_attachments']
pop = e.keys()

for key in pop:
    print('key: ', key)
    imgName  = key
    '''






name = "abcasa"
#print('e: ', e.keys())
#f = e[0]
#print("f: ", f['key'])
# print("c1: ", c.content['_id'])
#img = "http://localhost:5984/test2/5b5b558c24f1cc3213ccd3214100c7ac" + f['key']
#print('name:', name)
#print('imgName', imgName)
#img = "http://127.0.0.1:5984/test2/" + name + '/' + imgName
#print('img', img)
#print("img: ", img)



#doc = "http://localhost:5984/test2/2/aboutme.jpg"
# print("doc: ", doc.content)
# print("doc: ", doc)

# j = {"irwin": "andyir"}
# requests.post('http://127.0.0.1:5984/test2/', data=None, json=j)





# return jsonify({'name': "yes"})

# return jsonify({'error': 'Missing data!'})
#"VGhpcyBpcyBhIGJhc2U2NCBlbmNvZGVkIHRleHQ="


'''
        #return redirect(url_for('imgurl'))


        docName = request.form['memeBaseNameInput']

        docNameUrl = 'http://127.0.0.1:5984/test2/' + docName
        print('docNameUrl: ', docNameUrl)
        c = requests.get('http://127.0.0.1:5984/test2/' + docName)

        if c:'''


'''parsed_json = json.loads(c.text)
            print("parsed_json: ", parsed_json)

            e = parsed_json['_attachments']
            pop = e.keys()

            for key in pop:
                print('key: ', key)
                imgName = key

            print('docName: ', docName)
            print('imgName: ', imgName)
            imgLocation = 'http://127.0.0.1:5984/test2/' + docName + '/' + imgName
            print('imgLocation: ', imgLocation)
            return render_template('imgurl.html')'''




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    if request.method == 'POST':

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





@app.route('/page3', methods=['GET', 'POST'])
def page3():

    if request.method == 'POST':

        docName = request.form['memeBaseNameInput']
        print("docName: ", docName)

        docNameUrl = 'http://127.0.0.1:5984/test2/' + docName
        print("docNameUrl: ", docNameUrl)

        ca = requests.get(docNameUrl)
        print("ca: ", ca.text)

        if ca :
            parsed_json = json.loads(ca.text)
            print("parsed_json: ", parsed_json)

            e = parsed_json['_attachments']
            pop = e.keys()

            for key in pop:
                print('key: ', key)
                imgName = key

            print("imgName: ", imgName)
            imglocation = 'http://127.0.0.1:5984/test2/' + docName + '/' + imgName

            return redirect(url_for('imgurl', imglocation = imglocation))




    return render_template('page3.html')


@app.route('/page5', methods=['GET', 'POST'])
def page5():
    if request.method == 'POST':
        return redirect(url_for('index'))









@app.route('/imgurl')
def imgurl():
    #http://stackoverflow.com/questions/17057191/flask-redirect-while-passing-arguments
    img = request.args['imglocation']

    print("img: ", img)

    return render_template('imgurl.html', img = img)






@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        age = request.form['age']

        return render_template('test.html', age=age)


@app.route('/page')
def page():
    return ("Andrew Irwin")
    # return render_template('index.html')


@app.route('/test', methods=["GET", "POST"])
def test():
    return render_template('test.html')

    if request.method == "POST":
        print("posted")


@app.errorhandler(404)
def page_not_found(e):
    return ("page does not exist")


if __name__ == '__main__':
    app.run(debug=True)
