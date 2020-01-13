from flask import Flask, redirect, render_template, request, session, Markup
from datetime import datetime
import time, random

app = Flask(__name__)
app.secret_key = 'secret'
activity_list = []
amount_of_gold = 0
number_of_turns = 0

@app.route('/')
def index():
    
    if 'amount_of_gold' not in session:
        session['amount_of_gold'] = 0
        session['activity_list'] = []
        session['number_of_turns'] = 0
        session['game_on'] = True

    return render_template('/index.html', activity_list=session['activity_list'], amount_of_gold=session['amount_of_gold'])

########################################################################################################################################

@app.route('/process_gold', methods=['POST'])
def process_gold():
    session['number_of_turns'] = session['number_of_turns'] + 1
    choice = request.form['choice']
    print(choice)
    current_time = time.time()
    timestamp = datetime.fromtimestamp(current_time).strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp)

    if (session['number_of_turns'] <= 15):
        turn = str(session['number_of_turns'])
        if choice == 'farm':
            randNum = random.randint(10, 20)
            activity = Markup( "<p class='green'>" + turn + ". Earned " + str(randNum) + " gold from the farm! " + timestamp + "</p>")
            print(activity)
        
        elif choice == 'cave':
            randNum = random.randint(5, 10)
            activity = Markup("<p class='green'>" + turn + ". \tFound " + str(randNum) + " gold in the cave! " + timestamp + "</p>")
            print(activity)
        
        elif choice == 'house':
            randNum = random.randint(2, 5)
            activity = Markup("<p class='green'>" + turn + ". Found " + str(randNum) + " gold in your couch! " + timestamp + "</p>")
            print(activity)

        elif choice == 'casino':
            winLoss = random.randint(1, 100)
            if winLoss < 75:
                randNum = random.randint(-50, 0)
                activity = Markup("<p class='red'> " + turn + ". Lost " + str(randNum) + " gold at the casino! :( " + timestamp + "</p>")
            else:
                randNum = random.randint(0, 50)
                activity = Markup("<p class='green'> " + turn + ". Won " + str(randNum) + " gold at the casino! :D " + timestamp + "</p>")
            print(activity)
        session['amount_of_gold'] = session['amount_of_gold'] + randNum
        if session['amount_of_gold'] >= 400:
            activity = Markup("Congratulations! You made it to 400 gold in less than 15 turns! Start a <a href='/new_game'>New Game?")
    else:
        activity = Markup("Game over. You didn't make it to 400 gold. Start a <a href='/new_game'>New Game?</a>")
    
    session['activity_list'].append(activity)
    print(session.get('activity_list'))
    return redirect('/')

@app.route('/new_game')
def new_game():
    session.clear()
    amount_of_gold = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)