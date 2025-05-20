import pgzrun
import random
import time
import sys
import os

TITLE = 'messy room'
WIDTH = 804
HEIGHT = 556
time_limit = 50

#OBJECTS
 #general
background = Actor("background.png")
blur = Actor("blur.png")
background.state = ['title','start','win','lose','about','reset']
background.current_state = background.state[0]

put_away = "put_away.png"
bed = Actor("bed_messy.png")
trash = Actor("trash_empty.png")
bookshelf = Actor("bookshelf.png")
drawer = Actor("drawer.png")

bed.state = ['not done', 'done']
bed.current_state = bed.state[1]

trash.state = ['not done', 'done']
trash.current_state = trash.state[0]

drawer.state = ['not done', 'done']
drawer.current_state = drawer.state[0]

bookshelf.state = ['not done', 'done']
bookshelf.current_state = bookshelf.state[0]

start_button = Actor("start.png")
about_button = Actor("about.png")
main_menu = Actor("main_menu.png")
play_again = Actor("play_again.png")
sound_button = Actor("mute.png")

play_again.state = ["unclickable","clickable"]
play_again.current_state = play_again.state[0]
start_button.state = ["unclickable","clickable"]
start_button.current_state = start_button.state[1]
about_button.state = ["unclickable","clickable"]
about_button.current_state = about_button.state[1]
main_menu.state = ["unclickable","clickable"]
main_menu.current_state = main_menu.state[0]

sounds.put_away.set_volume(0.5)
sounds.start.set_volume(0.2)

 #trash
t1 = Actor("trash1.png")
t2 = Actor("trash2.png")
t3 = Actor("trash3.png")
t4 = Actor("trash4.png")
t5 = Actor("trash5.png")
 #books
b1 = Actor("book1.png")
b2 = Actor("book2.png")
b3 = Actor("book3.png")
b4 = Actor("book4.png")
b5 = Actor("book5.png")
 #clothes
c1 = Actor("clothes1.png")
c2 = Actor("clothes2.png")
c3 = Actor("clothes3.png")
c4 = Actor("clothes4.png")
c5 = Actor("clothes5.png")

#random placement
i_x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i_y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#ITEMS LOCATIONS
 #general
start_button.pos = (random.randint(100, 700),random.randint(475, 525))
about_button.pos = (random.randint(400, 700),random.randint(75, 325))
main_menu.pos = (705,535)
play_again.pos = (660,520)
sound_button.pos = (785,535)

bed.pos = (318,287)

trash.pos = (485,225)

bookshelf.pos = (400,118)

drawer.pos = (587,215)

game = False

#background music
music.play("music.wav")

def beginning():
    screen.clear()
    blur.draw()
    music.set_volume(1)
    screen.draw.text("messy room",(100,100), fontsize=60)
    screen.draw.text('instructions:', (110,300), fontsize = 35)
    screen.draw.text('drag and drop the scattered items into the correct spots', (230,370), fontsize = 30)
    screen.draw.text('time to clean is ' + str(time_limit) +' seconds', (180,420), fontsize = 30)
    start_button.draw()
    sound_button.draw()
    start_button.current_state = start_button.state[1]
    about_button.draw()
    about_button.current_state = about_button.state[1]
    bed.current_state = bed.state[1]
    
def reset():
    trash.current_state = trash.state[0]
    bookshelf.current_state = bookshelf.state[0]
    drawer.current_state = drawer.state[0]
    bed.current_state = bed.state[0]
    trash.image = "trash_empty.png"
    bed.image = "bed_messy.png"
    drawer.image = "drawer.png"
    bookshelf.image = "bookshelf.png"
     #trash
    t1.image = "trash1.png"
    t2.image = "trash2.png"
    t3.image = "trash3.png"
    t4.image = "trash4.png"
    t5.image = "trash5.png"
     #books
    b1.image = "book1.png"
    b2.image = "book2.png"
    b3.image = "book3.png"
    b4.image = "book4.png"
    b5.image = "book5.png"
     #clothes
    c1.image = "clothes1.png"
    c2.image = "clothes2.png"
    c3.image = "clothes3.png"
    c4.image = "clothes4.png"
    c5.image = "clothes5.png"
    
    for i in range(15):
        i_x[i] = random.randint(50, 750)
        i_y[i] = random.randint(385, 540)
        
    t1.pos = (i_x[0],i_y[0])
    t2.pos = (i_x[1],i_y[1])
    t3.pos = (i_x[2],i_y[2])
    t4.pos = (i_x[3],i_y[3])
    t5.pos = (i_x[4],i_y[4])
     #books
    b1.pos = (i_x[5],i_y[5])
    b2.pos = (i_x[6],i_y[6])
    b3.pos = (i_x[7],i_y[7])
    b4.pos = (i_x[8],i_y[8])
    b5.pos = (i_x[9],i_y[9])
     #clothes
    c1.pos = (i_x[10],i_y[10])
    c2.pos = (i_x[11],i_y[11])
    c3.pos = (i_x[12],i_y[12])
    c4.pos = (i_x[13],i_y[13])
    c5.pos = (i_x[14],i_y[14])
    

def start():
    game = True
    start_button.current_state = start_button.state[0]
    about_button.current_state = about_button.state[0]
    main_menu.current_state = main_menu.state[0]
    play_again.current_state = play_again.state[0]
    screen.clear()
    background.draw()
    screen.draw.text('to do:', (10,10), fontsize = 35)
    screen.draw.text('put away 5 clothes', (15,40), fontsize = 30)
    screen.draw.text('put away 5 books', (15,65), fontsize = 30)
    screen.draw.text('put away 5 trash', (15,90), fontsize = 30)
    screen.draw.text('make bed', (15,115), fontsize = 30)
    bed.draw()
    trash.draw()
    bookshelf.draw()
    drawer.draw()
 #clothes
    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()
    c5.draw()
 #books
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
 #trash
    t1.draw()
    t2.draw()
    t3.draw()
    t4.draw()
    t5.draw()
    
    sound_button.draw()
    
    current_time = time.time()
    total_time = current_time - start_time
    screen.draw.text('time remaining:' + str(int(time_limit - total_time)), (500, 15), fontsize=40)
    if total_time > time_limit and game == True:
        background.current_state = "lose"
        main_menu.pos = (random.randint(300, 750),random.randint(0, 500))
        play_again.pos = (random.randint(100, 700),random.randint(475, 525))

#game win function
def win():
    screen.clear()
    reset()
    bed.current_state = bed.state[1]
    blur.draw()
    main_menu.draw()
    main_menu.current_state = main_menu.state[1]
    sound_button.draw()
    screen.draw.text("win",(100,100), fontsize=60)
    play_again.draw()
    play_again.current_state = play_again.state[1]
    game = False
    
def lose():
    screen.clear()
    reset()
    bed.current_state = bed.state[1]
    blur.draw()
    main_menu.draw()
    main_menu.current_state = main_menu.state[1]
    screen.draw.text("lose",(100,100), fontsize=60)
    sound_button.draw()
    play_again.draw()
    play_again.current_state = play_again.state[1]
    game = False
    
def about():
    screen.clear()
    blur.draw()
    main_menu.pos = (685,535)
    main_menu.draw()
    main_menu.current_state = main_menu.state[1]
    sound_button.draw()
    play_again.current_state = play_again.state[0]
    start_button.current_state = start_button.state[0]
    about_button.current_state = about_button.state[0]
    screen.draw.text("about us", (300, 40), fontsize=70)
    screen.draw.text("created by", (315, 120), fontsize=50)
    screen.draw.text("faiaz azmain", (300, 180), fontsize=50)
    screen.draw.text("cicely karas", (305, 240), fontsize=50)
    screen.draw.text("serena warner", (290, 300), fontsize=50)
    screen.draw.text("graphics by", (310, 380), fontsize=50)
    screen.draw.text("snake roth-bamburg", (250, 450), fontsize=50)
    screen.draw.text("all rights reserved", (10, 530), fontsize=20)

def draw():
    if background.current_state == "title":
        beginning()
    elif background.current_state == "start":
        start()
    elif background.current_state == "win":
        win()
    elif background.current_state == "lose":
        lose()
    elif background.current_state == "about":
        about()
    elif background.current_state == "reset":
        reset()
        background.current_state = "start"

#way to exit the game
def escape(key):
    if key == keys.ESCAPE:
        sys.exit()

# updating
def update(dt):
    pass

# function to move items
def on_mouse_move(pos, rel, buttons):
    if mouse.LEFT in buttons:
    #trash
        if t1.collidepoint(pos) and t1.image != put_away:
            t1.x = pos[0]
            t1.y = pos[1]
        elif t2.collidepoint(pos) and t2.image != put_away:
            t2.x = pos[0]
            t2.y = pos[1]
        elif t3.collidepoint(pos) and t3.image != put_away:
            t3.x = pos[0]
            t3.y = pos[1]
        elif t4.collidepoint(pos) and t4.image != put_away:
            t4.x = pos[0]
            t4.y = pos[1]
        elif t5.collidepoint(pos) and t5.image != put_away:
            t5.x = pos[0]
            t5.y = pos[1]
    #books
        elif b1.collidepoint(pos) and b1.image != put_away:
            b1.x = pos[0]
            b1.y = pos[1]
        elif b2.collidepoint(pos) and b2.image != put_away:
            b2.x = pos[0]
            b2.y = pos[1]
        elif b3.collidepoint(pos) and b3.image != put_away:
            b3.x = pos[0]
            b3.y = pos[1]
        elif b4.collidepoint(pos) and b4.image != put_away:
            b4.x = pos[0]
            b4.y = pos[1]
        elif b5.collidepoint(pos) and b5.image != put_away:
            b5.x = pos[0]
            b5.y = pos[1]
    #clothes
        elif c1.collidepoint(pos) and c1.image != put_away:
            c1.x = pos[0]
            c1.y = pos[1]
        elif c2.collidepoint(pos) and c2.image != put_away:
            c2.x = pos[0]
            c2.y = pos[1]
        elif c3.collidepoint(pos) and c3.image != put_away:
            c3.x = pos[0]
            c3.y = pos[1]
        elif c4.collidepoint(pos) and c4.image != put_away:
            c4.x = pos[0]
            c4.y = pos[1]
        elif c5.collidepoint(pos) and c5.image != put_away:
            c5.x = pos[0]
            c5.y = pos[1]


#function to change bed
def on_mouse_down(pos, button):
    if bed.collidepoint(pos) and bed.current_state == bed.state[0]:
        bed.current_state = bed.state[1]
        bed.image = "bed_made.png"
        sounds.right.play()
        
    if start_button.collidepoint(pos) and start_button.current_state == start_button.state[1]:
        background.current_state = background.state[5]
        sounds.start.play()
        sounds.start.set_volume(0.35)
        global start_time
        start_time = time.time()
        screen.draw.text('to put away:', (10,10), fontsize = 35)
        screen.draw.text('5 clothes', (random.randint(10, 30),random.randint(20, 40)), fontsize = 30)
        screen.draw.text('5 books', (random.randint(10, 30),random.randint(50, 70)), fontsize = 30)
        screen.draw.text('5 trash', (random.randint(10, 30),random.randint(80, 100)), fontsize = 30)
        
    elif about_button.collidepoint(pos) and about_button.current_state == about_button.state[1]:
        background.current_state = background.state[4]
        
    elif play_again.collidepoint(pos) and play_again.current_state == play_again.state[1]:
        background.current_state = background.state[5]
        start_time = time.time()
        
    elif main_menu.collidepoint(pos) and main_menu.current_state == main_menu.state[1]:
        start_button.pos = (random.randint(100, 700),random.randint(475, 525))
        about_button.pos = (random.randint(400, 700),random.randint(75, 325))
        background.current_state = background.state[0]
        main_menu.current_state = main_menu.current_state[0]
        
    elif sound_button.collidepoint(pos):
        if sound_button.image == "mute.png":
            music.pause()
            sound_button.image = "unmute.png"
        elif sound_button.image == "unmute.png":
            music.play("music.wav")
            sound_button.image = "mute.png"
            
#function to
#       1. 'put away' items if at correct location
#       2. put the item back to original location if not at correct location
#       3. playing sound effect when all items of one type are 'put away'
def on_mouse_up(pos, button):
    trash_count = 0
    book_count = 0
    clothes_count = 0
 #trash
    if trash.colliderect(t1):
        if t1.image == "trash1.png":
            sounds.put_away.play()
        t1.image = put_away
        trash_count += 1
    else:
        t1.pos = (i_x[0],i_y[0])
        
    if trash.colliderect(t2):
        if t2.image == "trash2.png":
            sounds.put_away.play()
        t2.image = put_away
        trash_count += 1
    else:
        t2.pos = (i_x[1],i_y[1])
    
    if trash.colliderect(t3):
        if t3.image == "trash3.png":
            sounds.put_away.play()
        t3.image = put_away
        trash_count += 1
    else:
        t3.pos = (i_x[2],i_y[2])
    
    if trash.colliderect(t4):
        if t4.image == "trash4.png":
            sounds.put_away.play()
        t4.image = put_away
        trash_count += 1
    else:
        t4.pos = (i_x[3],i_y[3])
    
    if trash.colliderect(t5):
        if t5.image == "trash5.png":
            sounds.put_away.play()
        t5.image = put_away
        trash_count += 1
    else:
        t5.pos = (i_x[4],i_y[4])
        
    if trash_count == 5 and trash.current_state == trash.state[0]:
        trash.current_state = trash.state[1]
        trash.image = "trash_full.png"
        sounds.right.play()
    
 #books
    if b1.colliderect(bookshelf):
        if b1.image == "book1.png":
            sounds.put_away.play()
        b1.image = put_away
        book_count += 1
    else:
        b1.pos = (i_x[5],i_y[5])
        
    if b2.colliderect(bookshelf):
        if b2.image == "book2.png":
            sounds.put_away.play()
        b2.image = put_away
        book_count += 1
    else:
        b2.pos = (i_x[6],i_y[6])
        
    if b3.colliderect(bookshelf):
        if b3.image == "book3.png":
            sounds.put_away.play()
        b3.image = put_away
        book_count += 1
    else:
        b3.pos = (i_x[7],i_y[7])
        
    if b4.colliderect(bookshelf):
        if b4.image == "book4.png":
            sounds.put_away.play()
        b4.image = put_away
        book_count += 1
    else:
        b4.pos = (i_x[8],i_y[8])
        
    if b5.colliderect(bookshelf):
        if b5.image == "book5.png":
            sounds.put_away.play()
        b5.image = put_away
        book_count += 1
    else:
        b5.pos = (i_x[9],i_y[9])
        
    if book_count == 5 and bookshelf.current_state == bookshelf.state[0]:
        bookshelf.current_state = bookshelf.state[1]
        bookshelf.image = put_away
        sounds.right.play()
    
 #clothes
    if c1.colliderect(drawer):
        if c1.image == "clothes1.png":
            sounds.put_away.play()
        c1.image = put_away
        clothes_count += 1
    else:
        c1.pos = (i_x[10],i_y[10])
    
    if c2.colliderect(drawer):
        if c2.image == "clothes2.png":
            sounds.put_away.play()
        c2.image = put_away
        clothes_count += 1
    else:
        c2.pos = (i_x[11],i_y[11])
    
    if c3.colliderect(drawer):
        if c3.image == "clothes3.png":
            sounds.put_away.play()
        c3.image = put_away
        clothes_count += 1
    else:
        c3.pos = (i_x[12],i_y[12])
    
    if c4.colliderect(drawer):
        if c4.image == "clothes4.png":
            sounds.put_away.play()
        c4.image = put_away
        clothes_count += 1
    else:
        c4.pos = (i_x[13],i_y[13])
    
    if c5.colliderect(drawer):
        if c5.image == "clothes5.png":
            sounds.put_away.play()
        c5.image = put_away
        clothes_count += 1
        if c5.image == "clothes5.png":
            sounds.put_away.play()
    else:
        c5.pos = (i_x[14],i_y[14])
    
    if clothes_count == 5 and drawer.current_state == drawer.state[0]:
        drawer.current_state = drawer.state[1]
        drawer.image = put_away
        clothes_count += 1
        sounds.right.play()
    
    if trash.current_state == trash.state[1] and bed.current_state == bed.state[1] and bookshelf.current_state == bookshelf.state[1] and drawer.current_state == drawer.state[1]:
        background.current_state = "win"
        main_menu.pos = (random.randint(200, 750),random.randint(0, 500))
        play_again.pos = (random.randint(100, 700),random.randint(475, 525))
    
os.environ['SDL_VIDEO_CENTERED'] = '1'

pgzrun.go()