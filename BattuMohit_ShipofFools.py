from random import randint


class Die:
    """
    Responsible for handling
    randomly generated integer
    values between 1 and 6.
    """
    def __init__(self):
        # value is initialised to 0
        self._value = 0
        
    def roll(self):
        """
        Task is to assign a new random number to
        the _value attribute of an object.
        The method should not return anything.
        """
        self._value = randint(1, 6)
        
    def get_value(self):
        # Returns the value of the attribute _value.
        return self._value


class DiceCup:
    """
    Handles five objects (dice) of class Die.
    Has the ability to bank and release dice individually.  
    Can also roll dice that are not banked.
    """
    def __init__(self):
        # Five objects of the class Die are put in the list.
        # Here we initialised with False Objects 5 times.
        self.Lost = [False for i in range(5)]
        self.dice1 = Die()
        self.dice2 = Die()
        self.dice3 = Die()
        self.dice4 = Die()
        self.dice5 = Die()
        self.__dice = [self.dice1, 
                       self.dice2, self.dice3, 
                       self.dice4, self.dice5]

    def roll(self):
        """
        It is rolling dice that are not banked in 
        the for-loop you need to add an
        if statement to decide whether a specific
        die should be rolled or not.
        """
        for dice in self.__dice:
            i = self.__dice.index(dice)
            if self.Lost[i] is False:
                self.__dice[i].roll()
                
    def value(self, index):
        """
        It returns the values from the given index
        value present in the dice list.
        """
        return self.__dice[index].get_value()
        
    def release_all(self):
        # Deletes the banked element.
        # Creates a new element list.
        for index in range(5):
            self.Lost[index] = False
            
    def release(self, index):
        # It removes one of the banked element in the list.
        self.Lost[index] = False
        
    def bank(self, index):
        # According to the given index that particular element is banked.
        self.Lost[index] = True
        
    def is_banked(self, index):
        """
        If index is present in banked list then
        it will return true or else it will return false.
        """
        if self.Lost[index] is False:
            print('Not Banked')
        else:
            print('Banked')


class ShipOfFoolsGame:
    """
    Responsible for the game logic and has the
    ability to play a round of the game 
    resulting in a score.Also has a property that tells what 
    accumulated score results in a winning state, for example 21.
    """
    def __init__(self):
            self.__winning_score = 21
            self._dicecup = DiceCup()

    def round(self):
        """
        Since each player has got 3 chances
        We are using for loop to iterate over the 3 chances.
        Here we are banking the numbers of 6,5 and 4.
        The total score of the player in that
        3 chances are also calculated and returned here.
        """
        has_ship, has_captain, has_crew = False, False, False
        
        self.score_crew = 0

        for round in range(3):
            global dice
            self._dicecup.roll()
            self.dice = [self._dicecup.dice1.get_value(),
                         self._dicecup.dice2.get_value(), 
                         self._dicecup.dice3.get_value(), 
                         self._dicecup.dice4.get_value(), 
                         self._dicecup.dice5.get_value()]
            
            print(self.dice)
            if not has_ship and 6 in self.dice:
                self._dicecup.bank(self.dice.index(6))
                has_ship = True
            if has_ship and not has_captain and 5 in self.dice:
                self._dicecup.bank(self.dice.index(5))
                has_captain = True
            if has_captain and not has_crew and 4 in self.dice:
                
                self._dicecup.bank(self.dice.index(4))
                has_crew = True
            if has_ship and has_captain and has_crew:
                for x in range(5):
                    if self.dice[x] > 3:
                        self._dicecup.bank(x)
        if has_ship and has_captain and has_crew:
            # It will calculate the score of a dice6
            self.score_crew = sum(self.dice) - 15
            self._dicecup.release_all()

    def get_win(self):
        # It will return the score limit
        return self.__winning_score
            
                               
class PlayRoom:
    """
    Responsible for handling a number of players and a game.
    Every round the room lets each player play, and 
    afterwards check if any player have reached the winning score.
    """
    def __init__(self):
        self.scr = [0, 0]
        self._player_games = []

    def set_game(self, game) -> None:
        # just enter the name without paranthesis
        # Here we have initialised the players as empty list.
        self.game1 = game
        if self.game1.__doc__ == ShipOfFoolsGame.__doc__:
            print("Game Started!!\n")
        else:
            print('Game not Found!\n')
        
    def add_player(self, player_name):
        # just enter the name without paranthesis
        # Here we have initialised the players as empty list.
        self.gamer_name = player_name
        self._player_games.append(self.gamer_name)

    def reset_scores(self):
        # The scores of the players have been reset by making a score to 0.
        for i in range(2):
            self._player_games[i].score = 0
            
    def play_round(self):
        """
        This will iterate through "n" number of rounds till one of the player
        reaches to the ultimate score of 21 points.
        """
        for i in range(2):
            self._player_games[i].play_round(self.game1)
            
    def game_finished(self):
        # Here the game is played till 21 score.
        if max(self.scr) > self.game1.get_win():
            return True
        else:
            return False
            
    def print_scores(self):
        # It will print out the scores of the two players.
        for i in range(len(self._player_games)):
            player_score = self._player_games
            self.scr[i] = player_score[i].score
            print(player_score[i].name, player_score[i].score)
            
    def print_winner(self):
        # Here it will print out the final winner of the game
        maximum_score = max(self.scr)
        evaluated_score = self.scr.index(maximum_score)
        self.print_wn = self._player_games[evaluated_score].name
        print(f"The Winner is", self.print_wn)
        
        
class Player:
    """
    Responsible for the score of the individual player.
    Has the ability, given a game logic, play a round of a game. 
    The gained score is accumulated in the attribute score.
    """
    def __init__(self, name):
        # Initialised a name variable and score variable
        self.score = 0
        self.name = name
        
    def set_name(self, name):
        # The name of each player is set here using a list.
        self._name = name

    def current_score(self):
        # Displays a Current Score
        return self._score
        
    def reset_score(self):
        # The scores are reset to 0.
        self.score = 0
        
    def play_round(self, playername):
        # Here the players are played for 3 chances
        # Score of each player are calculated and accumulated in every round
        # The max limit of the score is set to 21
        self.values = playername
        self.values.round()
        self.score = self.score+self.values.score_crew
        print()

    def get_name(self):
        # Gets the player name
        return self._name

if __name__ == "__main__":
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame())
    room.add_player(Player("Ling"))
    room.add_player(Player('Chang'))
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()





