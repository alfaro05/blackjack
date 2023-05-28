import random

class Player():
    def __init__(self, hand, still_alive, total):
        if(hand == []):
            self.hand = []
            self.still_alive = True
            self.total = 0
        else:
            self.hand = hand
            self.still_alive = still_alive
            self.total = total

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
    def __init__(self, num_players, deck, player_1_hand, player_2_hand):
        if(deck == []):
            self.deck = Deck(True, [])
            self.player_1_hand = []
            self.player_2_hand = []
        else:
            self.deck = deck
            self.player_1_hand = player_1_hand
            self.player_2_hand = player_2_hand

        self.num_players = num_players 
        # It can only work for two players, but this can be expanded.
        # A new class "Player" can be created, so Game has a list
        # of players, with their own take card method, hand, and
        # "still_alive" atributes.
        
        self.still_alive_list = [True, True] #True if a player still haven't reached 21.
        self.game_over = False
        self.start_game()

    def start_game(self):
        starting_cards = self.deck.take_cards(2*self.num_players)
        self.player_1_hand = [starting_cards[0], starting_cards[1]]
        self.player_2_hand = [starting_cards[2],starting_cards[3]]
        print (self.player_1_hand, self.player_2_hand)

    def player_1_takes_card(self):
        new_card = self.deck.take_cards(1)
        self.player_1_hand += new_card

    def player_2_takes_card(self):
        new_card = self.deck.take_cards(1)
        self.player_2_hand += new_card

    def check_round(self):
        player_index = 0 #Index to select self.still_alive
        results_list = [True, True]
        for player in (self.player_1_hand, self.player_2_hand):
            total_amount = 0
            ace_amount = 0
            for card in player:
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
            results_list[player_index] = max_under_22
            self.still_alive_list[player_index] = still_alive
            player_index += 1
        if(self.still_alive_list[0] and self.still_alive_list[1]):
            self.game_over = False
        else:
            self.game_over = True

    def bot_logic(self):
        pass

if(__name__=="__main__"):
    this_game = Game(2, [], [], [])
    this_game.player_1_takes_card()
    this_game.player_2_takes_card()
    this_game.check_round()
    print(this_game.player_1_hand)
    print(this_game.player_2_hand)
    print(this_game.still_alive_list, this_game.player_1_hand, this_game.player_2_hand)