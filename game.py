from graphics2 import *
from button import Button
from progress_bar import ProgressBar
import time
import random
import math

VILLAN_SPEED = 10
FOOD_SPEED = 10
NUM_WIN = 15
NUM_LOSE = 10
STALL_TIME = 0.05
WINDOW_DIMENSION = 666
THRESHOLD = 50

def distance_between_points(point1, point2):
    '''
    Calculates the distance between two points
    
    Params:
    point1 (Point): the first point
    point2 (Point): the second point
    
    Returns:
    the distance between the two points
    '''
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    
    return math.sqrt(dx ** 2 + dy ** 2)

def is_close_enough(character_img, object_img):
    '''
    Determines if the character is close enough to the food to say the character
    caught the food.
    
    Params:
    character_img (Image): the image of the character 
    foods_img (Image): the image of the food
    
    Returns:
    True if the character catches the food
    '''
    character_center = character_img.getCenter()
    object_center = object_img.getCenter()
    distance = distance_between_points(character_center, object_center)
     
    return distance < THRESHOLD

def create_window(width, height, window_title, window_color):
    
    window = GraphWin(window_title,width, height)
    window.setBackground(window_color)
    
    return window
    
def add_text_to_window(window, text_point, text_content, text_color, text_size, text_style = "italic"):
    
    text = Text(text_point, text_content)
    text.setSize(text_size)
    text.setStyle(text_style)
    text.setTextColor(text_color)
    text.draw(window)
    
    return text

def add_image_to_window(image_point, image_name, window):
    
    image = Image(image_point, image_name)
    image.draw(window)
    
    return image
    
def add_button_to_window(button_point, button_width, button_height, window, button_name = ""):
    
    button = Button(button_point, button_width, button_height,button_name, "pink")
    button.draw(window)
    button.activate()
    
    return button
    
def intro_window():
    '''
    Displays the introductory window and closes it after a delay
    '''    
    window = create_window(WINDOW_DIMENSION, WINDOW_DIMENSION, "Scooby and Shaggy game", "white")
    image_point = Point(333, 333)
    
    add_image_to_window(image_point, "intro.gif", window)
    time.sleep(1.2)
    window.close()

def insturction_window():
    '''
    Displays the instruction window, with the directions needed for the game. It closes this window when their is a click.
    '''
    window = create_window(WINDOW_DIMENSION, WINDOW_DIMENSION, "inustruction", "black")
    
    direction =  f'''
    Help your character escape from the villans by eating {NUM_WIN} foods.          
    \n If {NUM_LOSE} villans catch you before you can escape you will lose.
    \n You move your character by using your mouse pointer.
    '''
    add_text_to_window(window, Point(333,133), direction, "pink", 20,)
    add_text_to_window(window, Point(333,600), "CLICK TO CONTINUE", "pink", 30,)

    click =  window.getMouse()
    if click != '':
        window.close()

def selection_window():
    '''
    Displays the character selection window and return the selected character
    and corresponding food.
    
    Returns:
    Scooby image drawn to the window, shaggy image drawn to the window and food image name based on the choice of the player. 
    '''
    window = create_window(WINDOW_DIMENSION, WINDOW_DIMENSION, "selection", "black")
        
    direction = f'''
    Choose a charater to continue
    \n If you choose shaggy the food you have to catch will be sandwiches
    \n If you choose scooby the food you have to catch will be scooby foods
    
    '''
    add_text_to_window(window, Point(333,133), direction, "pink", 20, "normal")
    add_text_to_window(window, Point(190,370), "Shaggy", "pink", 15, )
    add_text_to_window(window, Point(190,470), "Scooby", "pink", 15, )
    shaggy = add_image_to_window(Point(120,400), "shaggy.gif", window)
    scooby = add_image_to_window(Point(100,500), "dog.gif", window)
    shaggy_button = add_button_to_window(Point(190,400), 50, 20, window, button_name = "")
    scooby_button = add_button_to_window(Point(190,500), 50, 20, window, button_name = "")
        
    click = window.getMouse()
    while not (scooby_button.isClicked(click) or shaggy_button.isClicked(click)):
        click = window.getMouse()
        
    if scooby_button.isClicked(click):
        window.close()
        food = "treat.gif"
        return scooby,food
    
    elif shaggy_button.isClicked(click):
        window.close()
        food = "sandwhich .gif"
        return shaggy,food
    
def win_window():
    '''
    Displays the win window and runs main again or closes the program based on player choice.
    
    '''
    window = create_window(WINDOW_DIMENSION, WINDOW_DIMENSION, "Scooby and shaggy game", "black")
    scooby_van = add_image_to_window(Point(0,133), "van.gif", window)
        
    for num in range(50):
        scooby_van.move(20,0)
        time.sleep(STALL_TIME)
    
    add_text_to_window(window, Point(333,333), "You Escaped", "pink", 50, text_style = "italic")
    play_again_button = add_button_to_window(Point(190,400), 70, 30, window, "Play again")
    quit_button = add_button_to_window(Point(490,400), 70, 30, window, "Quit")
    
    click = window.getMouse()
    while (not play_again_button.isClicked(click)) and (not quit_button.isClicked(click)):
        click = window.getMouse()
        
    if play_again_button.isClicked(click):
        window.close()
        main()
        
    elif quit_button.isClicked(click):
        exit(-1)

def lose_window():
    '''
    Displays the lose window and runs main or closes the program based on player choice.
    
    '''
    window = create_window(WINDOW_DIMENSION, WINDOW_DIMENSION, "Scooby and shaggy game", "black")
    add_text_to_window(window, Point(333,233), "You Lose", "pink", 50, text_style = "italic")
    replay_button = add_button_to_window(Point(190,400), 70, 30, window, "Replay")
    quit_button = add_button_to_window(Point(490,400), 70, 30, window, "Quit")
        
    click = window.getMouse()
    while (not replay_button.isClicked(click)) and (not quit_button.isClicked(click)):
        click = window.getMouse()
        
    if replay_button.isClicked(click):
        window.close()
        main()
        
    elif quit_button.isClicked(click):
        exit(-1)
    
def game_background_window():
    '''
    Displays the window the game runs in.
    
    Returns:
    the window displayed
    '''
    window = create_window(WINDOW_DIMENSION, WINDOW_DIMENSION, "Scooby and shaggy game", "white")
    add_image_to_window(Point(333,333), "background.gif", window)
    add_text_to_window(window, Point(600,25), "Point: ", "White", 20,)
    
    return window
               
def move_objects(food_img_list,villan_img_list):
    '''
    Moves every food one FOOD_SPEED unit down the window
    
    Params:
    food_img_list (list): the list of falling food
    '''
    for food in food_img_list:
        food.move(0, FOOD_SPEED)
    
    for villan in villan_img_list:
        villan.move(VILLAN_SPEED, 0)
        
def move_character(window, character_img):
    '''
    Moves the character by setting the center of character image to the point the mouse pointer is at 
    
    Params:
    window (GraphWin): the window where game play takes place
    character_img (Image): the character image
    '''
    mouse_click_center  = window.checkMousePointer().getCenter()
    character_img.setCenter(mouse_click_center)
    
def add_food_to_window(window,food):
    '''
    Adds one food to the top of the window at a random location
    
    Params:
    window (GraphWin): the window where game play takes place
    
    Returns:
    the food added to the window
    '''
    x_location = random.randrange(40, 620)
    food_point = Point(x_location, 0)
    food_img = Image(food_point, food)
    food_img.draw(window)
    
    return food_img

def add_poof_to_window(window,villan):
    '''
    Adds one smoke cloud image to the point where the villan and character contact of the window at a random location
    
    Params:
    window (GraphWin): the window where game play takes place
    '''
    
    poof_point = villan.getCenter()
    villan.undraw()
    poof_img = add_image_to_window(poof_point, "poof.gif", window)
    time.sleep(STALL_TIME)
    poof_img.undraw()
    
def add_villan_to_window(window, image_name):
    '''
    Adds one pirate to the left of the window at a random location
    
    Params:
    window (GraphWin): the window where game play takes place
    
    Returns:
    the pirate added to the window
    '''
    y_location = random.randrange(40,620)
    villan_point = Point(0,y_location)
    villan_img = add_image_to_window(villan_point, image_name, window)
    
    return villan_img

def add_health_bar_to_window(window):
    '''
    Adds health bar, which is a progress bar and heart next to it, to the window
    
    '''
    bar = ProgressBar(Point(570, 50), 50, 10, "red")
    percent = 100
    bar.update(window, percent)
    
    life_img = Image(Point(640,55),"heart.gif")
    life_img.draw(window)
    
    return bar

def generate_object(window,foods,villans,food):
    '''
    Generates the type of villans at a random interval
    
    Params:
    window (GraphWin): the window where game play takes place
    foods(image): the food image based on the character
    villans(image): the villan image that spawns in
    food(Image): the food image based on the character
    '''
    
    if random.randrange(100) < 6: # 6% of the time I will get a food
        food = add_food_to_window(window,food)
        foods.append(food)
        
    if random.randrange(100) < 6:
        pirate = add_villan_to_window(window, "pirate.gif")
        villans.append(pirate)
        
    if random.randrange(100) == 1:
        ghost = add_villan_to_window(window, "ghost.gif")
        villans.append(ghost)
        
def check_and_remove_food(window,food_list,character,contact):
    '''
    Check if the villan is oustide the window or near the character and count that amount of time its near the character.
    
    Params:
    window(GraphWin): the window where the game play takes place in
    food_list(List): list containg the food images
    character(Image): the character image thats spawns in
    contact(Int): number of count that increases when character touches food 
    
    Return:
    the number of times character touches food           
    '''
    for food in food_list:
        if is_close_enough(character,food):
            food.undraw()
            food_list.remove(food)
            contact = contact + 1
    
    for food in food_list:
        if food.getCenter().getY() > 650:
            food.undraw()
            food_list.remove(food)
    
    return contact

def check_and_remove_villan(window,villan_list,character,attack,bar):
    '''
    Check if the villan is oustide the window or near the character and count that amount of time its near the character.
    
    Params:
    window(GraphWin): the window where the game play takes place in
    villan_list(List): list containg the villan images
    character(Image): the character image thats spawns in
    attact(Int): number of count that increases when villan touches character
    bar(ProgressBar); the bar that decreases when villan touches character
    
    Return:
    the number of times villan touches character            
    '''
    for villan in villan_list:
        if is_close_enough(character,villan):
            add_poof_to_window(window,villan)
            villan_list.remove(villan)
            attack = attack + 1
            life_count = 100 - (attack / NUM_LOSE) * 100
            bar.update(window, life_count)
            
    for villan in villan_list:
        if villan.getCenter().getX() > 650:
            villan.undraw()
            villan_list.remove(villan)
    
    return attack

def game_loop(window,character,food,health_bar):
    '''
    Loop that runs the game.
    
    Params:
    WIndow(GraphWin): the window where the game play takes in.
    character(Image): the choosen character image.
    food(Image): the food image based on the character
    
    Returns:
    True if the player wins the game:
    '''
    count_contact = 0
    count_attack = 0
    
    food_list = []
    villan_list = []
        
    point_text = add_text_to_window(window, Point(635, 25), "", "White", 20, text_style = "italic")
    
    while count_contact < NUM_WIN and count_attack < NUM_LOSE:
        
        move_character(window,character)
        generate_object(window,food_list,villan_list,food)
        move_objects(food_list,villan_list)
        count_contact = check_and_remove_food(window,food_list,character,count_contact)
        count_attack = check_and_remove_villan(window,villan_list,character,count_attack,health_bar)
         
        point_text.setText(str(count_contact))
        
        time.sleep(STALL_TIME)
        
    return count_contact == NUM_WIN

def main():
     
    intro_window()
    insturction_window()
    character, food = selection_window()
    window = game_background_window()
    bar = add_health_bar_to_window(window)
    character.draw(window)
    win_lose = game_loop(window, character,food,bar)
    window.close() # close the main window 
    
    if win_lose:
        win_window()
    else:
        lose_window()

main()