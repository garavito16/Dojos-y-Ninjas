
from flask import render_template,redirect, request
from dojos_y_ninjas import app
from dojos_y_ninjas.modelos.model_dojo import Dojo

@app.route('/dojos',methods=["GET"])
def get_dojos():
    result = Dojo.getDojos()
    return render_template("dojos.html",dojos=result)

@app.route('/create_dojo',methods=["POST"])
def create_dojo():
    dojo = {
        "name" : request.form["name"]
    }
    result = Dojo.createDojo(dojo)
    if result > 0:
        return redirect('/dojos')

@app.route('/dojos/<dojo_id>',methods=["GET"])
def view_dojo(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    dojo = Dojo.ninjasOfDojo(data)
    print(dojo)
    return render_template("view_dojo.html",dojo=dojo)