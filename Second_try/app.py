from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/restaurant_db'
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    party_size = db.Column(db.Integer, nullable=False)
    booking_time = db.Column(db.TIMESTAMP, nullable=False) 
    preferences = db.Column(db.String(255))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    data = request.json

    reservation = Reservation(
        first_name=data['firstName'],
        last_name=data['lastName'],
        phone_number=data['phoneNumber'],
        party_size=data['partySize'],
        reservation_number=data['reservationNumber'],
        booking_time=data['bookingTime']
    )

    db.session.add(reservation)
    db.session.commit()

    return jsonify({"message": "Reservation submitted successfully"}), 200

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)