import pygame
pygame.init()
# helper funcion
def text_in_py(word, size = 60):
	font1 = pygame.font.SysFont("san", size)
	return font1.render(word, True, WHITE)
# setting color
BACKGROUND = (214, 214, 214)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Setting text
text_plus = text_in_py("+")
text_sub = text_in_py("-")
text_div = text_in_py("/")
text_mul = text_in_py("x")
notations = [text_plus, text_sub, text_mul, text_div]
text_result = text_in_py("Result")
	
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
	# operation
	for i in range(4):
		pygame.draw.rect(screen, BLACK, (275, 275 + 75*i , 50, 50))
		screen.blit(notations[i], (285, 275 + 75*i))	
	# result
	pygame.draw.rect(screen, BLACK, (350, 275 , 140, 50))
	screen.blit(text_result, (360, 275))
	pygame.draw.rect(screen, WHITE, (60, 160, 380, 80))
	screen.blit(text_in_py("Result", 40), (70, 125))
	
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

	pygame.display.flip()

pygame.quit()
