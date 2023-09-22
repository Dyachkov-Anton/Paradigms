#Контекст
#Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
#время реализовать её. Два игрока по очереди ставят крестики
#и нолики на игровое поле. Игра завершается когда кто-то
#победил, либо наступила ничья, либо игроки отказались
#играть.

#Задача
#Написать игру в “Крестики-нолики”. Можете использовать
#любые парадигмы, которые посчитаете наиболее
#подходящими. Можете реализовать доску как угодно - как
#одномерный массив или двумерный массив (массив массивов).
#Можете использовать как правила, так и хардкод, на своё
#усмотрение. Главное, чтобы в игру можно было поиграть через
#терминал с вашего компьютера.


board = list(range(1,10))

def draw_board(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")
		
def take_input(player_token):
	valid = False
	while not valid:
		player_answer = input("Куда поставим " + player_token+"? ")
		try:
			player_answer = int(player_answer)
		except:
			print ("Некорректный ввод.  Вы уверены, что ввели число?")
		if player_answer >= 1 and player_answer <= 9:
			if (str(board[player_answer-1]) not in "XO"):
				board[player_answer-1] = player_token
				valid = True
			else:
				print ("Эта клетка уже занята")
		else:
			print ("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")
			
def check_win(board):
	win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for each in win_coord:
		if board[each[0]] == board[each[1]] == board[each[2]]:
			return board[each[0]]
	return False 

def main(board):
	counter = 0
	win = False
	while not win:
		draw_board(board)
		if counter % 2 == 0:
			take_input("X")
		else:
			take_input("O")
		counter += 1
		if counter > 4:
			tmp = check_win(board)
			if tmp:
				print (tmp, "выиграл!")
				win = True
				break
		if counter == 9:
			print ("Ничья!")
			break
	draw_board(board)
	

main(board)