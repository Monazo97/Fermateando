import pygame, random, math
from random import randint

WIDTH = 600
HEIGHT = 600

VERDE = (19, 111, 67)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fermateando")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
pregunta_font = pygame.font.Font('freesansbold.ttf', 64)
textX = 10
testY = 10

#Variables

lives = 3
pos = randint(0,11)



# ~ queries = ["1 + 1 = ", "2 + 1 - 2 = ", "3 + 2 - 1 = ",
			# ~ "1 - 2 + 3 = ", "2 + 3 - 2 = "]

# ~ answer = [2, 1, 4, 2, 3]

archivo = open("test.in","r")

queries = [0] * 1000
answer = [0] * 1000

line = 0

for linea in archivo.readlines():
	queries[line], answer[line] = linea.split("=")
	queries[line] += "= "
	answer[line] = answer[line][1:-1]
	answer[line] = answer[line]
	line += 1
	
archivo.close()

# Logo

logoImg = pygame.image.load('f.png')
logoImg = pygame.transform.scale(logoImg,(200,200))
wrong = pygame.image.load('wrong.png')
wrong = pygame.transform.scale(wrong,(100,100))
correct = pygame.image.load('correct.png')
correct = pygame.transform.scale(correct,(100,100))

# Timer

counter, text_counter = 45, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT,1000)

def show_score(x,y):
	score = font.render("Score : " + str(score_value),True, (255,255,255))
	screen.blit(score,(x,y))
	
def game_over_text():
	over_text = over_font.render("GAME OVER", True, WHITE)
	screen.blit(over_text,(125,250))
	restart_text = font.render("Press 'R' to restart", True, WHITE)
	screen.blit(restart_text,(180,325))
	
def show_logo(x,y):
	screen.blit(logoImg,(x,y))

def show_query(idx):
	pregunta = pregunta_font.render(queries[idx],True,WHITE)
	# ~ pregunta = pregunta_font.render(answer[idx],True,WHITE)
	screen.blit(pregunta,(100,250))
	
def show_timer():
	cur_time = font.render("Time : " + str(counter), True, WHITE)
	screen.blit(cur_time,(450,20))
	
def show_lives():
	aux_pos = [(10,500), (120,500), (230,500)]
	for i in range(0,3-lives):
		screen.blit(wrong,aux_pos[i])

def show_correct():
	screen.blit(correct,(250,350))
	
def show_wrong():
	screen.blit(wrong,(250,350))
	
def show_before_game():
	titulo = font.render("Press 'SPACE' to start", True, WHITE)
	screen.blit(titulo,(150,300))
	

start_time = 0
passed_time = 10
last = 0
started = 0

running = True
while running:
	clock.tick(60)
	
	all_sprites.update()
	screen.fill(VERDE)
	all_sprites.draw(screen)
	pygame.display.flip()
	show_score(textX, testY)
	show_timer()
	show_logo(400,400)
	show_lives()
	
	if started == 0:
		show_before_game()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = false
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					started = 1
		pygame.display.update()
		continue
	
	
	
	if(lives <= 0 or counter <= 0):
		game_over_text()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					lives = 3
					counter = 45
					score_value = 0
					started = 0
					pos = randint(0,11)
	else:
		show_query(pos)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					last = 1
					number = pregunta_font.render(str(last),True,WHITE)
					screen.blit(number,(500,250))
					if answer[pos] == "1":
						show_correct()
						score_value += 1
						pygame.display.update()
						pygame.time.delay(500)
					else:
						lives -= 1
						show_wrong()
						pygame.display.update()
						pygame.time.delay(500)
					# ~ pos += 1
				if event.key == pygame.K_2:
					last = 2
					number = pregunta_font.render(str(last),True,WHITE)
					screen.blit(number,(500,250))
					if answer[pos] == "2":
						show_correct()
						score_value += 1
						pygame.display.update()
						pygame.time.delay(500)
					else:
						lives -= 1
						show_wrong()
						pygame.display.update()
						pygame.time.delay(500)
					# ~ pos += 1
				if event.key == pygame.K_3:
					last = 3
					number = pregunta_font.render(str(last),True,WHITE)
					screen.blit(number,(500,250))
					if answer[pos] == "3":
						show_correct()
						score_value += 1
						pygame.display.update()
						pygame.time.delay(500)
					else:
						lives -= 1
						show_wrong()
						pygame.display.update()
						pygame.time.delay(500)
					# ~ pos += 1
				if event.key == pygame.K_4:
					last = 4
					number = pregunta_font.render(str(last),True,WHITE)
					screen.blit(number,(500,250))
					if answer[pos] == "4":
						show_correct()
						score_value += 1
						pygame.display.update()
						pygame.time.delay(500)
					else:
						lives -= 1
						show_wrong()
						pygame.display.update()
						pygame.time.delay(500)
					# ~ pos += 1
				latest = pos
				if score_value < 5:
					while pos == latest:
						pos = randint(0,11)
				elif score_value < 13:
					while pos == latest:
						pos = randint(12,29)
				else:
					while pos == latest:
						pos = randint(30,44)
			if event.type == pygame.USEREVENT:
				counter -= 1
		
	pygame.display.update()
	
	
#pygame.quit()
