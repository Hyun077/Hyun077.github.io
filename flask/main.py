from flask import Flask, render_template
from flask import jsonify, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask import send_from_directory
from pathlib import Path
import subprocess
import os
import xlwings as xw
from test import change 

UPLOAD_FOLDER = 'C:/Users/eic/Desktop/TEST/temp/'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif','xls'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/test")
def test():
    if(subprocess.call("test.py", shell=True)):
        return jsonify("great!")
@app.route("/hello", methods=['GET', 'POST'])
def call_hello():
    if request.method == 'POST': 
        return redirect(url_for('hello', username=request.form.get('username')))
    return render_template("hello.html")
@app.route("/hello/<username>", methods=['GET', 'POST'])
def hello(username):
        return '<script language="javascript">alert("Hello "+"' + username + '");</script>'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    
@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(app.config['UPLOAD_FOLDER'] )
            new_filename = filename.split('.')[0] + ".xlsx"
            change(filename)
            os.remove(app.config['UPLOAD_FOLDER']+filename)
            print(filename)
            print(new_filename)

            TEMP_OB=redirect(url_for('uploaded_file',filename=new_filename))
            return TEMP_OB
    return redirect(url_for('call_hello'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #os.remove(app.config['UPLOAD_FOLDER']+filename)
    TEMP_OB=send_from_directory(app.config['UPLOAD_FOLDER'],filename,as_attachment=True)
    return TEMP_OB


if __name__ == "__main__":
    #app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
    
def create_app():
   return app