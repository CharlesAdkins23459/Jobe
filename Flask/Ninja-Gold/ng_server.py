from flask import Flask, redirect, render_template, request, session, Markup
from datetime import datetime
import time, random

app = Flask(__name__)
app.secret_key = 'secret'
activity_list = []
amount_of_gold = 0

@app.route('/')
def index():
    
    if 'amount_of_gold' not in session:
        session['amount_of_gold'] = 0
        session['activity_list'] = []

    return render_template('/index.html', activity_list=session['activity_list'], amount_of_gold=session['amount_of_gold'])
########################################################################################################################################

@app.route('/process_gold', methods=['POST'])
def process_gold():
    choice = request.form['choice']
    print(choice)
    current_time = time.time()
    timestamp = datetime.fromtimestamp(current_time).strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp)
    
    if choice == 'farm':
        randNum = random.randint(10, 20)
        activity = Markup("<p class='green'>Earned " + str(randNum) + " from the farm! " + timestamp + "</p>")
        print(activity)
    
    elif choice == 'cave':
        randNum = random.randint(5, 10)
        activity = Markup("<p class='green'>Found " + str(randNum) + " in the cave " + timestamp + "</p>")
        print(activity)
    
    elif choice == 'house':
        randNum = random.randint(2, 5)
        activity = Markup("<p class='green'>Found " + str(randNum) + " gold in your couch!" + timestamp + "</p>")
        print(activity)

    elif choice == 'casino':
        winLoss = random.randint(1, 100)
        if winLoss < 75:
            randNum = random.randint(-50, 0)
            activity = Markup("<p class='red'>Lost " + str(randNum) + " gold at the casino! :(" + timestamp + "</p>")
        else:
            randNum = random.randint(0, 50)
            activity = Markup("<p class='green'>Won " + str(randNum) + " gold at the casino! :D" + timestamp + "</p>")
        print(activity)

    # activity_list.append(activity)
    # session['activity_list'] =  activity_list
    session['activity_list'].append(activity)
    session['amount_of_gold'] = session['amount_of_gold'] + randNum
    print(session.get('activity_list'))
    return redirect('/')

@app.route('/new_game')
def new_game():
    session.clear()

    amount_of_gold = 0

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)