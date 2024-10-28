import pgzrun
import random

WIDTH=800
HEIGHT=600
CENTRE_X= WIDTH/2
CENTRE_Y= HEIGHT/2
CENTRE=(CENTRE_X, CENTRE_Y)
FINAL_LEVEL=10
START_SPEED=10
ITEMS=["bag","bottle","battery","chips"]

game_over=False
game_complete=False
current_level=1
items=[]
animations=[]

def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("back",(0,0))
    


pgzrun.go()