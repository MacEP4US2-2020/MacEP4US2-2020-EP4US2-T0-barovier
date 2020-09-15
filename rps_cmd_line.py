import random
game_opts = ["Rock","Paper","Scissors"]
ai_choice = random.choice(game_opts)

print("Welcome to the Rock-Paper-Scissors Game!")
usr_name = input("Please enter your name ")
usr_choice = input("Please enter your choice as one of the following [Rock,Paper,Scissors] ")
print(usr_choice)

def check_winner(usr_inp,ai_inp,usr_name = usr_name, game_opts=game_opts):
    winner = None
    if usr_inp == "Gun":
        print("You found the hack CONGRATS")
        winner = usr_name
    elif usr_inp not in game_opts:
        print("Invalid input")
        return "There is no winner when you don't play correctly"
    elif usr_inp == ai_inp:
        winner = "None! You tied"
    elif usr_inp == "Rock":
        if ai_inp == "Paper":
            winner = "Ai"
        elif ai_inp == "Scissors":
            winner = usr_name
    elif usr_inp == "Scissors":
        if ai_inp == "Paper":
            winner = usr_name
        elif ai_inp == "Rock":
            winner = "Ai"
    elif usr_inp == "Paper":
        if ai_inp == "Scissors":
            winner = "Ai"
        elif ai_inp == "Rock":
            winner = usr_name


    return winner

winning_player = check_winner(usr_choice,ai_choice)
print("The winning player is ",winning_player)

        
    
    
    
                   
