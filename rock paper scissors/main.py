import random


class Game:
    def com_choice(self, com):
        computer = ""
        if com == 1:
            computer = "rock"
        elif com == 2:
            computer = "paper"
        elif com == 3:
            computer = "scissor"
        return computer

    def rules(self, com, user):
        result = ""
        if com == 1 and user == "p" or (com == 2 and user == "s") or (com == 3 and user == "r"):
            result = "You Win"
        elif com == 1 and user == "s" or (com == 2 and user == "r") or (com == 3 and user == "p"):
            result = "You lose"
        elif com == 1 and user == "r" or (com == 2 and user == "p") or (com == 3 and user == "s"):
            result = "Draw"
        else:
            print("Wrong Answer")
            Game().game_function()
        return result

    def game_function(self):
        again = True
        while again:
            # 1 for rock, 2 for paper, 3 for scissor
            print("r = rock\t p = paper\t s = scissor")
            user = input("your turn : ").lower()
            com = random.randint(1, 3)
            computer = Game().com_choice(com)
            result = Game().rules(com, user)
            if result != "":
                print(f"\ncom = {computer}")
            else:
                pass

            print(result)

            wrong = True
            while wrong:
                wanna_play = input("Wanna play again? (Y/N)").lower()
                if wanna_play == "y":
                    again = True
                    wrong = False
                elif wanna_play == "n":
                    again = False
                    wrong = False
                else:
                    print("Wrong Answer")
                    wrong = True
            pass
        print("GOOD BYE")


Game().game_function()
