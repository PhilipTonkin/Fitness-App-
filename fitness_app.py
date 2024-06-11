from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classes')
def classes():
    mock_classes = [
        {"id": 1, "name": "Yoga", "time": "9:00 AM", "trainer": "Alice"},
        {"id": 2, "name": "Spin", "time": "11:00 AM", "trainer": "Bob"},
        {"id": 3, "name": "Pilates", "time": "1:00 PM", "trainer": "Charlie"}
    ]
    return render_template('classes.html', classes=mock_classes)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        booked_class = request.form['class']
        return f'You have booked {booked_class}'
    mock_classes = [
        {"id": 1, "name": "Yoga", "time": "9:00 AM", "trainer": "Alice"},
        {"id": 2, "name": "Spin", "time": "11:00 AM", "trainer": "Bob"},
        {"id": 3, "name": "Pilates", "time": "1:00 PM", "trainer": "Charlie"}
    ]
    return render_template('booking.html', classes=mock_classes)

@app.route('/trainers')
def trainers():
    mock_trainers = [
        {"id": 1, "name": "Alice", "bio": "Certified Yoga Instructor"},
        {"id": 2, "name": "Bob", "bio": "Experienced Spin Trainer"},
        {"id": 3, "name": "Charlie", "bio": "Professional Pilates Coach"}
    ]
    return render_template('trainers.html', trainers=mock_trainers)

@app.route('/user', methods=['GET', 'POST'])
def user():
    user = {"name": "", "email": ""}
    if request.method == 'POST':
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        return f'Profile updated for {user["name"]}'
    return render_template('user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
