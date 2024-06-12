from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

trainers = [
    {
        'name': 'Alice Johnson',
        'specialty': 'Specializes in yoga and pilates.',
        'image': 'alice.jpg',
        'bio': 'Alice has over 10 years of experience in yoga and pilates. She has conducted workshops and seminars globally. Join her for an enriching experience.',
        'challenges': ['Join the zero to 10k team', 'Yoga for flexibility and strength']
    },
    {
        'name': 'Bob Smith',
        'specialty': 'Certified personal trainer focusing on strength training and bodybuilding.',
        'image': 'bob.jpg',
        'bio': 'Bob is a seasoned personal trainer with a passion for strength training. He has helped many clients achieve their fitness goals.',
        'challenges': ['Strength training for all levels', 'Bodybuilding competition prep']
    },
    {
        'name': 'Carol Lee',
        'specialty': 'Expert in HIIT and aerobic exercises.',
        'image': 'carol.jpg',
        'bio': 'Carol is known for her high-energy HIIT and aerobic classes. She motivates her students to push their limits and achieve new heights.',
        'challenges': ['HIIT for quick results', 'Functional training for daily life']
    },
]

classes = [
    {
        'name': 'Aerobic Class',
        'image': 'aerobic.jpg',
        'instructor': 'Alice Johnson',
        'schedule': [('Monday', '9:00 AM - 10:00 AM'), ('Wednesday', '9:00 AM - 10:00 AM')]
    },
    {
        'name': 'HIIT Class',
        'image': 'hiit.jpg',
        'instructor': 'Bob Smith',
        'schedule': [('Tuesday', '10:00 AM - 11:00 AM'), ('Thursday', '10:00 AM - 11:00 AM')]
    },
    {
        'name': 'Pilates Class',
        'image': 'pilates.jpg',
        'instructor': 'Carol Lee',
        'schedule': [('Friday', '11:00 AM - 12:00 PM')]
    },
    {
        'name': 'Yoga Class',
        'image': 'yoga.jpg',
        'instructor': 'Alice Johnson',
        'schedule': [('Monday', '12:00 PM - 1:00 PM'), ('Wednesday', '12:00 PM - 1:00 PM')]
    },
    {
        'name': 'Strength Training',
        'image': 'strength.jpg',
        'instructor': 'Bob Smith',
        'schedule': [('Monday', '5:00 PM - 6:00 PM'), ('Friday', '5:00 PM - 6:00 PM')]
    },
    {
        'name': 'Flexibility Training',
        'image': 'flexibility.jpg',
        'instructor': 'Carol Lee',
        'schedule': [('Wednesday', '7:00 AM - 8:00 AM')]
    },
]

@app.route('/')
def index():
    return render_template('index.html', trainers=trainers)

@app.route('/classes')
def class_schedule():
    return render_template('classes.html', classes=classes)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        session['booked_class'] = request.form['class']
        return redirect(url_for('user'))
    return render_template('booking.html', classes=classes)

@app.route('/trainers')
def trainers_view():
    return render_template('trainers.html', trainers=trainers)

@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html')

@app.route('/cancel', methods=['POST'])
def cancel_booking():
    session.pop('booked_class', None)
    return redirect(url_for('user'))

@app.route('/private_sessions/<trainer_name>', methods=['GET', 'POST'])
def private_session(trainer_name):
    if request.method == 'POST':
        session['booked_session'] = {
            'trainer': trainer_name,
            'date': request.form['date'],
            'time': request.form['time']
        }
        return redirect(url_for('user'))
    return render_template('private_session.html', trainer_name=trainer_name)

if __name__ == '__main__':
    app.run(debug=True)
