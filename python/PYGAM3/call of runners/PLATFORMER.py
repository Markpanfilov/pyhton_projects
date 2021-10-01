from random import*
import pygame
pygame.init()
collide=0
width=1900
height=1000	
red=(255,40,30)
white= (255,244,244)
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
font=pygame.font.Font("fonts/ustroke.ttf",72)
class Runner (pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.jump_speed=10
		self.falling_speed=2
		self.x=x
		self.count_jumps=0
		self.jump=0
		self.score=0
		self.stop_score=1
		self.jump_height=500
		self.current_jump_height=0
		self.record=0
		self.get_record()
		self.y=y
		self.heartbeatsound=pygame.mixer.Sound("sounds/heartbeat.ogg")
		self.screamsounds=pygame.mixer.Sound("sounds/scream.ogg")
		self.images=[pygame.image.load("images/runer_"+str(i)+".png")for i in range(1,3)]
		for g in range(len(self.images)):
			self.width,self.height=self.images[g].get_size()
			self.images[g]=pygame.transform.scale(self.images[g],(self.width//2,self.height//2))
					
		self.i=0
		self.width,self.height=self.images[g].get_size()
		self.image=self.images[self.i]
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def update(self):
		self.jumping()
		self.i=0 if self.i else 1
		self.image=self.images[self.i]
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def last_call(self):
		if self.y + self.height > height-200:
			return False
		else:
			return True 
	def falling(self,platforms):
		if not self.jump:
			legs= self.y + self.height 
			for p in platforms:
				collide=pygame.sprite.collide_rect_ratio(1)(self,p)
				if collide:
					self.y=p.y-0-self.height
					self.eraser()
					if self.stop_score:
						self.stop_score=0
						self.score+=1
					return 1
				else:
					self.y += self.falling_speed
	def get_record(self):
		with open("record.txt") as file:
			self.record=int(file.read())
	def set_record(self,value):
		with open("record.txt","w") as file:
			file.write(str(value))
	def jumping (self):
		if self.jump:
			if self.current_jump_height>=self.jump_height:
				self.jump=0
				self.jump_speed=10
				self.current_jump_height=0
			elif self.count_jumps < 3:
				if self.current_jump_height>self.jump_height*0.5:
					if self.jump_height*0.5<self.current_jump_height<self.jump_height*0.6:
						self.jump_speed-=1
				self.y-=self.jump_speed
				self.stop_score=1
				self.current_jump_height+=self.jump_speed
			else:
				self.jump=0
	def default(self):
		self.y=0
		self.count_jumps=0
		self.jump=0
		self.score=0
		self.stop_score=1
		self.jump_height=500



	def counter (self):
		print(self.count_jumps)
		if self.count_jumps < 3:
			self.count_jumps+=1            
	def eraser (self):
		self.count_jumps=0

class Platform (pygame.sprite.Sprite):
	last=0
	def __init__(self,x,y,number):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.oldx=x
		self.oldy=y
		self.number=number
		self.move=0
		self.speed=6
		self.images=[pygame.image.load("images/"+str(i)+".png") for i in range(1,11)]
		for g in range(len(self.images)):
			self.width,self.height=self.images[g].get_size()
			self.images[g]=pygame.transform.scale(self.images[g],(self.width*2,self.height*2))
		self.image=choice (self.images)
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.width,self.height=self.image.get_size()
	def update(self):
		if self.move==1:
			self.x-=self.speed
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.moving()
	def moving (self):
		if self.x + self.width<0-self.width:
			self.x=Platform.last.x+200
			self.y=randint(250,height-250)
			self.image=choice (self.images)
			Platform.last=self
	def default (self):
		self.x=self.oldx
		self.y=self.oldy

class Background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/Gamoverscreen_1.png")
		self.width,self.height=self.image.get_size()
		self.image= pygame.transform.scale(self.image,(self.width*2,self.height*2))
		self.x=width//2
		self.y=height//2
		self.rect=self.image.get_rect(center=(self.x,self.y))
	def update(self):
		self.rect=self.image.get_rect(center=(self.x,self.y))

class Fireball (pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images=[pygame.image.load("images/fire_ball/fire_ball_"+str(i)+".png")for i in range(0,4)]
		self.i=0
		for i in range(len(self.images)):
			self.images[i]=pygame.transform.rotozoom(self.images[i],90,1)
			self.images[i]=pygame.transform.scale(self.images[i],(106,100))
		self.image=self.images[self.i]	
		self.width,self.height=self.image.get_size()
		self.x=randint(width//2,width)
		self.y=height
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def update(self):
		self.x-=5
		self.y-=10
		if self.i<len(self.images)-1:
			self.i+=1
		else:
			self.i=0
		self.image=self.images[self.i]			

		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def default(self):
		self.x=randint(width//2,width)
		self.y=height


class Explosion (pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images=[pygame.image.load("images/explosion/explosion_"+str(i)+".png")for i in range(0,5)]
		self.i=0
		for i in range(len(self.images)):
			self.images[i]=pygame.transform.rotozoom(self.images[i],90,1)
			self.images[i]=pygame.transform.scale(self.images[i],(150,150))
		self.image=self.images[self.i]	
		self.width,self.height=self.image.get_size()
		self.x=randint(width//2,width)
		self.y=height
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def update(self):
		if self.i<len(self.images)-1:
			self.i+=1
		else:
			self.i=0
		self.image=self.images[self.i]			

		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def setPosition(self,x,y):
		self.x=x
		self.y=y
	def default(self):
		self.y=height
		self.i=0
		self.rect=self.image.get_rect(topleft=(self.x,self.y))




class Restartbutton(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/restart.png")
		self.image= pygame.transform.scale(self.image,(300,300))
		self.width,self.height=self.image.get_size()
		self.x=width//2-self.width//2
		self.y=height//2-self.height//2
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def update(self):
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def click(self,pos):
		x,y=pos
		if self.x<x<self.x+self.y and self.y<y<self.y+self.height:
			restart_game()








class Imagebackground(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/background.jpg")
		self.width,self.height=self.image.get_size()
		self.image= pygame.transform.scale(self.image,(width,height))
		self.x=x
		self.y=y
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def update(self):
		self.movement()  
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def movement(self):
		if self.x<=-width:
			self.x=width-1             
		else:
			self.x-=1



class Lava (pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("images/lavatexture.jpg")
		self.width,self.height=self.image.get_size()
		self.height=95
		self.image= pygame.transform.scale(self.image,(width,self.height))
		self.x=0
		self.y=height-self.height
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
	def update(self):
		self.rect=self.image.get_rect(topleft=(self.x,self.y))

button=Restartbutton()
lava=Lava()
fireball=Fireball()  
explosion=Explosion() 
imbackg=[Imagebackground(0-width//2,0),Imagebackground(width//2,0)]
runner=Runner(width//2,-100)
platforms=[Platform(x,randint(250,height-250),x) for x in range(width//2,2925,200) ]
Platform.last=platforms[-1]
background=Background()
all_sprites=pygame.sprite.Group()
end_sprites=pygame.sprite.Group()
end_sprites.add(background)
end_sprites.add(button)
all_sprites.add(imbackg)
all_sprites.add(platforms)
all_sprites.add(runner)
all_sprites.add(lava)
timer=0

def restart_game():
	global collide
	runner.default()
	for platform in platforms:
		platform.default()
	fireball.default()
	explosion.default() 
	runner.screamsounds.stop()
	collide=0
	all_sprites.remove(explosion)
	explosion.i=0
	all_sprites.add(fireball)


excollide=0

t=0

fps=40
while True:
	clock.tick(fps) 
	for event in pygame.event.get():
		if event.type==pygame.MOUSEBUTTONDOWN :
			if  t>80:
				t=0
				pos=pygame.mouse.get_pos()
				button.click(pos)



		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				pygame.quit()
			if event.key==pygame.K_SPACE:
				runner.counter()
				runner.jump=1
				for platform in platforms:
					platform.move=1
	if not collide:
		if runner.last_call():
			screen.fill((150,130,0))
			runner.heartbeatsound.stop()
		else:
			screen.fill(red)
			runner.heartbeatsound.play()
		last=platforms[-1]
		excollide=pygame.sprite.collide_rect_ratio(1)(runner,fireball)
		print(runner.y,explosion.y)
		all_sprites.update()
		all_sprites.draw(screen)
		score_render=font.render("your score: "+ str(runner.score), True, white)
		screen.blit(score_render,(15,20))
		record_render=font.render("your record: "+ str(runner.record), True, white)
		screen.blit(record_render,(width-810,20))
		runner.falling(platforms)
		if runner.y+runner.height>=height-lava.height:
			collide=1
			runner.heartbeatsound.stop()
		if timer+10000<pygame.time.get_ticks():
			timer=pygame.time.get_ticks()
			all_sprites.add(fireball)
		elif fireball.y+fireball.height<0:
			all_sprites.remove(fireball)
			fireball.y=height
			fireball.x=randint(width//2,width)
			timer=pygame.time.get_ticks()
		elif excollide:
			all_sprites.remove(fireball)
			explosion.setPosition(fireball.x, fireball.y)
			all_sprites.add(explosion) 
			fps=1
			excollide=0
		if explosion.i==4:
			collide=1
			fps=40
			excollide=0
			explosion.y=height
			explosion.i=0

	else:
		t+=1
		fps=40
		if runner.score>runner.record:
			runner.set_record(runner.score)
		end_sprites.update()
		end_sprites.draw(screen)
		runner.screamsounds.play()

	pygame.display.flip()
