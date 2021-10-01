import pygame 
pygame.init()
width=1900
height=1000
screen=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
text=pygame.font.SysFont("Bahnschrift SemiBold",142)
blue=(0,0,180)
square=pygame.Surface((50,50))
white=(255,255,255)
red=(255,0,0)
class  Racket :
 	def __init__(self,x):
 		self.x=x
 		self.y=height//2
 		self.width=50
 		self.height=170
 		self.speed=120
 		self.score=0
 	def render(self):
 		pygame.draw.rect(screen,white,(self.x,self.y,self.width,self.height))
 	def up(self):
 		if self.y-self.speed>=0:
 			self.y-=self.speed
 	def down(self):
 		if self.y+self.height+self.speed<=height:
 			self.y+=self.speed
 	def setscore(self):
 		self.score+=1
class  Ball :
 	def __init__(self):
 		self.x=width//2
 		self.pop=pygame.mixer.Sound("pop.ogg")
 		self.y=height//2
 		self.radius=30
 		self.side_x=0
 		self.side_y=0
 		self.speed_x=2
 		self.speed_y=1
 	def render(self):
 		self.move()
 		pygame.draw.circle(screen,white,(self.x,self.y),self.radius)
 	def default(self):
 		self.x=width//2
 		self.y=height//2
 		self.side_x=0
 	def move(self):
 		if self.x+self.radius>=width:
 			self.side_x=0
 		elif self.x-self.radius<=0:
 			self.side_x=1
 		if self.side_x:
 			self.x+=self.speed_x
 		else:
 			self.x-=self.speed_x
 		if self.y+self.radius>=height:
 			self.side_y=0
 		elif self.y-self.radius<=0:
 			self.side_y=1
 		if self.side_y:
 			self.y+=self.speed_y
 		else:
 			self.y-=self.speed_y
class Restart:
	def __init__(self):
		self.image=pygame.image.load("restart.png")
		self.size=self.image.get_size()
		self.x=width//2-self.size[0]//2
		self.y=height//2-self.size[1]//2
		self.clicked=1
	def render(self):
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		screen.blit(self.image,self.rect)
	def default(self):
		self.clicked=1
	def click(self,pos):
		x_mouse=pos[0]
		y_mouse=pos[1]
		if self.clicked and x_mouse > self.x and x_mouse < self.x + self.size[0] and y_mouse > self.y and y_mouse < self.y + self.size[1]:
			self.clicked=0
			restart_game()
def restart_game():
	ball.default()
	restart.default()
	left_racket.score=0
	right_racket.score=0



left_racket=Racket(30)
right_racket=Racket(width-50-30)
ball=Ball()
restart=Restart()
multiplayer=1
indents=[100,161,224,286]
while True:
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN:
			pos=pygame.mouse.get_pos()
			restart.click(pos)
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				pygame.quit()
			elif event.key==pygame.K_m:
				multiplayer+=1
			elif event.key==pygame.K_w and not multiplayer %2:
				left_racket.up()
			elif event.key==pygame.K_s and not multiplayer %2:
				left_racket.down()
			elif event.key==pygame.K_UP:
				right_racket.up()
			elif event.key==pygame.K_DOWN:
				right_racket.down()
	screen.fill(blue)
	for y in range (145,height,100):
		pygame.draw.rect(screen,white,(width//2-10,y,20,70))
	if ball.x+ball.radius>=width or ball.x-ball.radius<=0:
		screen.fill(red)
		restart.render()
	else:
		if ball.x-ball.radius<=left_racket.x+left_racket.width and ball.x-ball.radius>left_racket.x and ball.y-ball.radius>=left_racket.y and ball.y+ball.radius<=left_racket.y+left_racket.height:
			ball.side_x=1
			ball.pop.play()
			left_racket.setscore()
		if ball.x+ball.radius>=right_racket.x and ball.x+ball.radius<right_racket.x+right_racket.width and ( ball.y-ball.radius>right_racket.y and ball.y-ball.radius<=right_racket.y+right_racket.height or  ball.y+ball.radius>right_racket.y and ball.y+ball.radius<=right_racket.y+right_racket.height):
			ball.side_x=0
			ball.pop.play()
			ball.x=right_racket.x-ball.radius-10
			right_racket.setscore()
		if multiplayer%2:
			left_racket.y=ball.y-left_racket.height//2
		left_racket.render()
		right_racket.render()
		ball.render()
		left_racket_text=text.render(str(left_racket.score),True,white)
		screen.blit(left_racket_text,(width//2-indents[len(str(left_racket.score))-1],30))
		right_racket_text=text.render(": "+str(right_racket.score),True,white)
		screen.blit(right_racket_text,(width//2-20,30))
	pygame.display.flip()






















































































































































































































































