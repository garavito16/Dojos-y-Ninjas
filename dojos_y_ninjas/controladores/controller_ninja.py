from flask import render_template,redirect, request
from dojos_y_ninjas import app
from dojos_y_ninjas.modelos.model_ninja import Ninja
from dojos_y_ninjas.modelos.model_dojo import Dojo

@app.route('/ninjas',methods=["GET"])
def view_create_ninja():
    dojos = Dojo.getDojos()
    return render_template("create_ninja.html",dojos=dojos)


@app.route('/ninjas',methods=["POST"])
def create_ninja():
    id = request.form["dojo_id"]
    ninja = {
        "first_name" : request.form["first_name"],
        "last_name"  : request.form["last_name"],
        "age"  : request.form["age"],
        "dojo_id"  : request.form["dojo_id"]
    }
    result = Ninja.createNinja(ninja)
    print(result)
    if result > 0:
        return redirect('/dojos/'+id)
    else:
        return redirect('/ninjas')

