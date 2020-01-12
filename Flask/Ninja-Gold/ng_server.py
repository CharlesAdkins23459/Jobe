from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def index():
    if 'gold' in session:
        session['amount_of_gold'] = session.get('gold_amount')
    else:
        session['amount_of_gold'] = 0 
        session['activities'] = []
    return render_template('/index.html')

@app.route('/process_gold', methods=['POST'])
def process_gold():
    choice = request.form['choice']
    print(choice)
    if choice == 'farm':
        randNum = random.randint(10, 20)
    elif choice == 'cave':
        randNum = random.randint(5, 10)
    elif choice == 'house':
        randNum = random.randint(2, 5)
    elif choice == 'casino':
        randNum = random.randint(-50, 0)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)