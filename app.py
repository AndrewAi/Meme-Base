from flask import Flask, request, render_template, flash, url_for, redirect, jsonify
import couchdb, json, requests, random
from werkzeug.utils import secure_filename

app = Flask(__name__)

database = "memebase"








@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        docName = request.form['memeBaseNameInput']
        print("docName: ", docName)

        docNameUrl = 'http://127.0.0.1:5984/' + database + '/' + docName
        print("docNameUrl: ", docNameUrl)

        ca = requests.get(docNameUrl)
        print("ca: ", ca.text)

        if ca:
            parsed_json = json.loads(ca.text)
            print("parsed_json: ", parsed_json)

            e = parsed_json['_attachments']
            pop = e.keys()

            for key in pop:
                print('key: ', key)
                imgName = key

            print("imgName: ", imgName)
            imglocation = 'http://127.0.0.1:5984/' + database + '/' + docName + '/' + imgName

            return redirect(url_for('imgurl', imglocation=imglocation, imgTitle=imgName))



    return render_template('index.html')



@app.route('/tocreate', methods=['GET', 'POST'])
def tocreate():
    if request.method == 'POST':
        return redirect(url_for('create'))


@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('create.html')




@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':

        memeName = request.form['memeName']
        memeBaseName = request.form['memeBaseName']
        file = request.form['data']

        if file:
            print("file: ", file)
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
            uploadRequest =  requests.post('http://127.0.0.1:5984/' + database + '/', data=None, json=jj)

            print("uploadRequest: ", uploadRequest.status_code)
            if uploadRequest.status_code == requests.codes.ok:
                return jsonify({'name': "Meme Uploaded"})

            return jsonify({'error': "Failed to Upload Meme. Sorry :("})


@app.route('/imgurl')
def imgurl():
    # http://stackoverflow.com/questions/17057191/flask-redirect-while-passing-arguments
    img = request.args['imglocation']
    imgTitle = request.args['imgTitle']

    print("img: ", img)

    return render_template('imgurl.html', img=img, imgTitle=imgTitle)





@app.errorhandler(404)
def page_not_found(e):
    return ("page does not exist")


if __name__ == '__main__':
    app.run(debug=True)
