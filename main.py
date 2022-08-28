"""
    Welcome to the Keep it Rolling game
    Rules :
     - both player will throw dice
     - who ever got the highest number on the top will win the round
     - every player has to win 10 rounds to win the game
     - the player who will win 10 rounds first wins the game

    let's KEEP IT ROLLING
"""
import random


class Die:
    """
    This class controls the characterstics and actions of a die
    Attribute(s) : score -> store the value that show up on the dice after
    rolling

    Method(s) : roll() -> perform rolling action
    """

    def __init__(self):
        self._score = None

    @property
    def score(self):
        return self._score

    def _roll(self):
        self._score = random.randint(1, 6)
        return self.score


class Player:
    """
    This class controls the characterstics and actions of a player
    Attribute(s) : die -> instance of Die class
                 : _is_computer -> tells that the player is
                                   computer(True) or human(False)
                 : _counter -> it counts the number of wins of each player

    Method(s) : decrement_counter() -> used to decrement the counter
              : roll_die() -> used to roll the die for a partcular player
    """

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def _decrement_counter(self):
        self._counter -= 1

    def _roll_die(self):
        return self._die._roll()


class DiceGame:
    """
    This class controls the game flow
    Attribute(s) : human -> human player instance of player class
                 : computer -> computer player instance of player class

    Method(s) : play() -> launch the game
              : play_round() -> launch a new round
              : check_game_over -> checking whether game is over or not
              : print_round_welcome() -> print the welcome message after
                                         every launch of the new round
              : show_dice() -> shows what number on dice showed up after
                               rolling
              : show_counters() -> shows how many wins are needed for
                                   each player
              : show_game_over() -> shows game over text
              : play_again() -> prompts whether or not you want to play agian
                                or exit
    """

    def __init__(self, human, computer):
        self._human = human
        self._computer = computer

    def play(self):
        print("\n==============================")
        print("🎲 Welcome to KEEP it ROLLING! 🎲")
        print("==============================")
        while True:
            self._play_round()
            game_over = self._check_game_over()
            if game_over:
                break
        self._play_again()

    def _play_round(self):
        self._print_round_welcome()
        human_score = self._human._roll_die()
        computer_score = self._computer._roll_die()
        self._show_dice(human_score, computer_score)
        if human_score > computer_score:
            print("🎉 You won this round! Congrats! 🎉")
            self._human._decrement_counter()
        elif computer_score > human_score:
            print("🙁 The computer won this round. Try again! 🙁")
            self._computer._decrement_counter()
        else:
            print("😮 You and the computer have tied! 😮")
        self._show_counters()

    def _print_round_welcome(self):
        print("\n------------- New Round -------------")
        input("🎲 Press any key to roll the dice. 🎲")

    def _show_dice(self, human_score, computer_score):
        print(f"\nYour die: {human_score}")
        print(f"Computer die: {computer_score}\n")

    def _show_counters(self):
        print(f"\nYour counter: {self._human._counter}")
        print(f"Computer counter: {self._computer._counter}")

    def _check_game_over(self):
        if self._human._counter == 0:
            self._show_game_over(self._human)
            return True
        elif self._computer._counter == 0:
            self._show_game_over(self._computer)
            return True
        else:
            return False

    def _show_game_over(self, winner):
        print("\n========================================================")
        print("✨                      GAME OVER!                      ✨")
        print("========================================================")
        if winner.is_computer:
            print("❌ The computer won the game. Sorry! Please try again! ❌")
        else:
            print("🥂          You won the game! Congratulations!          🥂")
        print("========================================================")

    def _play_again(self):
        print("\nWould you like to play again?\n")
        response = input("Type 'y' for 'yes' and 'n' for 'no': ")
        response = response.lower()
        if response == "y":
            self._human._counter = 10
            self._computer._counter = 10
            game.play()
        elif response == "n":
            print("\n😊 Thanks for playing! Have a nice day! 😊")
        else:
            print("\nPlease input either 'y' or 'n'.")
            self._play_again()


human_die = Die()
computer_die = Die()

human_player = Player(human_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(human_player, computer_player)

game.play()
