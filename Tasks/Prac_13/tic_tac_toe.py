import os


class Cell:
    def __init__(self, num):
        self.num = num
        self.symbol = ' '

    def __str__(self):
        return self.symbol


class Board:
    def __init__(self):
        self.cells = []
        for i in range(9):
            self.cells.append(Cell(i + 1))

    def display(self):
        for i in range(3):
            print('-------------')
            out = '| '
            for j in range(3):
                out += str(self.cells[i * 3 + j]) + ' | '
            print(out)
        print('-------------')

    def update(self, cell_num, symbol):
        if self.cells[cell_num - 1].symbol == ' ':
            self.cells[cell_num - 1].symbol = symbol
            return True
        else:
            return False

    def is_game_over(self):
        for i in range(3):
            if self.cells[i * 3].symbol == self.cells[i * 3 + 1].symbol == self.cells[i * 3 + 2].symbol and self.cells[i * 3].symbol != ' ':
                return True
        for i in range(3):
            if self.cells[i].symbol == self.cells[i + 3].symbol == self.cells[i + 6].symbol and self.cells[i].symbol != ' ':
                return True
        if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol and self.cells[0].symbol != ' ':
            return True
        if self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol and self.cells[2].symbol != ' ':
            return True
        for cell in self.cells:
            if cell.symbol == ' ':
                return False
        return True


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def get_move(self):
        try:
            cell_num = int(input(self.name + ', введите номер клетки: '))
            if cell_num < 1 or cell_num > 9:
                raise ValueError
            else:
                return cell_num
        except ValueError:
            print('Введите правильный номер клетки.')
            return self.get_move()


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1

    def play_turn(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.current_player.name + '\'s turn:\n')
        self.board.display()
        cell_num = self.current_player.get_move()
        while not self.board.update(cell_num, self.current_player.symbol):
            print('Данная клетка занята.')
            cell_num = self.current_player.get_move()

        if self.board.is_game_over():
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self.current_player.name + ' wins!\n')
            self.board.display()
            self.current_player.score += 1
            return True

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return False

    def play_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.board = Board()
        self.current_player = self.player1
        while not self.board.is_game_over():
            if self.play_turn():
                break

        print('Score:')
        print(self.player1.name + ': ' + str(self.player1.score))
        print(self.player2.name + ': ' + str(self.player2.score))


while True:
    player1 = Player('Игрок 1', 'X')
    player2 = Player('Игрок 2', 'O')
    game = Game(player1, player2)
    game.play_game()

    again = input('Хотите ли продолжить игру(да/нет): ')
    if again.lower() != 'да':
        break

print('Спасибо за игру!')
