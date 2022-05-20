import pygame, socket, sys
from threading import Thread

width = 800
height = 100
username = input("Input a username: ")
screen = pygame.display.set_mode([width, height])
WindowX, y = screen.get_size()
OldWindowX, OldY = screen.get_size()
pygame.init()
pygame.display.set_caption("Chat Program v2: "+username)

font1 = pygame.font.SysFont('segoe ui', 20)
txtinput = ""
inputting = False
te = font1.render("Enter a message here...",True, (0,0,0))
keep_going = True
Color = (100,100,100)
MainRect = pygame.Rect((0,0),(width,height))
Fullscreen = False
port = 10000
#this will be merged into a program, and not just the input. not sure when
max_queue = 18
messages = [None] * max_queue
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost",port)
s.connect(server_address)
def listen():
    while True:
        #s.settimeout(0)
        data = s.recv(8192)
        user = s.recv(8192)
        message = data.decode()
        sys.stdout.write("%s\n" % message)
        #print("%s" % data.decode(),end="\r")
Thread(target = listen).start()
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()
            if MainRect.collidepoint(spot) and not inputting:
                inputting = True
        if event.type == pygame.QUIT:
            keep_going = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if inputting:
                if not event.key == pygame.K_BACKSPACE and not event.key == pygame.K_RETURN:
                    txtinput = txtinput + event.unicode
                    te = font1.render(txtinput,True, (0,0,0))
                elif event.key == pygame.K_RETURN:
                    inputting = False
                    message = txtinput
                    byte_message = message.encode()
                    username = username.encode()
                    s.sendall(byte_message)
                    s.sendall(username)
                    te3 = font1.render(message,True, (0,0,0))
                    txtinput = ""
                    te = font1.render("Enter a message here...",True, (0,0,0))
                    username = username.decode()
                else:
                    txtinput = txtinput[:-1]
                    te = font1.render(txtinput,True, (0,0,0))
            #if event.key == pygame.K_p:
                #print("YEEEAAH")
    spot = pygame.mouse.get_pos()
    pygame.draw.rect(screen,  Color, MainRect)
    screen.blit(te, (0,0)) # i have decended into bilt madness
    pygame.display.update()
pygame.quit()