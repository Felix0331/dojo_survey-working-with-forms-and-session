from flask import render_template,request,redirect,session
from flask_app import app

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_form():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    data={
        'name': request.form['name'],
        'location':request.form['location'],
        'language':request.form['language'],
        'comment':request.form['comment']
    }
    id = Dojo.add_dojo(data)
    print(f"{id} *********")
    return redirect(f'/result/{id}')

@app.route('/result/<int:id>')
def show_result(id):
    data={
        'id':id
    }
    dojo = Dojo.get_dojo(data)
    return render_template('result.html',dojo=dojo)

@app.route("/make_dojo", methods=["POST"])
def create_dojo():
    data = {
        "name":request.form["dojo_name"]
    }
    Dojo.add_dojo(data)
    return redirect("/dojos")