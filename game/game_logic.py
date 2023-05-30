import random

#Instances from this class contain the total amount 
class Player():
    def __init__(self, hand, still_alive, result):
        if(hand == []):
            self.hand = []
            self.still_alive = True
            self.result = 0
            self.will_continue = True
        else:
            self.hand = hand
            self.still_alive = still_alive
            self._result = result
            self.will_continue = True

class Deck():
    def __init__(self, first_round, current_deck):
        if(first_round):
            self.set_deck()
        else:
            self.deck = current_deck
    def set_deck(self):
        symbols_tuple = ["spade","heart", "diamond", "club"]
        deck_list = []
        for symbol in symbols_tuple:
            deck_list += [(num, symbol) for num in range(1,14,1)]
            random.shuffle(deck_list)
        self.deck = deck_list
    #Takes cards from the deck. The amount depends on the argument.
    def take_cards (self, num_cards):
        cards_removed = []
        for i in range(num_cards):
            cards_removed.append(self.deck[i])
            self.deck.pop(0)
        return(cards_removed)
    
class Game():
    def __init__(self, num_players, deck, players):
        self.num_players = num_players 
        self.game_over = False
        if(deck == []):
            self.deck = Deck(True, [])
            self.set_players()
            self.start_game()
        else:
            self.deck = deck
            self.players = players
            print(self.players)

    def set_players(self):
        players = []
        for i in range(self.num_players):
            players.append(Player([], True, 0))
        self.players = players

    def start_game(self):
        starting_cards = self.deck.take_cards(2*self.num_players)

        for i in range(self.num_players):
            self.players[i].hand += [starting_cards[2*i],starting_cards[1+2*i]]

    def player_takes_new_card(self, player_index):
        new_card = self.deck.take_cards(1)
        self.players[player_index].hand+=(new_card)

    def check_round(self):
        for player in (self.players):
            total_amount = 0
            ace_amount = 0
            for card in player.hand:
                card_value = card[0] if (card[0]<11) else 10
                total_amount += card_value
                if(card[0] == 1):
                    ace_amount += 1
            posibilities = [(total_amount + i*10) for i in range(ace_amount+1)]
            still_alive = False
            max_under_22 = 0
            for value in posibilities:
                if(value < 22):
                    max_under_22 = value
                    still_alive = True
            player.result = max_under_22
            player.still_alive = still_alive
        number_of_winners = 0
        for this_player in self.players:
            number_of_winners = number_of_winners+1 if(this_player.still_alive) else number_of_winners
        if(number_of_winners == 1 or number_of_winners == 0):
            self.game_over = True

    #Simple method that considers if taking another card is a good idea.
    def bot_logic(self, player_index):
        take_card_flag = False
        current_points = self.players[player_index].result
        if(current_points < 15):
            take_card_flag = True
        if(current_points == 15):
            take_card_flag = True
        if(current_points == 16):
            if(random.random()<(5/13)):
                take_card_flag = True
            else:
                self.will_continue = False
        if(current_points == 17):
            if(random.random()<(4/13)):
                take_card_flag = True
            else:
                self.will_continue = False
        if(current_points == 18):
            if(random.random()<(3/13)):
                take_card_flag = True
            else:
                self.will_continue = False
        if(current_points == 19):
            if(random.random()<(2/13)):
                take_card_flag = True
            else:
                self.will_continue = False
        if(current_points == 20):
            if(random.random()<(1/13)):
                take_card_flag = True
            else:
                self.will_continue = False
        if(current_points == 21):
            self.will_continue = False
        return(take_card_flag)
    
    def session_object(self):
        deck_list = []
        for card in self.deck.deck:
            for element in card:
                deck_list.append(element)
        player_1_hand_list = []
        player_2_hand_list = []
        for card in self.players[0].hand:
            for element in card:
                player_1_hand_list.append(element)
        for card in self.players[1].hand:
            for element in card:
                player_2_hand_list.append(element)
        return(deck_list, player_1_hand_list, player_2_hand_list)
    
def take_previous_round(session_list):
    deck_list = session_list[0]
    first_player_round = session_list[1]
    second_player_round = session_list[2]

def reorder_list(list):
    index = 0
    output_list = []
    while(index < int(0.5*len(list))):
        output_list.append((list[2*index], list[1+2*index]))
        index += 1
    return(output_list)

if(__name__=="__main__"):
    this_game = Game(2, [], [])
    print(this_game.players[0].hand)
    print(this_game.players[1].hand)