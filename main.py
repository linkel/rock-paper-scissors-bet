import random
import time

def main():
    print("Rock Paper Scissors Betting")
    play()


def rps(round_number):
    input_mapping = {"r": 1, "p": 2, "s": 3}
    name_mapping = {1: "rock", 2: "paper", 3:"scissors"}
    key_beats_value = {1: 3, 2: 1, 3: 2}
    key_gets_beat_by_value = {1: 2, 2: 3, 3: 1}
    selection = None
    while not selection:
        selection = input("\nEnter your play! \nr for rock, p for paper, s for scissors.")
        if selection not in ["r", "p", "s"]:
            selection = None
            print("Invalid input.")
    player_choice = input_mapping[selection]
    if round_number < 13:
        opponent_choice = random.randint(1, 3)
    else:
        opponent_choice = key_gets_beat_by_value[player_choice]
    print("You threw {0} and opponent threw {1}!".format(str(name_mapping[player_choice]), str(name_mapping[opponent_choice])))
    if opponent_choice == player_choice:
        print("It's a tie.")
        return 2
    if key_beats_value[player_choice] == opponent_choice:
        print("You won!")
        return 1
    else:
        print("You lost.")
        return 0


def play():
    round_number = 1
    player_money = 1000
    while player_money > 800:
        print("Round {0}".format(round_number))
        print("You have ${0} to gamble with. Betting $50...".format(player_money))
        outcome = rps(round_number)
        if outcome == 0:
            player_money -= 50
        elif outcome == 1:
            player_money += 50
        round_number += 1
    while player_money > 0:
        print("Round {0}".format(round_number))
        print("You have ${0} to gamble with. Betting $50...".format(player_money))
        outcome = special_rps()
        if outcome == 0:
            player_money -= 50
        elif outcome == 1:
            player_money += 50
        elif outcome == 3:
            print("You have ${0} to gamble with but no one wants to play with you.".format(player_money))
            input("Press any key to contemplate life.")
            print("I feel you.")
            time.sleep(1)
            print("Goodbye!")
            return
        round_number += 1
    if player_money == 0:
        print("Great job on playing {0} rounds of rock paper scissors before running out of cash!".format(round_number))
        print("You're either a very patient or a thoughtlessly curious person.")
        input("Press any key to reflect on this.")
        print("Have a great day.")
        return

def special_rps():
    input_mapping = {"r": 1, "p": 2, "s": 3}
    name_mapping = {1: "rock", 2: "paper", 3:"scissors"}
    key_beats_value = {1: 3, 2: 1, 3: 2}
    selection = None
    while not selection:
        selection = input("\nEnter your play! \nr for rock, p for paper, s for scissors, a to attack your opponent.")
        if selection not in ["r", "p", "s", "a"]:
            selection = None
            print("Invalid input.")
    if selection in ["r", "p", "s"]:
        opponent_choice = random.randint(1, 3)
        player_choice = input_mapping[selection]
        print("You threw {0} and opponent threw {1}!".format(str(name_mapping[player_choice]), str(name_mapping[opponent_choice])))
        if opponent_choice == player_choice:
            print("It's a tie.")
            return 2
        if key_beats_value[player_choice] == opponent_choice:
            print("You won!")
            return 1
        else:
            print("You lost.")
            return 0
    else:
        attacks = [
            "You reach across and slap your opponent across their money-grubbing weaselly face-bits.",
            "Without warning you slam a prime uppercut into your opponent's delicate little loser jaw.",
            "With great vigor you slug your opponent right in their shameless pudgy facehole.",
            "You lunge forward and smash your fist deep into your opponent's unsuspecting face."
        ]
        print("{0}".format(attacks[random.randint(0, 3)]))
        time.sleep(1)
        print('"Dude"')
        time.sleep(1)
        print('"Ow"')
        time.sleep(1)
        print('"Christ"')
        time.sleep(2)
        print('"What the fuck man"')
        time.sleep(1.5)
        print('"What the fuck is your problem?"')
        time.sleep(1)
        print('"Jesus"')
        time.sleep(2)
        print('"I\'m not putting up with this shit"')
        time.sleep(2)
        return 3

if __name__ == "__main__":
    main()
