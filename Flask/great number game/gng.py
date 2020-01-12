from flask import Flask, redirect, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'keyring'

@app.route('/')
def great_number_game():    
    if 'random_number' in session:
        session['random_number'] = session.get('random_number')
        session['number_of_guesses'] = session.get('number_of_guesses') + 1
    else:
        session['random_number'] = random.randint(1, 100)
        session['outcome'] = "outcome"
        session['guess'] = "guess"
        session['number_of_guesses'] = 0

    return render_template('gng.html', randNum=session['random_number'], outcome=session['outcome'], guess=session['guess'], numGuesses=session['number_of_guesses'])

@app.route('/check', methods=['POST'])
def num_check():
    random_number = session['random_number']
    guess = request.form['guess']
    session['guess'] = guess
    print(session['number_of_guesses'])
    if int(guess) < random_number:
        print("Too Low!")
        print(guess)
        print(random_number)
        session['outcome'] = "Too Low!"
    elif int(guess) > random_number:
        print("Too High!")
        session['outcome'] = "Too High!"
    else: 
        print("Exactly")
        session['outcome'] = "Correct!"
    return redirect('/')

@app.route('/new-game')
def new_game():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)