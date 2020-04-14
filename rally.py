#Ралли
import pygame
import random


BLUE=(0,128,255)
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)

pygame.init()

w=700
h=700
speed=8
x=150
y=300

sc=pygame.display.set_mode((w,h))
sc.fill(WHITE) 

FPS=150
clock=pygame.time.Clock()

pygame.display.set_caption('Ралли') 

icon=pygame.image.load('C:/Users/A/Desktop/F/wheel.png')
pygame.display.set_icon(icon)

car=pygame.image.load('C:/Users/A/Desktop/F/auto.png')
car.set_colorkey((255,255,255))
car_rect=car.get_rect(center=(x,y))
sc.blit(car,car_rect)

scale=pygame.transform.scale(car,(car.get_width()//2,car.get_height()//2))

background=pygame.image.load('C:/Users/A/Desktop/F/трасса.png')
background_rect=background.get_rect(center=(w//2,h//2))

pygame.mixer.music.load('C:/Users/A/Desktop/Новая папка (3)/Новая папка (2)/Kalimba.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

coin=pygame.image.load('C:/Users/A/Desktop/F/coin.png')
bomb=pygame.image.load('C:/Users/A/Desktop/F/bomb.png')

pygame.display.update()

i=0
cords=[(100,155),(200,170),(300,180),(400,220),(500,250),(600,240),(100,400),(200,600),(300,500),(400,650),(500,440),(600,320)]

COIN_CORDS=(cords[random.randint(0,11)])
BOMB_CORDS=(cords[random.randint(0,11)])
while 1:
	sc.fill(WHITE)
	coin_rect=coin.get_rect(center=COIN_CORDS)
	sc.blit(background,background_rect)
	sc.blit(coin,coin_rect)
	scale_rect=scale.get_rect(center=(x,y))
	sc.blit(scale,scale_rect)
	bomb_rect=bomb.get_rect(center=BOMB_CORDS)
	sc.blit(bomb,bomb_rect)
	events=pygame.event.get()
	for event in events:
		if event.type==pygame.QUIT:
			pygame.quit()
			break

	
	if i>=0:
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and x>0:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			x -= speed
			rot=pygame.transform.rotate(scale,90)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect)

		if keys[pygame.K_RIGHT] and x<700:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			x += speed
			rot=pygame.transform.rotate(scale,-90)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect)

		if keys[pygame.K_UP] and y>0:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			y -= speed
			rot=pygame.transform.rotate(scale,0)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect) 

		if keys[pygame.K_DOWN] and y<700:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			y += speed
			rot=pygame.transform.rotate(scale,180)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect)

		if keys[pygame.K_LEFT] and keys[pygame.K_UP] and x>0 and y>0:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			x -= speed-1
			rot=pygame.transform.rotate(scale,45)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect)

		if keys[pygame.K_LEFT] and keys[pygame.K_DOWN] and x>0 and y<700:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			x -= speed-1
			rot=pygame.transform.rotate(scale,135)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect)

		if keys[pygame.K_RIGHT] and keys[pygame.K_UP] and x<700 and y>0:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			x += speed-1
			rot=pygame.transform.rotate(scale,-45)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect)

		if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN] and x<700 and y<700:
			sc.fill(WHITE)
			sc.blit(background,background_rect)
			sc.blit(coin,coin_rect)
			sc.blit(bomb,bomb_rect)
			x += speed-1
			rot=pygame.transform.rotate(scale,-135)
			rot_rect=rot.get_rect(center=(x,y))
			sc.blit(rot,rot_rect)

		f1=pygame.font.SysFont('impact',24)
		text=f1.render('Счёт: '+str(i),1,(255,0,0))
		sc.blit(text, (600,5))
		
		if x >=COIN_CORDS[0] and x <=COIN_CORDS[0]+50:
			if y >=COIN_CORDS[1] and y <= COIN_CORDS[1]+50:
				COIN_CORDS=(cords[random.randint(0,11)])
				i+=10
		if x >=BOMB_CORDS[0] and x <=BOMB_CORDS[0]+50:
			if y >=BOMB_CORDS[1] and y <= BOMB_CORDS[1]+50:
				BOMB_CORDS=(cords[random.randint(0,11)])
				i-=10
	elif i<0:
		f2=pygame.font.SysFont('impact',48)
		text2=f2.render('Вы проиграли!',1,(0,0,170))
		sc.blit(text2,((w//2)-120,(h//2)-100))
		
	clock.tick(FPS)
	pygame.display.update()



