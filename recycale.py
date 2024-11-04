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
    if game_over:
        screen.draw.text("Game Over", fontsize=50, center=CENTRE, color="black")
        screen.draw.text("Try Again", fontsize=50, center=(CENTRE_X, CENTRE_Y + 20), color="black")
    if game_complete:
        screen.draw.text("Good Job", fontsize=50, center=CENTRE, color="black")
        screen.draw.text("Round 2?", fontsize=50, center=CENTRE, color="black")
    else:
        for item in items:
            item.draw()
def get_option_to_create(number_of_extra_items):
    items_to_create=["paper"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
def create_items(items_to_create):
    new_items=[]
    for i in items_to_create():
        it=Actor(i+"img")
        new_items.append(it)
    return new_items()

pgzrun.go()
