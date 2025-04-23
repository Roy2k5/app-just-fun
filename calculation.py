import pygame
pygame.init()
# setting color
BACKGROUND = (214, 214, 214)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# helper funcion
def text_in_py(word, size = 60, color = WHITE):
	font1 = pygame.font.SysFont("san", size)
	return font1.render(word, True, color)
def cal_list(list_number, list_notation):
	temp = list_number[0]
	for i in range(len(list_notation)):
		if list_notation[i] == "+":
			temp = temp + list_number[i + 1]
		elif list_notation[i] == "-":
			temp = temp - list_number[i + 1]
		elif list_notation[i] == "/":
			temp = temp / list_number[i + 1]
		else:
			temp = temp * list_number[i + 1]
	return temp
# Setting text
text_plus = text_in_py("+")
text_sub = text_in_py("-")
text_div = text_in_py("/")
text_mul = text_in_py("x")
notation_str = ["+", "-", "x", "/"] 
notations = [text_plus, text_sub, text_mul, text_div]
text_result = text_in_py("Result")
text_clear = text_in_py("Clear")
zero_number = text_in_py(str(0))
text_ans = text_in_py("ans", 30)

	
numbers = []
for i in range(1, 10):
	numbers.append(text_in_py(str(i)))
# Start program





font = pygame.font.SysFont("sans", 40)
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Calculation")
running = True
clock = pygame.time.Clock()
result_list = []
result = None
notate_list = []
number_list = []
number = 0
string_answer = None
while(running):
	clock.tick(60)
	screen.fill(BACKGROUND)
	# screen  of calculation
	pygame.draw.rect(screen, BLACK, (50, 50, 400, 200))
	# button
	for i in range(3):
		for j in range(3):
			pygame.draw.rect(screen, BLACK, (50 + 75*j, 275 + 75*i , 50, 50))
			screen.blit(numbers[i*3 + j], (60 + 75*j, 275 + 75*i))
	pygame.draw.rect(screen, BLACK, (125, 500, 50, 50))
	screen.blit(zero_number, (135, 500))

	pygame.draw.rect(screen, BLACK, (200, 500, 50, 50))
	screen.blit(text_ans, (210, 500))
	# operation
	for i in range(4):
		pygame.draw.rect(screen, BLACK, (275, 275 + 75*i , 50, 50))
		screen.blit(notations[i], (285, 275 + 75*i))	
	# result
	pygame.draw.rect(screen, BLACK, (350, 275 , 140, 50))
	screen.blit(text_result, (360, 275))
	pygame.draw.rect(screen, WHITE, (60, 160, 380, 80))
	screen.blit(text_in_py("Result", 40), (70, 125))
	# Clear
	pygame.draw.rect(screen, BLACK, (350, 350 , 140, 50))
	screen.blit(text_clear, (360, 350))

	result_string = " ".join(str(x) for x in result_list)
	result_sur = text_in_py(result_string)
	screen.blit(result_sur, (60, 50))
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# Event in app
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			for i in range(3):
				for j in range(3):
					if mouse_x < 100 + j * 75 and mouse_x > 50 + j * 75 and mouse_y > 275 + 75 * i and mouse_y < 325 + 75 * i:
						result_list.append(i * 3 + j + 1)
						number = number*10 + (i * 3 + j + 1)
			if mouse_x > 125 and mouse_x < 175 and mouse_y > 500 and mouse_y < 550:
				result_list.append(0)
				number = number*10 + (0)
			for i in range(4):
				if mouse_x > 275 and mouse_x < 325 and mouse_y > 275 + 75*i and mouse_y < 325 + 75 * i:
					result_list.append(notation_str[i])
					number_list.append(number)
					number = 0
					notate_list.append(notation_str[i])
			if mouse_x > 350 and mouse_x < 490 and mouse_y > 275 and mouse_y < 325:
				number_list.append(number)
				number = 0
				result = cal_list(number_list, notate_list)
				string_answer = text_in_py(str(result), 60, BLACK)
			if mouse_x > 350 and mouse_x < 490 and mouse_y > 350 and mouse_y < 400:
				result_list = []
				result = None
				notate_list = []
				number_list = []
				number = 0
				string_answer = None
				
	if string_answer is not None:
		screen.blit(string_answer, (70, 180))


	pygame.display.flip()

pygame.quit()
