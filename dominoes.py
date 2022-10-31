import random


def domino_gen():
    dominoes_0 = [[0 for x in range(2)] for _ in range(7)]
    for x in range(0, 7):
        dominoes_0[x][1] = x
    dominoes_1 = [[1 for x in range(2)] for _ in range(6)]
    for x in range(0, 6):
        dominoes_1[x][1] = x + 1
    dominoes_2 = [[2 for x in range(2)] for _ in range(5)]
    for x in range(0, 5):
        dominoes_2[x][1] = x + 2
    dominoes_3 = [[3 for x in range(2)] for _ in range(4)]
    for x in range(0, 4):
        dominoes_3[x][1] = x + 3
    dominoes_4 = [[4 for x in range(2)] for _ in range(3)]
    for x in range(0, 3):
        dominoes_4[x][1] = x + 4
    dominoes_5 = [[5 for x in range(2)] for _ in range(2)]
    for x in range(0, 2):
        dominoes_5[x][1] = x + 5
    dominoes_6 = [[6, 6]]
    dominoes = dominoes_0 + dominoes_1 + dominoes_2 + dominoes_3 + dominoes_4 + dominoes_5 + dominoes_6
    return dominoes


def random_dominoes(dominoes):
    computer = []
    player = []
    for _ in range(7):
        computer.append(random.choice(dominoes))
        dominoes = [i for i in dominoes if i not in computer]
        player.append(random.choice(dominoes))
        dominoes = [i for i in dominoes if i not in player]
    stock = [i for i in dominoes]
    return computer, player, stock


def domino_snake(computer, player):
    player_double = []
    computer_double = []
    p = False
    c = False
    status = ""
    for x in range(7):
        if player[x][0] == player[x][1]:
            player_double.append(player[x])
            p = True
        if computer[x][0] == computer[x][1]:
            computer_double.append(computer[x])
            c = True
    if p and c:
        if max(player_double) > max(computer_double):
            domino_snake = [max(player_double)]
            player = [i for i in player if i not in domino_snake]
            status = "computer"
        if max(computer_double) > max(player_double):
            domino_snake = [max(computer_double)]
            computer = [i for i in computer if i not in domino_snake]
            status = "player"
    elif p:
        domino_snake = [max(player_double)]
        player = [i for i in player if i not in domino_snake]
        status = "computer"
    elif c:
        domino_snake = [max(computer_double)]
        computer = [i for i in computer if i not in domino_snake]
        status = "player"
    if not p and c:
        return False
    else:
        return domino_snake, status, computer, player


def computer_move(computer, domino_snake, stock):
    number_sum = []
    domino_values = []
    for i in range(7):
        number_sum.append(sum(x.count(i) for x in computer) + sum(x.count(i) for x in domino_snake))
    for i in range(len(computer)):
        domino_values.append(number_sum[computer[i][0]] + number_sum[computer[i][1]])
    while True:
        if len(domino_values) != 0:
            highest_value_index = domino_values.index(max(domino_values))
            computer_input = highest_value_index + 1
        else:
            computer_input = 0
        if computer_input == 0:
            if len(stock) != 0:
                computer.append(stock[random.randint(0, len(stock) - 1)])
                stock = [i for i in stock if i not in computer]
                status = "player"
                no_move_pc = False
                break
            elif len(stock) == 0:
                status = "player"
                no_move_pc = True
                break
        elif 0 < computer_input <= len(computer):
            if any(x in domino_snake[len(domino_snake) - 1] for x in computer[computer_input - 1]):
                if computer[computer_input - 1][0] == domino_snake[len(domino_snake) - 1][1]:
                    domino_snake.append(computer[computer_input - 1])
                    computer = [i for i in computer if i not in domino_snake]
                    status = "player"
                    no_move_pc = False
                    break
                elif computer[computer_input - 1][1] == domino_snake[len(domino_snake) - 1][1]:
                    computer[computer_input - 1][0], computer[computer_input - 1][1] = computer[computer_input - 1][1], \
                                                                                    computer[computer_input - 1][0]
                    domino_snake.append(computer[computer_input - 1])
                    computer = [i for i in computer if i not in domino_snake]
                    status = "player"
                    no_move_pc = False
                    break
            if any(x in domino_snake[0] for x in computer[abs(computer_input) - 1]):
                if computer[abs(computer_input) - 1][1] == domino_snake[0][0]:
                    domino_snake.insert(0, computer[abs(computer_input) - 1])
                    computer = [i for i in computer if i not in domino_snake]
                    status = "player"
                    no_move_pc = False
                    break
                elif computer[abs(computer_input) - 1][0] == domino_snake[0][0]:
                    computer[abs(computer_input) - 1][0], computer[abs(computer_input) - 1][1] = \
                    computer[abs(computer_input) - 1][1], computer[abs(computer_input) - 1][0]
                    domino_snake.insert(0, computer[abs(computer_input) - 1])
                    computer = [i for i in computer if i not in domino_snake]
                    status = "player"
                    no_move_pc = False
                    break
                else:
                    del domino_values[highest_value_index]
                    continue
            else:
                del domino_values[highest_value_index]
                continue
    return computer, domino_snake, stock, status, no_move_pc
        

while True:
    dominoes = domino_gen()
    computer, player, stock = random_dominoes(dominoes)
    if domino_snake(computer, player):
        domino_snake, status, computer, player = domino_snake(computer, player)
        break
    else:
        continue

no_move_pc = False
no_move_p = False

while True:
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print()
    if len(domino_snake) > 6:
        for i in range(3):
            if i == 2:
                print(domino_snake[i], end="...")
            else:
                print(domino_snake[i], end="")
        for i in range(len(domino_snake) - 3, len(domino_snake)):
            print(domino_snake[i], end="")
    else:
        for element in domino_snake:
            print(element, end="")
    print("\n")
    print("Your pieces:")
    for i in range(len(player)):
        print(f"{i + 1}:{player[i]}")
    print()
    if (len(player) == 0 and len(computer) == 0) or (no_move_p and no_move_pc):
        print("Status: The game is over. It's a draw!")
        break
    elif len(player) == 0:
        print("Status: The game is over. You won!")
        break
    elif len(computer) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        while True:
            player_input = input()
            if player_input == "":
                computer, domino_snake, stock, status, no_move_pc = computer_move(computer, domino_snake, stock)
                break
            else:
                print("Invalid input. Please try again.")
                continue
    elif status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
        while True:
            player_input = input()
            try:
                player_input = int(player_input)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            if player_input != 0:
                if 0 < player_input <= len(player):
                    if any(x in domino_snake[len(domino_snake) - 1] for x in player[player_input - 1]):
                        if player[player_input - 1][0] == domino_snake[len(domino_snake) - 1][1]:
                            domino_snake.append(player[player_input - 1])
                            player = [i for i in player if i not in domino_snake]
                            status = "computer"
                            no_move_p = False
                            break
                        elif player[player_input - 1][1] == domino_snake[len(domino_snake) - 1][1]:
                            player[player_input - 1][0], player[player_input - 1][1] = player[player_input - 1][1], \
                                                                                    player[player_input - 1][0]
                            domino_snake.append(player[player_input - 1])
                            player = [i for i in player if i not in domino_snake]
                            status = "computer"
                            no_move_p = False
                            break
                    else:
                        print("Illegal move. Please try again.")
                        continue
                elif -len(player) <= player_input < 0:
                    if any(x in domino_snake[0] for x in player[abs(player_input) - 1]):
                        if player[abs(player_input) - 1][1] == domino_snake[0][0]:
                            domino_snake.insert(0, player[abs(player_input) - 1])
                            player = [i for i in player if i not in domino_snake]
                            status = "computer"
                            no_move_p = False
                            break
                        elif player[abs(player_input) - 1][0] == domino_snake[0][0]:
                            player[abs(player_input) - 1][0], player[abs(player_input) - 1][1] = player[abs(player_input) - 1][1], player[abs(player_input) - 1][0]
                            domino_snake.insert(0, player[abs(player_input) - 1])
                            player = [i for i in player if i not in domino_snake]
                            status = "computer"
                            no_move_p = False
                            break
                        else:
                            print("Illegal move. Please try again.")
                            continue
                    else:
                        print("Illegal move. Please try again.")
                        continue
                else:
                    print("Invalid input. Please try again.")
                    continue
            elif player_input == 0:
                if len(stock) != 0:
                    player.append(stock[random.randint(0, len(stock) - 1)])
                    stock = [i for i in stock if i not in player]
                    status = "computer"
                    no_move_p = False
                    break
                elif len(stock) == 0:
                    status = "computer"
                    no_move_p = True
                    break            