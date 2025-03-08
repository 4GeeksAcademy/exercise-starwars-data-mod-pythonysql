from flask import Flask, request, jsonify
from models import db, User, Personaje, Planet, Specie, Vehicle
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
Migrate(app, db)
db.init_app(app) #Establecemos la conexion con flask y sqlalchemy



# PUT GET POST DELETE de tabla User
@app.route('/user', methods=["POST"])
def create_user():
    user = User()
    user.name = request.json.get('name')
    user.email = request.json.get('email')
    user.password = request.json.get('password')
    user.date = request.json.get('date')

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario guardado"
    }), 200

@app.route('/user/list')
def get_all_user():
    user = user.query.all()
    user = list(map(lambda user: user.serialize_user(), user))
    return jsonify(user), 200


@app.route('/user/<int:user_id>', methods=["PUT", "DELETE"])
def update_delete_user(user_id):
    if request.method == 'PUT':
        user = user.query.get(user_id)
        if user is None:
            return jsonify({
                'mensaje': 'Usuario no encontrado'
            }), 404
        else:
            user.name = request.json.get('name')
            user.email = request.json.get('email')
            user.password = request.json.get('password')
            user.date = request.json.get('date')

            db.session.commit()

            return jsonify({
                'mensaje': 'Usuario modificado'
            }), 200
    elif request.method == 'DELETE':
        user = user.query.get(user_id)
        if user is None:
            return jsonify({
                'mensaje': 'User no encontrado'
            }), 404
        else:
            db.session.delete(user)
            db.session.commit()

            return jsonify({
                "mensaje":"usuario eliminado"
            }), 200
        

# PUT GET POST DELETE de tabla Personaje
@app.route('/favorite/personaje', methods=["POST"])
def create_personaje():
    personaje = Personaje()
    personaje.firstname_per = request.json.get('firstname_per')
    personaje.descrip_per = request.json.get('descrip_per')
    personaje.user_id = request.json.get('user_id')
   

    db.session.add(personaje)
    db.session.commit()

    return jsonify({
        "mensaje": "Personaje guardado"
    }), 200

@app.route('/favorite/personaje/list')
def get_all_personaje():
    personaje = personaje.query.all()
    personaje = list(map(lambda personaje: personaje.serialize_personaje(), personaje))
    return jsonify(personaje), 200


@app.route('/favorite/personaje/<int:personaje_id>', methods=["PUT", "DELETE"])
def update_delete_personaje(personaje_id):
    if request.method == 'PUT':
        personaje = personaje.query.get(personaje_id)
        if personaje is None:
            return jsonify({
                'mensaje': 'personaje no encontrado'
            }), 404
        else:
            personaje.firstname_per = request.json.get('firstname_per')
            personaje.descrip_per = request.json.get('descrip_per')
            personaje.user_from_id = request.json.get('user_from_id')
          

            db.session.commit()

            return jsonify({
                'mensaje': 'personaje modificado'
            }), 200
    elif request.method == 'DELETE':
        personaje = personaje.query.get(personaje_id)
        if personaje is None:
            return jsonify({
                'mensaje': 'Personaje no encontrado'
            }), 404
        else:
            db.session.delete(personaje)
            db.session.commit()

            return jsonify({
                "mensaje":"personaje eliminado"
            }), 200


# PUT GET POST DELETE de tabla Planets
@app.route('/favorite/planet', methods=["POST"])
def create_personaje():
    planet = Planet()
    planet.firstname_pla = request.json.get('firstname_pla')
    planet.descrip_pla = request.json.get('descrip_pla')
    planet.user_id = request.json.get('user_id')
   

    db.session.add(planet)
    db.session.commit()

    return jsonify({
        "mensaje": "planet guardado"
    }), 200

@app.route('/favorite/planet/list')
def get_all_planet():
    planet = planet.query.all()
    planet = list(map(lambda planet: planet.serialize_planet(), planet))
    return jsonify(planet), 200


@app.route('/favorite/planet/<int:planet_id>', methods=["PUT", "DELETE"])
def update_delete_personaje(planet_id):
    if request.method == 'PUT':
        planet = planet.query.get(planet_id)
        if planet is None:
            return jsonify({
                'mensaje': 'planet no encontrado'
            }), 404
        else:
            planet.firstname_pla = request.json.get('firstname_pla')
            planet.descrip_pla = request.json.get('descrip_pla')
            planet.user_from_id = request.json.get('user_from_id')
          

            db.session.commit()

            return jsonify({
                'mensaje': 'planet modificado'
            }), 200
    elif request.method == 'DELETE':
        planet = planet.query.get(planet_id)
        if planet is None:
            return jsonify({
                'mensaje': 'planet no encontrado'
            }), 404
        else:
            db.session.delete(planet)
            db.session.commit()

            return jsonify({
                "mensaje":"planet eliminado"
            }), 200


# PUT GET POST DELETE de tabla specie
@app.route('/favorite/specie', methods=["POST"])
def create_personaje():
    specie = Specie()
    specie.firstname_spe = request.json.get('firstname_spe')
    specie.descrip_spe = request.json.get('descrip_spe')
    specie.user_id = request.json.get('user_id')
   

    db.session.add(specie)
    db.session.commit()

    return jsonify({
        "mensaje": "specie guardado"
    }), 200

@app.route('/favorite/specie/list')
def get_all_specie():
    specie = specie.query.all()
    specie = list(map(lambda specie: specie.serialize_specie(), specie))
    return jsonify(specie), 200


@app.route('/favorite/specie/<int:specie_id>', methods=["PUT", "DELETE"])
def update_delete_specie(specie_id):
    if request.method == 'PUT':
        specie = specie.query.get(specie_id)
        if specie is None:
            return jsonify({
                'mensaje': 'specie no encontrado'
            }), 404
        else:
            specie.firstname_spe = request.json.get('firstname_spe')
            specie.descrip_spe = request.json.get('descrip_spe')
            specie.user_id = request.json.get('user_id')
          

            db.session.commit()

            return jsonify({
                'mensaje': 'specie modificado'
            }), 200
    elif request.method == 'DELETE':
        specie = specie.query.get(specie_id)
        if specie is None:
            return jsonify({
                'mensaje': 'specie no encontrado'
            }), 404
        else:
            db.session.delete(specie)
            db.session.commit()

            return jsonify({
                "mensaje":"specie eliminado"
            }), 200


# PUT GET POST DELETE de tabla vehicle
@app.route('/favorite/vehicle', methods=["POST"])
def create_vehicle():
    vehicle = vehicle()
    vehicle.firstname_vehi = request.json.get('firstname_vehi')
    vehicle.descrip_vehi = request.json.get('descrip_vehi')
    vehicle.user_id = request.json.get('user_id')
   

    db.session.add(vehicle)
    db.session.commit()

    return jsonify({
        "mensaje": "vehicle guardado"
    }), 200

@app.route('/favorite/vehicle/list')
def get_all_vehicle():
    vehicle = vehicle.query.all()
    vehicle = list(map(lambda vehicle: vehicle.serialize_vehicle(), vehicle))
    return jsonify(vehicle), 200


@app.route('/favorite/vehicle/<int:personaje_id>', methods=["PUT", "DELETE"])
def update_delete_vehicle(vehicle_id):
    if request.method == 'PUT':
        vehicle = vehicle.query.get(vehicle_id)
        if vehicle is None:
            return jsonify({
                'mensaje': 'vehicle no encontrado'
            }), 404
        else:
            vehicle.firstname_vehi = request.json.get('firstname_vehi')
            vehicle.descrip_vehi = request.json.get('descrip_vehi')
            vehicle.user_id = request.json.get('user_id')
          

            db.session.commit()

            return jsonify({
                'mensaje': 'vehicle modificado'
            }), 200
    elif request.method == 'DELETE':
        vehicle = vehicle.query.get(vehicle_id)
        if vehicle is None:
            return jsonify({
                'mensaje': 'vehicle no encontrado'
            }), 404
        else:
            db.session.delete(vehicle)
            db.session.commit()

            return jsonify({
                "mensaje":"vehicle eliminado"
            }), 200



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
