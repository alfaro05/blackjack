from django.shortcuts import render
from . import game_logic

def index(request):
    return render(request, "index.html")

def game(request):
    game_instance = game_logic.Game(2,[],[])
    request.session["game_object"] = game_instance.session_object()
    first_player_hand = game_instance.players[0].hand
    second_player_hand = game_instance.players[1].hand
    bot_will_continue = game_instance.players[0].will_continue
    request.session["bot_continues"]= bot_will_continue
    cards_dict = {"fph":first_player_hand,"sph":second_player_hand}
    return render(request, "game.html",cards_dict)

def next_round(request):
    continue_flag = ("True"==request.POST["continue"]) #if true, take another card from deck
    previous_round = request.session["game_object"]
    bot_takes_card = request.session["bot_continues"] #if true, bot takes another card
    #Create new instances for this round:
    deck_object = game_logic.Deck(False, game_logic.reorder_list(previous_round[0]))
    first_player = game_logic.Player(game_logic.reorder_list(previous_round[1]),True,0)
    second_player = game_logic.Player(game_logic.reorder_list(previous_round[2]),True,0)
    this_round_game = game_logic.Game(2, deck_object,[first_player,second_player])
    if(continue_flag):
        this_round_game.player_takes_new_card(1)
    if(bot_takes_card):
        this_round_game.player_takes_new_card(0)
    this_round_game.check_round()
    print("Bot", this_round_game.players[0].hand)
    print("Player", this_round_game.players[1].hand)
    game_over = this_round_game.game_over
    first_player_hand = this_round_game.players[0].hand
    second_player_hand = this_round_game.players[1].hand
    if(not(game_over)):
        request.session["game_object"]=this_round_game.session_object()
        bot_will_continue = this_round_game.players[0].will_continue
        request.session["bot_continues"]= bot_will_continue

    return render(request, "next_round.html",{"game_over":game_over,
        "fph":first_player_hand, "sph":second_player_hand})

#para el funcionamiento. en next round, para la instancia de jugadores, se toma de POST 
#la eleccion del jugador de seguir en el juego. Para el CPU se toma la bandera continue de la 
#instancia de jugador. 
