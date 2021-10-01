import pygame
import math
import time
import random
pygame.init()
height=900
width=900
screen=pygame.display.set_mode((width, height))
white=(255,255,255)
shooting_sound= pygame.mixer.Sound("sounds/shooting.ogg")
shooting_sound2= pygame.mixer.Sound("sounds/shooting2.ogg")
class Robot(pygame.sprite.Sprite):
	def __init__(self,background):
		pygame.sprite.Sprite.__init__(self)
		self.images=[pygame.image.load("images/robot.png"),pygame.image.load("images/robot2.png")]
		self.image= self.images[0]
		self.width,self.height=self.image.get_size()
		self.x= width//2-self.width//2
		self.y= height//2+height//5
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.hp=19
		self.angle=0
		self.angle2=180
		self.bullet=[]
		self.i=0
		self.frame=0
	def hploss(self):
		if self.hp>0:
			self.hp-=1
			print("robot",self.hp)
	def shot(self):
		if self.angle2 == 90:
			self.bullet.append(Bullet(self.angle,self.angle2,self.x + self.width,self.y))
		elif self.angle2 == 0:
			self.bullet.append(Bullet(self.angle,self.angle2,self.x,self.y + self.height))
		else:
			self.bullet.append(Bullet(self.angle,self.angle2,self.x,self.y))
		self.i=1
		self.frame=0
		self.render()
	def render(self):

		if self.angle==0:
			self.lookforward()
		elif self.angle==270:
			self.right()
		elif self.angle==180:
			self.back()
		elif self.angle==90:
			self.left()

	def left(self):
		self.angle=90
		self.angle2=270
		self.image=pygame.transform.rotate(self.images[self.i],self.angle)
	def right(self):
		self.angle=270
		self.angle2=90
		self.image=pygame.transform.rotate(self.images[self.i],self.angle)
	def back(self):
		self.angle=180
		self.angle2=0
		self.image=pygame.transform.rotate(self.images[self.i],self.angle)
	def lookforward(self):
		self.angle=0
		self.angle2=180
		self.image=pygame.transform.rotate(self.images[self.i],self.angle)
	def forward(self):
		if 60 < self.x < width - 60- self.width  and 60 < self.y < height - 60 -self.height:
			self.x=self.x + 60 * math.sin(math.radians(self.angle2))
			self.y=self.y + 60 * math.cos(math.radians(self.angle2))
		elif self.x <= 60:
			self.x = 61
		elif self.y <= 60:
			self.y = 61
		elif self.x >= width-60 - self.height :
			self.x=width-61 - self.width
		elif self.y >= height-60-self.height:
			self.y=height-61-self.height
	def update(self):
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		background.i=19-self.hp
		i=0
		while i<len(self.bullet):
			if self.bullet[i].state == 1:
				self.delete(i)
			else:
				i+=1
		if self.i==1:
			self.frame+=1
			if  self.frame>120:
				self.frame=0
				self.i=0
				self.render()
	def delete(self, i):
		del self.bullet[i]


class Bullet(pygame.sprite.Sprite):
	def __init__(self,angle,angle2,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.angle=angle
		self.angle2=angle2
		self.image=pygame.image.load("images/bullet.png")
		self.image=pygame.transform.rotate(self.image,self.angle)
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.state=0
		shooting_sound.play()
	def flight(self):
		self.x=self.x + 1 * math.sin(math.radians(self.angle2))
		self.y=self.y + 1 * math.cos(math.radians(self.angle2))
		if self.x >= width:
			self.state=1
		if self.x <= 0:
			self.state=1
		if self.y >= height:
			self.state=1
		if self.y <= 0:
			self.state=1
	def __del__(self):
		print(" i got deleted ")
	def update(self):
		self.flight()
		self.rect=self.image.get_rect(topleft=(self.x,self.y))


class Background(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x=0
		self.y=0
		self.images=[pygame.image.load(f"images/background/{i}.png").convert_alpha() for i in range(1,21)] 
		self.i=19
		self.image=self.images[self.i]
		self.rect=self.image.get_rect(topleft=(0,0))
	def update(self):
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.image=self.images[self.i]



class Health:
	def __init__(self,hp,x,y):
		self.x=x
		self.y=y
		self.hp=hp
		self.width=130
		self.height=20
		self.width_green=self.width
	def setpos(self,x,y):
		self.x=x
		self.y=y
	def gethp(self,p):
		p=p/self.hp
		self.width_green=p*self.width
	def update(self):
		pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.x,self.y,self.width,self.height))
		pygame.draw.rect(screen,(0,255,0),pygame.Rect(self.x,self.y,self.width_green,self.height))








class Enemybullet(pygame.sprite.Sprite):
	def __init__(self,angle,angle2,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.angle=angle
		self.angle2=angle2
		self.image=pygame.image.load("images/bullet2.png")
		self.image=pygame.transform.rotate(self.image,self.angle)
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.state=0
		shooting_sound2.play()
	def flight(self):
		self.x=self.x + 1 * math.sin(math.radians(self.angle2))
		self.y=self.y + 1 * math.cos(math.radians(self.angle2))
		if self.x >= width:
			self.state=1
		if self.x <= 0:
			self.state=1
		if self.y >= height:
			self.state=1
		if self.y <= 0:
			self.state=1
	def __del__(self):
		print(" enemybul got deleted ")

	def update(self):
		self.flight()
		self.rect=self.image.get_rect(topleft=(self.x,self.y))

class Enemy(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.x=x
		self.y=y
		self.images=[pygame.image.load("images/tank_1.png"),pygame.image.load("images/tank_2.png")]
		for i in range(len(self.images)):
			self.width,self.height=self.images[i].get_size()
			self.images[i]=pygame.transform.scale(self.images[i],(self.width//2, self.height//2))
		self.i=0
		self.image= self.images[0]
		self.width,self.height=self.images[0].get_size()
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.xold=x
		self.yold=y
		self.angle=180
		self.angle2=0
		self.old_time=self.gettime()
		self.stop=1
		self.past_time=0
		self.bul=None
		self.bulletpos()
		self.hp=60
		self.live=Health(self.hp,self.x,self.y)
	def hploss(self):
		self.hp-=1
		print("enemy lost a live",self.hp)
	def bulletpos(self):
		self.x1=self.x
		self.y1=self.y
		self.r=self.height//20
		self.r2=self.width//20
		x=self.x1+self.r2*math.sin(math.radians(self.angle))
		y=self.y1+self.r*math.cos(math.radians(self.angle))
		if self.bul==None:
			self.bul=Enemybullet(self.angle,self.angle2,x,y)
		else:
			self.delbul(1)
	def getdistance(self,pos):
		x2,y2=pos
		return math.sqrt((self.x-x2)**2+(self.y-y2)**2)
	def gettime(self):
		return time.time_ns() // 10000

	def getangle(self,pos):
		x2,y2=pos
		dx= self.x-x2
		dy= self.y-y2
		self.angle=math.degrees(math.atan2(dx,dy))
	def delbul(self,n):
		if self.bul != None:
			if n:
				if self.bul.y > height or self.bul.y < 0:
					del self.bul
					self.bul=None
			else:
				del self.bul
				self.bul=None
	def movement(self):
		if not self.stop:
			if time.time()-self.past_time>2:
				self.stop=1
				self.past_time=time.time()
			
		if self.stop:
			if self.gettime() - self.old_time>850:
				self.old_time=self.gettime()
				self.x=self.x - 1 * math.sin(math.radians(self.angle))
				self.y=self.y - 1 * math.cos(math.radians(self.angle))
		self.angle2=-(-180-self.angle) 
		self.image=pygame.transform.rotate(self.images[self.i],self.angle2)
		if self.x >= width:
			self.state=1
		if self.x <= 0:
			self.state=1
		if self.y >= height:
			self.state=1
		if self.y <= 0:
			self.state=1
	def update(self):
		self.rect=self.image.get_rect(topleft=(self.x,self.y))
		self.movement()
		self.bulletpos()
		self.live.gethp(self.hp)
		self.live.setpos(self.x-self.live.width//7,self.y-25)
		self.live.update()




enemylist=[]

background=Background()
all_sprites=pygame.sprite.Group()
enemylist.append(Enemy(50,70))
enemylist.append(Enemy(width-enemylist[0].width-50,70))
enemylist.append(Enemy(width//2-enemylist[0].width//2,150))
robot=Robot(background)
all_sprites.add(robot)
all_sprites.add(background)






"""get_pressed(num_buttons=3) -> (button1, button2, button3)"""

















while True:
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE:
				pygame.quit()
			if event.key==pygame.K_w:
				robot.lookforward()
			if event.key==pygame.K_a:
				robot.left()
			if event.key==pygame.K_s:
				robot.back()
			if event.key==pygame.K_d:
				robot.right()
			if event.key==pygame.K_w and event.key==pygame.K_LSHIFT :
				pass
		if event.type==pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[2]:
				robot.forward()
			if pygame.mouse.get_pressed()[0]:
				robot.shot()
	all_sprites.empty()
	for enemy in enemylist:
		enemy.getangle((robot.x,robot.y))
	all_sprites.add(robot.bullet)
	for enemy in enemylist:
		if enemy.bul!=None:	
			all_sprites.add(enemy.bul)
			if pygame.sprite.collide_rect(robot,enemy.bul):
				enemy.delbul(0)
				robot.hploss()
	for j in range(len(enemylist)):
		if j < len(enemylist)-1:
			if pygame.sprite.collide_rect(enemylist[j],enemylist[j+1]):
				i=random.randint(j,j+1)
				enemylist[i].stop=0
				enemylist[i].x+=30
				enemylist[i].y+=30
	i=0
	del_enemy=[]
	while i < (len(robot.bullet)):
		for j,enemy in enumerate(enemylist):
			if len(robot.bullet)!=i and pygame.sprite.collide_rect(robot.bullet[i], enemy):
				robot.delete(i)
				enemy.hploss()
				if enemy.hp<=0:
					del_enemy.append(j)
					break

		i += 1
	for i in del_enemy:
		del enemylist[i]

	all_sprites.add(robot)
	all_sprites.add(enemylist)
	all_sprites.add(background)




	screen.fill(white)
	all_sprites.update()
	all_sprites.draw(screen)
	pygame.display.flip()