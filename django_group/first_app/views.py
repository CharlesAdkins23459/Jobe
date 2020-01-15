from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'wins' not in request.session:
        request.session['wins'] = 0
        request.session['losses'] = 0
        request.session['ties'] = 0

    return render(request, "first_app/index.html")

def process_play(request):
    
    comp_choice = random.randint(1,3)
       
    if comp_choice == 1:
        computer_choice = "rock"
    elif comp_choice == 2:
        computer_choice = "paper"
    elif comp_choice == 3:
        computer_choice = "scissors"

    request.session["computer_choice"] = computer_choice

    player_choice = request.POST["player_choice"]
    
    if player_choice == computer_choice: 
        request.session["outcome"] = "tie"
        request.session['ties'] = request.session['ties'] + 1

    elif (player_choice == "paper" and computer_choice =="rock")or(player_choice == "rock" and computer_choice == "scissors")or(player_choice == "scissors" and computer_choice == "paper"):
        request.session["outcome"] = "You won"
        request.session['wins'] = request.session['wins'] + 1

    elif (player_choice == "paper" and computer_choice == "scissors") or (player_choice == "rock" and computer_choice == "paper") or (player_choice == "scissors" and computer_choice == "rock"):
        # request.sesssion["outcome"] = "you lost, i think"   
        request.session['losses'] = request.session['losses'] + 1


    print(player_choice)
    print(computer_choice)
    return redirect("/")