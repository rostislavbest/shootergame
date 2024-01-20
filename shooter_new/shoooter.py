import pygame
import random
pygame.init()
W,H = 700,500

fps = pygame.time.Clock()


class main():
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h  =h
        self.img = img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img),(self.w,self.h))

        self.rect = self.img_new.get_rect(center = (self.x,self.y))
        self.rand = random.randint(1,3)
player = main(350,450,50,100,'rocket.png')


bullet_list  = []# список для куль
bullet_ufo_list = []
planet_list = []
def addbullet():# функція яка додає кулю в список
    bullet_list.append(main(player.rect.x,player.rect.y,10,35,'bullet.png'))
def add(img):# функція додає противників в список через створення обєкту

    a = []
    y =19
    for el in range(5):
        a.append(main(random.randint(10,W-30),y,70,70,img))# створення обєкту противника та додавання в список
    return a
def add_ufo(img):# функція додає противників в список через створення обєкту

    a = []
    bul_ufo_list = []
    y =19
    for el in range(5):
        ufo = main(random.randint(10,W-30),y,70,70,img)
        a.append(ufo)# створення обєкту противника та додавання в список

    return a
def add_planet(img):# функція додає противників в список через створення обєкту
    y =19
    for el in range(5):
       ufo = main(random.randint(10,W-30),y,70,70,img)
       planet_list.append(ufo)# створення обєкту противника та додавання в список

print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')
print('багато якогось коду')

add_planet('planet.png')
list_enemy = add('asteroid.png')# створюю список астероїдів
list_ufo  = add_ufo('ufo.png')# створюю список нло
pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play(loops = -1)
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('Shooter')
fon = pygame.transform.scale(pygame.image.load('galaxy.jpg'),(W,H))
fon1 = pygame.transform.scale(pygame.image.load('galaxy.jpg'),(W,H))
run = True
fon_change = -1000
score_number = 0# рахунок на початок гри
health_number =15# життя на початку гри
level_ufo = False
level_planet = False
print(planet_list)
while run:

    score = 'enemyes:' +str(score_number)# змінка рахунку
    health = 'life:' + str(health_number)#зміннадля зміни життя
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                addbullet()


    screen.blit(fon, (0,0))
#--------------------весь текст в неашій грі-------------------------
    text_score = pygame.font.Font(None, 30)
    text_new = text_score.render(score, True, (255, 100, 130))
    screen.blit(text_new,(50,50))
    text_score = pygame.font.Font(None, 30)
    text_new = text_score.render(health, True, (255, 100, 130))
    screen.blit(text_new, (550, 50))

    #---------------------керування-------------------------------
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]  and player.rect.right<=W:
        player.rect.x +=3
    if key[pygame.K_LEFT]  and player.rect.left>=0:
        player.rect.x -=3

    screen.blit(player.img_new,player.rect)
#--------------------астероїди------------------------
    for el in list_enemy:
        screen.blit(el.img_new,el.rect)#відмальовуємо астероїд
        el.rect.y += el.rand# випадкова швидкість падіння астероїду
        if el.rect.bottom >=H:# якщо астероїд виходить за рамки знизу ми робоми так що він зявляється зверху
            el.rect.x,el.rect.y = random.randint(0,W-30),-50# випадкове положення зверху
            el.rand = random.randint(1,3)#випадкова швидкість
            health_number-=1
        for bullet in bullet_list:
            screen.blit(bullet.img_new, (bullet.rect.x +20, bullet.rect.y))#відмальовуємо кулю
            bullet.rect.y -=1# вона летить
            if bullet.rect.colliderect(el.rect):# якщо куля попадає по астереоїду і по нло
                bullet_list.pop()# куля видаляється зі списку
                el.rect.x,el.rect.y  =  random.randint(0,W),-50#переносить астероїд на вверх
                score_number+=1# змінюємо рахунок збитих астреоїдів
    if score_number>=5 and score_number<=10:
        level_ufo = True
    if score_number>=10 and score_number<=15:
        level_planet = True
        print('rtretret')
    if health_number<=0:

      break
    #---------------------------------------нло------------------------------------------
    if level_ufo:

        if len(list_enemy)>0:
            list_enemy.pop()
        for el in list_ufo:
            screen.blit(el.img_new, el.rect)  # відмальовуємо нло
            el.rect.y += el.rand  # випадкова швидкість падіння
            if len(bullet_ufo_list)<=-1:
                bullet_ufo_list.append(main(el.rect.x, el.rect.y, 10, 10, 'bullet.png'))


            if el.rect.bottom >= H:  # якщо нло виходить за рамки знизу ми робоми так що він зявляється зверху
                el.rect.x, el.rect.y = random.randint(0, W - 30), -50  # випадкове положення зверху
                el.rand = random.randint(1, 3)  # випадкова швидкість
                health_number -= 1


            for bullet in bullet_list:
                screen.blit(bullet.img_new, (bullet.rect.x + 20, bullet.rect.y))  # відмальовуємо кулю
                bullet.rect.y -= 1  # вона летить
                if bullet.rect.colliderect(el.rect):  # якщо куля попадає по астереоїду і по нло
                    bullet_list.pop()  # куля видаляється зі списку
                    el.rect.x, el.rect.y = random.randint(0, W), -50  # переносить астероїд на вверх
                    score_number += 1  # змінюємо рахунок збитих астреоїдів
            for j in bullet_ufo_list:
                screen.blit(j.img_new, (j.rect.x, j.rect.y))
                j.rect.y += j.rand
                if j.rect.y >= H:

                    j.rect.y,j.rect.x = el.rect.x, el.rect.y
        # ---------------------------------------нло------------------------------------------
        if level_ufo:

            if len(list_enemy) > 0:
                list_enemy.pop()
            for el in list_ufo:
                screen.blit(el.img_new, el.rect)  # відмальовуємо нло
                el.rect.y += el.rand  # випадкова швидкість падіння
                if len(bullet_ufo_list) <= -1:
                    bullet_ufo_list.append(main(el.rect.x, el.rect.y, 10, 10, 'bullet.png'))

                if el.rect.bottom >= H:  # якщо нло виходить за рамки знизу ми робоми так що він зявляється зверху
                    el.rect.x, el.rect.y = random.randint(0, W - 30), -50  # випадкове положення зверху
                    el.rand = random.randint(1, 3)  # випадкова швидкість
                    health_number -= 1

                for bullet in bullet_list:
                    screen.blit(bullet.img_new, (bullet.rect.x + 20, bullet.rect.y))  # відмальовуємо кулю
                    bullet.rect.y -= 1  # вона летить
                    if bullet.rect.colliderect(el.rect):  # якщо куля попадає по астереоїду і по нло
                        bullet_list.pop()  # куля видаляється зі списку
                        el.rect.x, el.rect.y = random.randint(0, W), -50  # переносить астероїд на вверх
                        score_number += 1  # змінюємо рахунок збитих астреоїдів
                for j in bullet_ufo_list:
                    screen.blit(j.img_new, (j.rect.x, j.rect.y))
                    j.rect.y += j.rand
                    if j.rect.y >= H:
                        j.rect.y, j.rect.x = el.rect.x, el.rect.y
        # ---------------------------------------нло------------------------------------------
        if level_planet:
            print('yes')
            if len(list_ufo) > 0:
                list_ufo.pop()
            for el in planet_list:
                screen.blit(el.img_new, el.rect)  # відмальовуємо нло
                el.rect.y += el.rand  # випадкова швидкість падіння
                if len(bullet_ufo_list) <= -1:
                    bullet_ufo_list.append(main(el.rect.x, el.rect.y, 10, 10, 'bullet.png'))

                if el.rect.bottom >= H:  # якщо нло виходить за рамки знизу ми робоми так що він зявляється зверху
                    el.rect.x, el.rect.y = random.randint(0, W - 30), -50  # випадкове положення зверху
                    el.rand = random.randint(1, 3)  # випадкова швидкість
                    health_number -= 1

                for bullet in bullet_list:
                    screen.blit(bullet.img_new, (bullet.rect.x + 20, bullet.rect.y))  # відмальовуємо кулю
                    bullet.rect.y -= 1  # вона летить
                    if bullet.rect.colliderect(el.rect):  # якщо куля попадає по астереоїду і по нло
                        bullet_list.pop()  # куля видаляється зі списку
                        el.rect.x, el.rect.y = random.randint(0, W), -50  # переносить астероїд на вверх
                        score_number += 1  # змінюємо рахунок збитих астреоїдів
                for j in bullet_ufo_list:
                    screen.blit(j.img_new, (j.rect.x, j.rect.y))
                    j.rect.y += j.rand
                    if j.rect.y >= H:
                        j.rect.y, j.rect.x = el.rect.x, el.rect.y
    fps.tick(70)
    pygame.display.update()






