from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

class Data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(60))
    age = db.Column(db.Integer)

db.init_app(app)

@app.route('/get', methods=['GET'])
def get_data():
    data = Data.query.all()
    response = [
        {
            'name': d.name,
            'age': d.age
        }
    for d in data]
    return jsonify(response)
    
@app.route('/post', methods=['POST'])
def post_data():
    info = request.get_json()
    new_data = Data(name = info["Name"],age = info["Age"])
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"Message":"New information added successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
