'''
David Cimpoiasu , 2130140
R. Vincent , instructor
Advanced Programming , section 2
Final Project
'''

# By the way type: ignore is used to ignore the error that the IDE gives me

'''Main file to run the game'''


import pygame #Main library used for the game
from class_backgammon import * #Imports the classes from the class_backgammon file
import random #Used to generate random numbers
from tkinter import messagebox #Used to display messages

pygame.init() #Initializes pygame

Width, Height = 800, 600  # Width and Height of the window
Window = pygame.display.set_mode((Width, Height))  # Window itself

FPS = 15  # Frames per second


Background = pygame.image.load('Asset\\background.png')  # Background image
Black_piece = pygame.image.load('Asset\\black.png')  # Black piece image
Red_piece = pygame.image.load('Asset\\red.png')  # Red piece image
Transparent = pygame.Surface((50, 50), pygame.SRCALPHA)  # Transparent image
Dice1 = pygame.image.load('Asset\\1.png')  # Dice 1 image
Dice2 = pygame.image.load('Asset\\2.png')  # Dice 2 image
Dice3 = pygame.image.load('Asset\\3.png')  # Dice 3 image
Dice4 = pygame.image.load('Asset\\4.png')  # Dice 4 image
Dice5 = pygame.image.load('Asset\\5.png')  # Dice 5 image
Dice6 = pygame.image.load('Asset\\6.png')  # Dice 6 image
DiceT = pygame.Surface((20, 20), pygame.SRCALPHA)  # Dice transparent image (Not used in the end)
number_empty = pygame.image.load('Asset\\Number_empty.png')  # Number empty image


sysfont = pygame.font.get_default_font() # Default font
font = pygame.font.SysFont(None, 30) # Font used for the text #type: ignore




#DICE

Dx1 = 30  # X coordinate of the dice
Dy1 = 290  # Y coordinate of the dice
Dx2 = 60  # X coordinate of the dice
Dy2 = 290  # Y coordinate of the dice

D1 = pygame.Rect(Dx1,Dy1,20,20) # Dice 1
D2 = pygame.Rect(Dx2,Dy2,20,20) # Dice 2




# lanes ands each square on the board

#L{lane number}S{square number}

BOX = [] # List of all the squares on the board
l12s1 = pygame.Rect(30,25,50,50)
BOX.append(l12s1)
l12s2 = pygame.Rect(30,75,50,50)
BOX.append(l12s2)
l12s3 = pygame.Rect(30,125,50,50)
BOX.append(l12s3)
l12s4 = pygame.Rect(30,175,50,50)
BOX.append(l12s4)
l12s5 = pygame.Rect(30,225,50,50)
BOX.append(l12s5)
    
l11s1 = pygame.Rect(90,25,50,50)
BOX.append(l11s1)
l11s2 = pygame.Rect(90,75,50,50)
BOX.append(l11s2)
l11s3 = pygame.Rect(90,125,50,50)
BOX.append(l11s3)
l11s4 = pygame.Rect(90,175,50,50)
BOX.append(l11s4)
l11s5 = pygame.Rect(90,225,50,50)
BOX.append(l11s5)

l10s1 = pygame.Rect(150,25,50,50)
BOX.append(l10s1)
l10s2 = pygame.Rect(150,75,50,50)
BOX.append(l10s2)
l10s3 = pygame.Rect(150,125,50,50)
BOX.append(l10s3)
l10s4 = pygame.Rect(150,175,50,50)
BOX.append(l10s4)
l10s5 = pygame.Rect(150,225,50,50)
BOX.append(l10s5)

l9s1 = pygame.Rect(210,25,50,50)
BOX.append(l9s1)
l9s2 = pygame.Rect(210,75,50,50)
BOX.append(l9s2)
l9s3 = pygame.Rect(210,125,50,50)
BOX.append(l9s3)
l9s4 = pygame.Rect(210,175,50,50)
BOX.append(l9s4)
l9s5 = pygame.Rect(210,225,50,50)
BOX.append(l9s5)

l8s1 = pygame.Rect(270,25,50,50)
BOX.append(l8s1)
l8s2 = pygame.Rect(270,75,50,50)
BOX.append(l8s2)
l8s3 = pygame.Rect(270,125,50,50)
BOX.append(l8s3)
l8s4 = pygame.Rect(270,175,50,50)
BOX.append(l8s4)
l8s5 = pygame.Rect(270,225,50,50)
BOX.append(l8s5)

l7s1 = pygame.Rect(330,25,50,50)
BOX.append(l7s1)
l7s2 = pygame.Rect(330,75,50,50)
BOX.append(l7s2)
l7s3 = pygame.Rect(330,125,50,50)
BOX.append(l7s3)
l7s4 = pygame.Rect(330,175,50,50)
BOX.append(l7s4)
l7s5 = pygame.Rect(330,225,50,50)
BOX.append(l7s5)

l6s1 = pygame.Rect(420,25,50,50)
BOX.append(l6s1)
l6s2 = pygame.Rect(420,75,50,50)
BOX.append(l6s2)
l6s3 = pygame.Rect(420,125,50,50)
BOX.append(l6s3)
l6s4 = pygame.Rect(420,175,50,50)
BOX.append(l6s4)
l6s5 = pygame.Rect(420,225,50,50)
BOX.append(l6s5)

l5s1 = pygame.Rect(480,25,50,50)
BOX.append(l5s1)
l5s2 = pygame.Rect(480,75,50,50)
BOX.append(l5s2)
l5s3 = pygame.Rect(480,125,50,50)
BOX.append(l5s3)
l5s4 = pygame.Rect(480,175,50,50)
BOX.append(l5s4)
l5s5 = pygame.Rect(480,225,50,50)
BOX.append(l5s5)

l4s1 = pygame.Rect(540,25,50,50)
BOX.append(l4s1)
l4s2 = pygame.Rect(540,75,50,50)
BOX.append(l4s2)
l4s3 = pygame.Rect(540,125,50,50)
BOX.append(l4s3)
l4s4 = pygame.Rect(540,175,50,50)
BOX.append(l4s4)
l4s5 = pygame.Rect(540,225,50,50)
BOX.append(l4s5)

l3s1 = pygame.Rect(600,25,50,50)
BOX.append(l3s1)
l3s2 = pygame.Rect(600,75,50,50)
BOX.append(l3s2)
l3s3 = pygame.Rect(600,125,50,50)
BOX.append(l3s3)
l3s4 = pygame.Rect(600,175,50,50)
BOX.append(l3s4)
l3s5 = pygame.Rect(600,225,50,50)
BOX.append(l3s5)

l2s1 = pygame.Rect(660,25,50,50)
BOX.append(l2s1)
l2s2 = pygame.Rect(660,75,50,50)
BOX.append(l2s2)
l2s3 = pygame.Rect(660,125,50,50)
BOX.append(l2s3)
l2s4 = pygame.Rect(660,175,50,50)
BOX.append(l2s4)
l2s5 = pygame.Rect(660,225,50,50)
BOX.append(l2s5)

l1s1 = pygame.Rect(720,25,50,50)
BOX.append(l1s1)
l1s2 = pygame.Rect(720,75,50,50)
BOX.append(l1s2)
l1s3 = pygame.Rect(720,125,50,50)
BOX.append(l1s3)
l1s4 = pygame.Rect(720,175,50,50)
BOX.append(l1s4)
l1s5 = pygame.Rect(720,225,50,50)
BOX.append(l1s5)

l13s1 = pygame.Rect(30,525,50,50)
BOX.append(l13s1)
l13s2 = pygame.Rect(30,475,50,50)
BOX.append(l13s2)
l13s3 = pygame.Rect(30,425,50,50)
BOX.append(l13s3)
l13s4 = pygame.Rect(30,375,50,50)
BOX.append(l13s4)
l13s5 = pygame.Rect(30,325,50,50)
BOX.append(l13s5)

l14s1 = pygame.Rect(90,525,50,50)
BOX.append(l14s1)
l14s2 = pygame.Rect(90,475,50,50)
BOX.append(l14s2)
l14s3 = pygame.Rect(90,425,50,50)
BOX.append(l14s3)
l14s4 = pygame.Rect(90,375,50,50)
BOX.append(l14s4)
l14s5 = pygame.Rect(90,325,50,50)
BOX.append(l14s5)

l15s1 = pygame.Rect(150,525,50,50)
BOX.append(l15s1)
l15s2 = pygame.Rect(150,475,50,50)
BOX.append(l15s2)
l15s3 = pygame.Rect(150,425,50,50)
BOX.append(l15s3)
l15s4 = pygame.Rect(150,375,50,50)
BOX.append(l15s4)
l15s5 = pygame.Rect(150,325,50,50)
BOX.append(l15s5)

l16s1 = pygame.Rect(210,525,50,50)
BOX.append(l16s1)
l16s2 = pygame.Rect(210,475,50,50)
BOX.append(l16s2)
l16s3 = pygame.Rect(210,425,50,50)
BOX.append(l16s3)
l16s4 = pygame.Rect(210,375,50,50)
BOX.append(l16s4)
l16s5 = pygame.Rect(210,325,50,50)
BOX.append(l16s5)

l17s1 = pygame.Rect(270,525,50,50)
BOX.append(l17s1)
l17s2 = pygame.Rect(270,475,50,50)
BOX.append(l17s2)
l17s3 = pygame.Rect(270,425,50,50)
BOX.append(l17s3)
l17s4 = pygame.Rect(270,375,50,50)
BOX.append(l17s4)
l17s5 = pygame.Rect(270,325,50,50)
BOX.append(l17s5)

l18s1 = pygame.Rect(330,525,50,50)
BOX.append(l18s1)
l18s2 = pygame.Rect(330,475,50,50)
BOX.append(l18s2)
l18s3 = pygame.Rect(330,425,50,50)
BOX.append(l18s3)
l18s4 = pygame.Rect(330,375,50,50)
BOX.append(l18s4)
l18s5 = pygame.Rect(330,325,50,50)
BOX.append(l18s5)

l19s1 = pygame.Rect(420,525,50,50)
BOX.append(l19s1)
l19s2 = pygame.Rect(420,475,50,50)
BOX.append(l19s2)
l19s3 = pygame.Rect(420,425,50,50)
BOX.append(l19s3)
l19s4 = pygame.Rect(420,375,50,50)
BOX.append(l19s4)
l19s5 = pygame.Rect(420,325,50,50)
BOX.append(l19s5)

l20s1 = pygame.Rect(480,525,50,50)
BOX.append(l20s1)
l20s2 = pygame.Rect(480,475,50,50)
BOX.append(l20s2)
l20s3 = pygame.Rect(480,425,50,50)
BOX.append(l20s3)
l20s4 = pygame.Rect(480,375,50,50)
BOX.append(l20s4)
l20s5 = pygame.Rect(480,325,50,50)
BOX.append(l20s5)

l21s1 = pygame.Rect(540,525,50,50)
BOX.append(l21s1)
l21s2 = pygame.Rect(540,475,50,50)
BOX.append(l21s2)
l21s3 = pygame.Rect(540,425,50,50)
BOX.append(l21s3)
l21s4 = pygame.Rect(540,375,50,50)
BOX.append(l21s4)
l21s5 = pygame.Rect(540,325,50,50)
BOX.append(l21s5)

l22s1 = pygame.Rect(600,525,50,50)
BOX.append(l22s1)
l22s2 = pygame.Rect(600,475,50,50)
BOX.append(l22s2)
l22s3 = pygame.Rect(600,425,50,50)
BOX.append(l22s3)
l22s4 = pygame.Rect(600,375,50,50)
BOX.append(l22s4)
l22s5 = pygame.Rect(600,325,50,50)
BOX.append(l22s5)

l23s1 = pygame.Rect(660,525,50,50)
BOX.append(l23s1)
l23s2 = pygame.Rect(660,475,50,50)
BOX.append(l23s2)
l23s3 = pygame.Rect(660,425,50,50)
BOX.append(l23s3)
l23s4 = pygame.Rect(660,375,50,50)
BOX.append(l23s4)
l23s5 = pygame.Rect(660,325,50,50)
BOX.append(l23s5)

l24s1 = pygame.Rect(720,525,50,50)
BOX.append(l24s1)
l24s2 = pygame.Rect(720,475,50,50)
BOX.append(l24s2)
l24s3 = pygame.Rect(720,425,50,50)
BOX.append(l24s3)
l24s4 = pygame.Rect(720,375,50,50)
BOX.append(l24s4)
l24s5 = pygame.Rect(720,325,50,50)
BOX.append(l24s5)


WIN = pygame.Rect(800,600,50,50) #winning box to put pices out of the game


prison = [] #list of prison boxes
REDprison = pygame.Rect(330,275,50,50) #red prison
prison.append(REDprison)
BLACKprison = pygame.Rect(420,275,50,50) #black prison
prison.append(BLACKprison)


# RECTANGLE CREATION FINISHED

#initial position of pieces
Blist_initial_x = [l13s1, l13s2, l13s3, l13s4, l13s5, 
                 l8s1, l8s2, l8s3, l6s1, l6s2, l6s3, l6s4, l6s5, l24s1, l24s2
                 ]# List of the initial position of black pieces

Rlist_initial_x = [l12s1, l12s2, l12s3, l12s4, l12s5, l1s1, l1s2, 
                 l17s1, l17s2, l17s3, l19s1, l19s2, l19s3, l19s4, l19s5
                 ]# List of the initial position of red pieces

Blane_initial = [13,13,13,13,13,8,8,8,6,6,6,6,6,24,24] # List of the initial lane of black pieces
Rlane_initial = [12,12,12,12,12,1,1,17,17,17,19,19,19,19,19] # List of the initial lane of red pieces


Blist_real = [] #list of black pieces initial position
Rlist_real = [] #list of red pieces initial position

#create the pieces
for i in range(15):
    Blist_real.append([i+1, 'black', Blist_initial_x[i], Blane_initial[i]])
    Rlist_real.append([i+1, 'red', Rlist_initial_x[i], Rlane_initial[i]])

Breal = [] #list of black pieces
Rreal = [] #list of red pieces

#Creation of the pieces
    
B1 = pieces(Blist_real[0][0], Blist_real[0][1], Blist_real[0][2], Blist_real[0][3])
Breal.append(B1)
B2 = pieces(Blist_real[1][0], Blist_real[1][1], Blist_real[1][2], Blist_real[1][3])
Breal.append(B2)
B3 = pieces(Blist_real[2][0], Blist_real[2][1], Blist_real[2][2], Blist_real[2][3])
Breal.append(B3)
B4 = pieces(Blist_real[3][0], Blist_real[3][1], Blist_real[3][2], Blist_real[3][3])
Breal.append(B4)
B5 = pieces(Blist_real[4][0], Blist_real[4][1], Blist_real[4][2], Blist_real[4][3])
Breal.append(B5)
B6 = pieces(Blist_real[5][0], Blist_real[5][1], Blist_real[5][2], Blist_real[5][3])
Breal.append(B6)
B7 = pieces(Blist_real[6][0], Blist_real[6][1], Blist_real[6][2], Blist_real[6][3])
Breal.append(B7)
B8 = pieces(Blist_real[7][0], Blist_real[7][1], Blist_real[7][2], Blist_real[7][3])
Breal.append(B8)
B9 = pieces(Blist_real[8][0], Blist_real[8][1], Blist_real[8][2], Blist_real[8][3])
Breal.append(B9)
B10 = pieces(Blist_real[9][0], Blist_real[9][1], Blist_real[9][2], Blist_real[9][3])
Breal.append(B10)
B11 = pieces(Blist_real[10][0], Blist_real[10][1], Blist_real[10][2], Blist_real[10][3])
Breal.append(B11)
B12 = pieces(Blist_real[11][0], Blist_real[11][1], Blist_real[11][2], Blist_real[11][3])
Breal.append(B12)
B13 = pieces(Blist_real[12][0], Blist_real[12][1], Blist_real[12][2], Blist_real[12][3])
Breal.append(B13)
B14 = pieces(Blist_real[13][0], Blist_real[13][1], Blist_real[13][2], Blist_real[13][3])
Breal.append(B14)
B15 = pieces(Blist_real[14][0], Blist_real[14][1], Blist_real[14][2], Blist_real[14][3])
Breal.append(B15)

R1 = pieces(Rlist_real[0][0], Rlist_real[0][1], Rlist_real[0][2], Rlist_real[0][3])
Rreal.append(R1)
R2 = pieces(Rlist_real[1][0], Rlist_real[1][1], Rlist_real[1][2], Rlist_real[1][3])
Rreal.append(R2)
R3 = pieces(Rlist_real[2][0], Rlist_real[2][1], Rlist_real[2][2], Rlist_real[2][3])
Rreal.append(R3)
R4 = pieces(Rlist_real[3][0], Rlist_real[3][1], Rlist_real[3][2], Rlist_real[3][3])
Rreal.append(R4)
R5 = pieces(Rlist_real[4][0], Rlist_real[4][1], Rlist_real[4][2], Rlist_real[4][3])
Rreal.append(R5)
R6 = pieces(Rlist_real[5][0], Rlist_real[5][1], Rlist_real[5][2], Rlist_real[5][3])
Rreal.append(R6)
R7 = pieces(Rlist_real[6][0], Rlist_real[6][1], Rlist_real[6][2], Rlist_real[6][3])
Rreal.append(R7)
R8 = pieces(Rlist_real[7][0], Rlist_real[7][1], Rlist_real[7][2], Rlist_real[7][3])
Rreal.append(R8)
R9 = pieces(Rlist_real[8][0], Rlist_real[8][1], Rlist_real[8][2], Rlist_real[8][3])
Rreal.append(R9)
R10 = pieces(Rlist_real[9][0], Rlist_real[9][1], Rlist_real[9][2], Rlist_real[9][3])
Rreal.append(R10)
R11 = pieces(Rlist_real[10][0], Rlist_real[10][1], Rlist_real[10][2], Rlist_real[10][3])
Rreal.append(R11)
R12 = pieces(Rlist_real[11][0], Rlist_real[11][1], Rlist_real[11][2], Rlist_real[11][3])
Rreal.append(R12)
R13 = pieces(Rlist_real[12][0], Rlist_real[12][1], Rlist_real[12][2], Rlist_real[12][3])
Rreal.append(R13)
R14 = pieces(Rlist_real[13][0], Rlist_real[13][1], Rlist_real[13][2], Rlist_real[13][3])
Rreal.append(R14)
R15 = pieces(Rlist_real[14][0], Rlist_real[14][1], Rlist_real[14][2], Rlist_real[14][3])
Rreal.append(R15)




Real_pieces = [] #LIST OF ALL PIECES
for i in Breal: 
    Real_pieces.append(i) 
for i in Rreal:
    Real_pieces.append(i)

#SET THE DICE
Window.blit(Dice1, (D1.x, D1.y))
Window.blit(Dice1, (D2.x, D2.y))

#SET THE LANES
#Lane numbers goes from topright to bottomright in counter clockwise direction
List_lane = []
lane1 = lane(1)
List_lane.append(lane1)
lane2 = lane(2)
List_lane.append(lane2)
lane3 = lane(3)
List_lane.append(lane3)
lane4 = lane(4)
List_lane.append(lane4)
lane5 = lane(5)
List_lane.append(lane5)
lane6 = lane(6)
List_lane.append(lane6)
lane7 = lane(7)
List_lane.append(lane7)
lane8 = lane(8)
List_lane.append(lane8)
lane9 = lane(9)
List_lane.append(lane9)
lane10 = lane(10)
List_lane.append(lane10)
lane11 = lane(11)
List_lane.append(lane11)
lane12 = lane(12)
List_lane.append(lane12)
lane13 = lane(13)
List_lane.append(lane13)
lane14 = lane(14)
List_lane.append(lane14)
lane15 = lane(15)
List_lane.append(lane15)
lane16 = lane(16)
List_lane.append(lane16)
lane17 = lane(17)
List_lane.append(lane17)
lane18 = lane(18)
List_lane.append(lane18)
lane19 = lane(19)
List_lane.append(lane19)
lane20 = lane(20)
List_lane.append(lane20)
lane21 = lane(21)
List_lane.append(lane21)
lane22 = lane(22)
List_lane.append(lane22)
lane23 = lane(23)
List_lane.append(lane23)
lane24 = lane(24)
List_lane.append(lane24)


#initialize the lanes with the pieces
for i in Real_pieces:
    a = i.lane 
    if a == 1:
        lane1.add_piece(i) #add the piece to the lane
    elif a == 2:
        lane2.add_piece(i)
    elif a == 3:
        lane3.add_piece(i)
    elif a == 4:
        lane4.add_piece(i)
    elif a == 5:
        lane5.add_piece(i)
    elif a == 6:
        lane6.add_piece(i)
    elif a == 7:
        lane7.add_piece(i)
    elif a == 8:
        lane8.add_piece(i)
    elif a == 9:
        lane9.add_piece(i)
    elif a == 10:
        lane10.add_piece(i)
    elif a == 11:
        lane11.add_piece(i)
    elif a == 12:
        lane12.add_piece(i)
    elif a == 13:
        lane13.add_piece(i)
    elif a == 14:
        lane14.add_piece(i)
    elif a == 15:
        lane15.add_piece(i)
    elif a == 16:
        lane16.add_piece(i)
    elif a == 17:
        lane17.add_piece(i)
    elif a == 18:
        lane18.add_piece(i)
    elif a == 19:
        lane19.add_piece(i)
    elif a == 20:
        lane20.add_piece(i)
    elif a == 21:
        lane21.add_piece(i)
    elif a == 22:
        lane22.add_piece(i)
    elif a == 23:
        lane23.add_piece(i)
    elif a == 24:
        lane24.add_piece(i)
    

        
        

#Creatiof of variables DONE

#Onto pygame now

pygame.display.set_caption("Backgammon")  # Title of the window

def draw_window():  # Function to draw the window
    '''Draw the window and the pieces'''
    
    Window.blit(Background, (0, 0))  # Draw the background
    for i in Breal:  # For loop to draw the black pieces
        Window.blit(Black_piece, (i.location.x, i.location.y))  # type: ignore
    for i in Rreal:  # For loop to draw the red pieces
        Window.blit(Red_piece, (i.location.x, i.location.y))  # type: ignore
    

            
            
    #SET THE DICE
    Window.blit(Dice1, (D1.x, D1.y))
    Window.blit(Dice1, (D2.x, D2.y))
        
    pygame.display.update()  # Update the display
    
def roll_dice():  # Function to roll the dice
    '''Roll the dice and return the random numbers'''
    radom_number1 = random.randint(1, 6)  # Get a random number between 1 and 6
    radom_number2 = random.randint(1, 6)  # Get a random number between 1 and 6
    return radom_number1, radom_number2  # Return the random numbers



def starter():  # Function to get the starter
    '''Get the starter'''
    Player = None
    messagebox.showinfo('Roll the dice','Roll the dice to see who starts') # Show a message box to tell the players to roll the dice
    k = random.randint(0, 1) # Get a random number between 0 and 1
    if k == 0: # If the number is 0
        messagebox.showinfo('Player','Red starts') # Show a message box to tell the players that red starts
        Player = 'red' # Set the player to red
    if k == 1: # If the number is 1
        messagebox.showinfo('Player','Black starts') # Show a message box to tell the players that black starts
        Player = 'black' # Set the player to black
    
    
    return Player


def showvalidmoves(lane = 0, D1 = 0, D2 = 0, color = None): #Function to show the valid moves
    '''Show the valid moves of the piece'''
    P = [] # makes sure code does not crash if no valid moves
    if color == 'red': # If the color is red
        P = [] # Create a list to store the valid moves temporarily
        Pd1,Pd2, Pd3 = None, None, None # Create variables to store the valid moves
        if D1+lane <25 and D1 != 0: # If the sum of the dice 1 and the lane is less than 25 and the dice is not 0
            Pd1 = D1+lane
            P.append(Pd1)
        if D2+lane <25 and D2 != 0: # If the sum of the dice 2 and the lane is less than 25 and the dice is not 0
            Pd2 = D2+lane
            P.append(Pd2)
        if D1 == D2 and D1+lane <25 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the sum of the dice 1 and the lane is less than 25 and the dice 1 and the dice 2 are not 0
            Pd3 = D1+lane
            P.append(Pd3)
        if D1+lane >= 25 and D1 != 0: # If the sum of the dice 1 and the lane is greater than or equal to 25 and the dice 1 is not 0
            Pd1 = 24
            P.append(Pd1)
        if D2+lane >= 25 and D2 != 0: # If the sum of the dice 2 and the lane is greater than or equal to 25 and the dice 2 is not 0
            Pd2 = 24
            P.append(Pd2)
        if D1 == D2 and D1+lane >= 25 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the sum of the dice 1 and the lane is greater than or equal to 25 and the dice 1 and the dice 2 are not 0
            Pd3 = 24
            P.append(Pd3)
            
            
    if color == 'black': # If the color is black
        if lane == 0: # If the lane is 0
            lane = 25 # Set the lane to 25
        P = [] # Create a list to store the valid moves temporarily
        Pd1,Pd2, Pd3 = None, None, None # Create variables to store the valid moves
        if lane-D1 >0 and D1 != 0: # If the lane minus the dice 1 is greater than 0 and the dice 1 is not 0
            Pd1 = lane-D1
            P.append(Pd1)
        if lane-D2 >0 and D2 != 0: # If the lane minus the dice 2 is greater than 0 and the dice 2 is not 0
            Pd2 = lane-D2
            P.append(Pd2)
        if D1 == D2 and lane-D1 >0 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the lane minus the dice 1 is greater than 0 and the dice 1 and the dice 2 are not 0
            Pd3 = lane-D1
            P.append(Pd3)
        if lane-D1 <= 0 and D1 != 0: # If the lane minus the dice 1 is less than or equal to 0 and the dice 1 is not 0
            Pd1 = 1
            P.append(Pd1)
        if lane-D2 <= 0 and D2 != 0: # If the lane minus the dice 2 is less than or equal to 0 and the dice 2 is not 0
            Pd2 = 1
            P.append(Pd2)
        if D1 == D2 and lane-D1 <= 0 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the lane minus the dice 1 is less than or equal to 0 and the dice 1 and the dice 2 are not 0
            Pd3 = 1
            P.append(Pd3)
            
            
    #convert to lane
    Loc = [] # Create a list to store the valid moves
    for k in P:
        if k != None: # If the valid move is not None
            for i in List_lane:
                if i.number == k: # If the lane number is equal to the valid move
                    if color == 'red' and i.color == 'black': # If the color is red and the lane color is black
                        continue
                    if color == 'black' and i.color == 'red': # If the color is black and the lane color is red
                        continue
                    if i.length < 5: # If the lane length is less than 5
                        Tx = eval('l{}s{}'.format(i.number, i.length+1)).x # Set the x coordinate of the valid move to the x coordinate of the lane
                        Ty = eval('l{}s{}'.format(i.number, i.length+1)).y # Set the y coordinate of the valid move to the y coordinate of the lane
                        Loc.append(['l{}s{}'.format(i.number, i.length+1), i.number]) # Add the valid move to the list
                    if i.length >= 5: # If the lane length is greater than or equal to 5
                        Tx = eval('l{}s1'.format(i.number)).x # Set the x coordinate of the valid move to the x coordinate of the lane
                        Ty = eval('l{}s1'.format(i.number)).y # Set the y coordinate of the valid move to the y coordinate of the lane
                        Loc.append(['l{}s1'.format(i.number), i.number]) # Add the valid move to the list
                    pygame.draw.rect(Window, (0, 255, 0), (Tx, Ty, 50, 50),2) # Draw a green rectangle on the valid move
    return Loc



def capturemoves(lane = 0, D1 = 0, D2 = 0, color = None): # Create a function to find the valid capture moves
    '''Search for valid capture moves'''
    P = [] # make sure the code dont crash
    if color == 'red': # If the color is red
        P = [] # Create a list to store the valid moves temporarily
        Pd1,Pd2, Pd3 = None, None, None # Create variables to store the valid moves
        if D1+lane <25 and D1 != 0: # If the sum of the dice 1 and the lane is less than 25 and the dice 1 is not 0
            Pd1 = D1+lane
            P.append(Pd1)
        if D2+lane <25 and D2 != 0: # If the sum of the dice 2 and the lane is less than 25 and the dice 2 is not 0
            Pd2 = D2+lane
            P.append(Pd2)
        if D1 == D2 and D1+lane <25 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the sum of the dice 1 and the lane is less than 25 and the dice 1 and the dice 2 are not 0
            Pd3 = D1+lane
            P.append(Pd3)
        if D1+lane >= 25 and D1 != 0: # If the sum of the dice 1 and the lane is greater than or equal to 25 and the dice 1 is not 0
            Pd1 = 24
            P.append(Pd1)
        if D2+lane >= 25 and D2 != 0: # If the sum of the dice 2 and the lane is greater than or equal to 25 and the dice 2 is not 0
            Pd2 = 24
            P.append(Pd2)
        if D1 == D2 and D1+lane >= 25 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the sum of the dice 1 and the lane is greater than or equal to 25 and the dice 1 and the dice 2 are not 0
            Pd3 = 24
            P.append(Pd3)
            
            
    if color == 'black': # If the color is black
        if lane == 0: # If the lane is 0
            lane = 25 # Set the lane to 25
        P = [] # Create a list to store the valid moves temporarily
        Pd1,Pd2, Pd3 = None, None, None # Create variables to store the valid moves
        if lane-D1 >0 and D1 != 0: # If the lane minus the dice 1 is greater than 0 and the dice 1 is not 0
            Pd1 = lane-D1
            P.append(Pd1)
        if lane-D2 >0 and D2 != 0: # If the lane minus the dice 2 is greater than 0 and the dice 2 is not 0
            Pd2 = lane-D2
            P.append(Pd2)
        if D1 == D2 and lane-D1 >0 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the lane minus the dice 1 is greater than 0 and the dice 1 and the dice 2 are not 0
            Pd3 = lane-D1
            P.append(Pd3)
        if lane-D1 <= 0 and D1 != 0: # If the lane minus the dice 1 is less than or equal to 0 and the dice 1 is not 0
            Pd1 = 1
            P.append(Pd1)
        if lane-D2 <= 0 and D2 != 0: # If the lane minus the dice 2 is less than or equal to 0 and the dice 2 is not 0
            Pd2 = 1
            P.append(Pd2)
        if D1 == D2 and lane-D1 <= 0 and D1 != 0 and D2 != 0: # If the dice 1 and the dice 2 are equal and the lane minus the dice 1 is less than or equal to 0 and the dice 1 and the dice 2 are not 0
            Pd3 = 1
            P.append(Pd3)
            
    #convert to lane
    poc = [] # Create a list to store the valid capture moves
    YY = False # Create a variable to check if the valid capture move is found (DEBUG PURPOSES)
    for k in P: # For every valid move
        if k != None: # If the valid move is not None
            for i in List_lane: # For every lane
                if i.number == k: # If the lane number is equal to the valid move
                    if color == 'red' and i.color == 'black' and i.length == 1: # If the color is red and the lane color is black and the lane length is 1
                        Tx = eval('l{}s1'.format(i.number)).x # Get the x coordinate of the lane
                        Ty = eval('l{}s1'.format(i.number)).y # Get the y coordinate of the lane
                        poc.append(['l{}s1'.format(i.number), i.number]) # Append the valid capture move to the list
                        YY = True # Set the variable to True (DEBUG PURPOSES)
                    if color == 'black' and i.color == 'red' and i.length == 1: # If the color is black and the lane color is red and the lane length is 1
                        Tx = eval('l{}s1'.format(i.number)).x # Get the x coordinate of the lane
                        Ty = eval('l{}s1'.format(i.number)).y # Get the y coordinate of the lane
                        poc.append(['l{}s1'.format(i.number), i.number]) # Append the valid capture move to the list
                        YY = True # Set the variable to True (DEBUG PURPOSES)
                    if YY == True: # If the variable is True (DEBUG PURPOSES)
                        pygame.draw.rect(Window, (0, 255, 0), (Tx, Ty, 50, 50),2) # Draw a green rectangle around the valid capture move (DEBUG PURPOSES)
    return poc
                    
                        
def draw_dice(d1,d2): # Function to draw the dice
    '''Draws the dice on the screen'''
    if d1 == 1:
        Window.blit(Dice1, (D1.x, D1.y)) # Dice 1 to Dice 6 are images of the dice
    elif d1 == 2:
        Window.blit(Dice2, (D1.x, D1.y))
    elif d1 == 3:
        Window.blit(Dice3, (D1.x, D1.y))
    elif d1 == 4:
        Window.blit(Dice4, (D1.x, D1.y))
    elif d1 == 5:
        Window.blit(Dice5, (D1.x, D1.y))
    elif d1 == 6:
        Window.blit(Dice6, (D1.x, D1.y))
    
    if d2 == 1:
        Window.blit(Dice1, (D2.x, D2.y))
    elif d2 == 2:
        Window.blit(Dice2, (D2.x, D2.y))
    elif d2 == 3:
        Window.blit(Dice3, (D2.x, D2.y))
    elif d2 == 4:
        Window.blit(Dice4, (D2.x, D2.y))
    elif d2 == 5:
        Window.blit(Dice5, (D2.x, D2.y))
    elif d2 == 6:
        Window.blit(Dice6, (D2.x, D2.y))                 
                
    
    



def main():  # Main function
    '''Main function to run the game'''
    Player = starter() # Get the player
    Turn_play = True # Variable to check if the player can play
    Movesequence = True # Variable to check if the player can move
    move = 0 # Variable to check how much the player can move
    Loc = [] # List to store the valid moves (short for location)
    poc = [] # List to store the valid capture moves (prison + location = poc)
    ppc = [] # List to store the valid prison moves (prison + prison + location = ppc)
    RP = 0 # Variable to see how many peices in prison for red
    BP = 0 # Variable to see how many peices in prison for black
    PP = None # Variable that may store the peice that is in prison (short for Playing Peice)
    double = False # Variable to check if the player rolled a double
    click = False # Variable to check if the player clicked on a peice (DEBUG PURPOSES)
    prisonR = False # Variable to check if the red player is in prison
    prisonB = False # Variable to check if the black player is in prison
    INPRISON = False # Variable to check if the player can move while prison is true (DEBUG PURPOSES)
    Prison_play = False # Variable to check if the player can play a peice out of prison
    winingR = False # Variable to check if the red player has all the pieces in the home
    winingB = False # Variable to check if the black player has all the pieces in the home
    RW = 0 # Variable to check how many peices are out of the board for red
    BW = 0 # Variable to check how many peices are out of the board for black
    skip = False # Variable to check if the player can skip a turn

    
    
    clock = pygame.time.Clock()  # Clock to control the FPS 
    
    
    run = True  # Variable to run the game
    draw_window() # Draw the window
    
    
    while run:  # While loop to run the game
        
        
        
        
        mouse = pygame.mouse.get_pos()  # Get the position of the mouse
        
        
        
        #over a box
        if D1.x <= mouse[0] <= D1.x + 20 and D1.y <= mouse[1] <= D1.y + 20: # If the mouse is over the dice 1 hilight it
            pygame.draw.rect(Window, (0, 255, 0), (D1.x, D1.y, 20, 20),2)
        else:
            pygame.draw.rect(Window, (255, 255, 255), (D1.x, D1.y, 20, 20),2) # Else draw a white rectangle around it
        
        if D2.x <= mouse[0] <= D2.x + 20 and D2.y <= mouse[1] <= D2.y + 20: # If the mouse is over the dice 2 hilight it
            pygame.draw.rect(Window, (0, 255, 0), (D2.x, D2.y, 20, 20),2)
        else:
            pygame.draw.rect(Window, (255, 255, 255), (D2.x, D2.y, 20, 20),2) # Else draw a white rectangle around it
            
        if Movesequence == True: # If the player can move
            for i in BOX: # For loop to check if the mouse is over a box
                if i.x <= mouse[0] <= i.x + 50 and i.y <= mouse[1] <= i.y + 50: # If the mouse is over a box hilight it
                    pygame.draw.rect(Window, (0, 255, 0), (i.x, i.y, 50, 50),2)
                else:
                    pygame.draw.rect(Window, (0, 0, 0), (i.x, i.y, 50, 50),2) # Else draw a black rectangle around it
        
        for i in prison: # For loop to check if the mouse is over a prison box
            if i.x <= mouse[0] <= i.x + 50 and i.y <= mouse[1] <= i.y + 50: # If the mouse is over a prison box hilight it
                pygame.draw.rect(Window, (0, 255, 0), (i.x, i.y, 50, 50),2)
            else:
                pygame.draw.rect(Window, (0, 0, 0), (i.x, i.y, 50, 50),2) # Else draw a black rectangle around it
            
        

        
        clock.tick(FPS)  # Tick the clock, controled by FPS
        for event in pygame.event.get():  # For loop to get the events of the game
            if event.type == pygame.QUIT:  # If the event is to quit the game AKA press the X button
                run = False  # Stop the game
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # If the player clicks
            
            
            ''' This is quite the long loop which I couldve have been optimized and made more function, like the showvalidmoves and capturemoves ones, but I didnt have time
            to do so. This if statement is to check if the player clicked on a peice and if the peice is valid to move. If the peice is valid
            then it will move the peice to the location that the player clicked on. It will also check if the player rolled a double. Now
            there are multiple types of moves that the player can do. The first one is a normal move (LOC), which is just moving the peice to valid
            location. The second one is a capture move (POC), which is when the player can capture a peice of the other player. The third one is
            a prison move (PPC), which is when the player can move a peice out of prison. The fourth one is a win move (WinningR or B), which is when the player has
            all the peices in the home.'''
            
            if move > 0 and Movesequence == True and (RP == 0 or BP == 0): # If the player can move and the player is not in prison 
                
                for i in BOX:  # For loop to check if the player clicked on a box
                    
                    
                    
                    if i.x <= mouse[0] <= i.x + 50 and i.y <= mouse[1] <= i.y + 50: # If the player clicked on a box 
                        
                        Movesequence = False # Stop the player from moving
                        
                        for l in Real_pieces: # For loop to check if the player clicked on a peice
                            
                            if l.location.x == i.x and l.location.y == i.y: # If the player clicked on a peice
                                
                                if l.color == 'red' and Player == 'red' and prisonR == False and (winingR == False): # If the player clicked on a red peice and the player is red and the player is not in prison and the player is not winning

                                    Loc = showvalidmoves(l.lane, d1, d2, l.color) # Get the valid moves for the peice
                                    poc = capturemoves(l.lane, d1, d2, l.color) # Get the capture moves for the peice
                                    PP = l # Set the peice to PP
                                    click = True # Set click to true
                                    pygame.display.update() # Update the display
                                    
                                elif l.color == 'black' and Player == 'black' and prisonB == False and (winingB == False): # If the player clicked on a black peice and the player is black and the player is not in prison and the player is not winning

                                    Loc = showvalidmoves(l.lane, d1, d2, l.color) # Get the valid moves for the peice
                                    poc = capturemoves(l.lane, d1, d2, l.color) # Get the capture moves for the peice
                                    PP = l # Set the peice to PP
                                    click = True # Set click to true
                                    pygame.display.update() # Update the display
                                    
                                elif l.color == 'red' and Player == 'red' and winingR == True: # If the player clicked on a red peice and the player is red and the player is winning
                                    '''I know I really couldve made this into a function but I didnt have time to do so'''
                                    
                                    skip = True # Set skip to true
                                    if l.lane == 25 - d1 and double == False: # If the peice is in the valid location of d1
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN
                                        
                                        RW +=1 # Add 1 to the red win counter
                                        move -= 1 # Subtract 1 from the move counter
                                        d1 = 0 # Set d1 to 0
                                        skip = False # Set skip to false
                                        
                                    if l.lane == 25 - d2 and double == False: # If the peice is in the valid location of d2
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN
                                        
                                        RW +=1 # Add 1 to the red win counter
                                        move -= 1 # Subtract 1 from the move counter
                                        d2 = 0 # Set d2 to 0
                                        skip = False # Set skip to false
                                        
                                    if l.lane == 25 - d1 and double == True: # If the peice is in the valid location of d1 and the player rolled a double
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN
                                       
                                        RW +=1 # Add 1 to the red win counter
                                        move -= 1 # Subtract 1 from the move counter
                                        skip = False # Set skip to false
                                        
                                    if l.lane == 25 - d2 and double == True: # If the peice is in the valid location of d2 and the player rolled a double
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN
                                        
                                        RW +=1 # Add 1 to the red win counter
                                        move -= 1 # Subtract 1 from the move counter
                                        skip = False # Set skip to false
                                        
                                    if skip == True:  # If the player didnt click on a valid location or there is no peice in the valid location
                                        
                                        Loc = showvalidmoves(l.lane, d1, d2, l.color) # Get the valid moves for the peice
                                        poc = capturemoves(l.lane, d1, d2, l.color) # Get the capture moves for the peice
                                        PP = l # Set the peice to PP
                                        click = True # Set click to true
                                        pygame.display.update() # Update the display
                                        
                                        
                                    if move == 2: # If the player rolled a double or exhausted all the extra moves
                                        double = False # Set double to false
                                        
                                    if move == 0: # If the player exhausted all the moves
                                        
                                        if Player == 'red': # If the player is red
                                            Player = 'black' # Set the player to black
                                        else:
                                            Player = 'red' # Set the player to red
                                            
                                        Turn_play = True # Set Turn_play to true
                                        
                                    Window.blit(Background, (0, 0))  # Draw the background 
                                    
                                    for yy in Breal:  # For loop to draw the black pieces
                                        Window.blit(Black_piece, (yy.location.x, yy.location.y))  # type: ignore
                                        
                                    for yy in Rreal:  # For loop to draw the red pieces
                                        Window.blit(Red_piece, (yy.location.x, yy.location.y))  # type: ignore
                                        
                                    draw_dice(d1, d2) # Draw the dice
                                    pygame.display.update() # Update the display
                                
                                elif l.color == 'black' and Player == 'black' and winingB == True: # If the player clicked on a black peice and the player is black and the player is winning
                                    
                                    skip = True # Set skip to true
                                    
                                    if l.lane == 25 - d1 and double == False: # If the peice is in the valid location of d1
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN

                                        BW +=1 # Add 1 to the black win counter
                                        move -= 1 # Subtract 1 from the move counter
                                        d1 = 0 # Set d1 to 0
                                        skip = False # Set skip to false
                                        
                                    if l.lane == 25 - d2 and double == False: # If the peice is in the valid location of d2
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN

                                        BW +=1 # Add 1 to the black win counter
                                        move -= 1 # Subtract 1 from the move counter
                                        d2 = 0 # Set d2 to 0
                                        skip = False # Set skip to false
                                        
                                    if l.lane == 25 - d1 and double == True: # If the peice is in the valid location of d1 and the player rolled a double
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN
                                        
                                        BW +=1 # Add 1 to the black win counter
                                        move -= 1 # Subtract 1 from the move counter
                                        skip = False # Set skip to false
                                        
                                    if l.lane == 25 - d2 and double == True: # If the peice is in the valid location of d2 and the player rolled a double
                                        eval('lane{}'.format(l.lane)).remove_piece(l) # Remove the peice from the lane
                                        l = (WIN, -1) # Set the peice to WIN
                                        
                                        BW +=1 # Add 1 to the black win counter
                                        move -= 1  # Subtract 1 from the move counter
                                        skip = False # Set skip to false
                                        
                                    if skip == True: # If the player didnt click on a valid location or there is no peice in the valid location
                                        Loc = showvalidmoves(l.lane, d1, d2, l.color) # Get the valid moves for the peice
                                        poc = capturemoves(l.lane, d1, d2, l.color) # Get the capture moves for the peice
                                        PP = l # Set the peice to PP
                                        click = True # Set click to true
                                        pygame.display.update() # Update the display
                                        
                                    if move == 2: # If the player rolled a double or exhausted all the extra moves
                                        double = False # Set double to false
                                        
                                    if move == 0: # If the player exhausted all the moves
                                        
                                        if Player == 'red': # If the player is red
                                            Player = 'black' # Set the player to black
                                            
                                        else: # If the player is black
                                            Player = 'red' # Set the player to red
                                            
                                        Turn_play = True # Set Turn_play to true
                                    
                                        
                                        
                                else: # If the player clicked on a peice that is not in the valid location
                                    print('Not your piece or you have a piece in prison') 
                                    Movesequence = True # Set Movesequence to true
                                    Loc = [] # Set Loc to an empty list
                                    PP = None # Set PP to None
                                    
                                if Loc == [] and poc == []: # If there are no valid moves and no capture moves
                                    print('No valid moves') 
                                    Movesequence = True # Set Movesequence to true
                                    PP = None # Set PP to None
                                    
                                    
                                    
                                    
                                    
            #print(INPRISON, Movesequence, move) #for debugging
            
            if move > 0 and INPRISON == True: #if there are moves left and the player can move out of prison (BUGGY and couldve made into a function)
                
                #print('INPRISON passed') #for debugging
                
                for i in prison: #for every piece in prison
                    
                    #print(i.x, i.y, mouse[0], mouse[1]) #for debugging
                    
                    if i.x <= mouse[0] <= i.x + 50 and i.y <= mouse[1] <= i.y + 50: #if the player clicked on a prison piece
                        Movesequence = False #set Movesequence to false
                        
                        for l in Real_pieces:  #for every piece on the board
                            
                            #print(l.location.x, l.location.y, i.x, i.y) #for debugging
                            
                            if l.location.x == i.x and l.location.y == i.y: # Find what piece it was
                                
                                #print('l passed') #for debugging
                                
                                if l.color == 'black': #if the piece is black
                                    
                                    #print('black passed') #for debugging
                                    
                                    for o in range(19, 25): #show available moves in opposite base
                                        
                                        if 25 - o == d1 or 25 - o == d2: #if the move is valid
                                            
                                            if eval('lane{}'.format(o)).pieces == [] or (eval('lane{}'.format(o)).length == 1 and eval('lane{}'.format(o)).color == 'red'): #if the lane is empty or has a red piece
                                                TTx = i.x #set the temporary x and y to the prison piece
                                                TTy = i.y 
                                                
                                                Tx = eval('l{}s1'.format(o)).x #set the x and y to the lane
                                                Ty = eval('l{}s1'.format(o)).y 
                                                
                                                ppc.append(eval('l{}s1'.format(o))) #add the lane to the list of possible moves
                                                
                                                pygame.draw.rect(Window, (0, 255, 0), (Tx, Ty, 50, 50),2) #draw a green box around the lane
                                                
                                                #print('Prison_play passed, maybe...') #for debugging
                                                
                                                Prison_play = True #set Prison_play to true
                                                
                                                pygame.display.update() #update the display
                                                
                                elif l.color == 'red':  #if the piece is red
                                    
                                    #print('red passed') #for debugging
                                    
                                    for o in range(1,7): #show available moves
                                        
                                        if o == d1 or o == d2: #if the move is valid
                                            
                                            if eval('lane{}'.format(o)).pieces == [] or (eval('lane{}'.format(o)).length == 1 and eval('lane{}'.format(o)).color == 'black'): #if the lane is empty or has a black piece
                                                TTx = i.x #set the temporary x and y to the prison piece
                                                TTy = i.y
                                                
                                                Tx = eval('l{}s1'.format(o)).x #set the x and y to the lane
                                                Ty = eval('l{}s1'.format(o)).y
                                                
                                                ppc.append(eval('l{}s1'.format(o))) #add the lane to the list of possible moves
                                                
                                                pygame.draw.rect(Window, (0, 255, 0), (Tx, Ty, 50, 50),2) #draw a green box around the lane
                                                
                                                Prison_play = True #set Prison_play to true
                                                
                                                pygame.display.update() #update the display
                                                
                if ppc == [] and Prison_play == True and (STUCK == False or d1 == d2): #if there are no valid moves out of prison (This part is the buggiest of the whole program and dont have time to fix it)
                    
                    STUCK = True #set STUCK to true (STUCK is a variable that is used to make sure that the player doesnt get stuck in prison) (Debugging purposes)
                    
                    print('No valid moves, onto the next player') 
                    
                    d1 = 0 #reset the dice
                    d2 = 0
                    
                    Movesequence = True #set Movesequence to true to restart the turn
                    
                    PP = None #set PP to None to restart the turn
                    
                    move = 0 #set move to 0 to restart the turn
                    
                    if Player == 'red': #if the player is red
                        Player = 'black' #set the player to black
                    else:
                        Player = 'red' #set the player to red
                        
                    Turn_play = True #set Turn_play to true to restart the turn
                                            
                                            
                                            
                                            
            #print(move, Movesequence, INPRISON, Prison_play, ppc) #for debugging
            
            if move > 0 and Movesequence == False and INPRISON == True and Prison_play == True and ppc != []: #if there are moves left and the player can move out of prison and there are valid moves
                
                STUCK = False #set STUCK to false (Debugging purposes)
                
                #print('ppc passed', ppc) #for debugging
                
                for i in ppc: #for every possible move
                    
                    if i.x <= mouse[0] <= i.x + 50 and i.y <= mouse[1] <= i.y + 50: #if the player clicked on a possible move
                        
                        #print('clicked on a valid move') #for debugging
                        
                        for l in Real_pieces: #for every piece on the board
                            
                            if l.location.x == TTx and l.location.y == TTy: #find the prison piece
                                
                                #print('l passed') #for debugging
                                
                                if l.color == 'black': #if the piece is black
                                    
                                    #print('black passed') #for debugging
                                    
                                    CC = 18 #set CC to 18 (lane number counter of opposite base, acts like a 0)
                                    
                                    for o in [l19s1, l20s1, l21s1, l22s1, l23s1, l24s1]: #for every lane in the opposite base
                                        
                                        CC += 1  #add 1 to CC (Changes the lane number)
                                        
                                        if o.x == i.x and o.y == i.y:  #find the lane that the player clicked on
                                            
                                            if eval('lane{}'.format(CC)).pieces != [] and eval('lane{}'.format(CC)).color == 'red': #if the lane has a red piece
                                                
                                                eval('lane{}'.format(CC)).pieces[0].move(REDprison, 0) #move the red piece to prison
                                                eval('lane{}'.format(CC)).remove_piece(eval('lane{}'.format(CC)).pieces[0]) #remove the red piece from the lane
                                                
                                                RP += 1 #add 1 to the red prison counter
                                                prisonR = True #set prisonR to true
                                                INPRISON = True #set INPRISON to true (Debugging purposes)
                                                
                                                print('Red in prison')
                                                
                                                Movesequence = True #set Movesequence to true to continue onto next move
                                                
                                                eval('lane{}'.format(CC)).add_piece(l) #add the black piece to the lane
                                                
                                                l.move(o, CC) #move the black piece to the lane
                                                
                                                STUCK = False #set STUCK to false (Debugging purposes)
                                                
                                            else: #if the lane is empty or has a black piece (CANNOT MOVE TO ANOTHER BLACK PIECE YET, oops)
                                                
                                                eval('lane{}'.format(CC)).add_piece(l) #add the black piece to the lane
                                                
                                                l.move(o, CC) #move the black piece to the lane
                                                
                                                STUCK = False #set STUCK to false (Debugging purposes)
                                            
                                            BP -= 1 #subtract 1 from the black prison counter
                                            
                                            if BP == 0: #if the black prison counter is 0
                                                prisonB = False #set prisonB to false
                                                
                                            if RP == 0 and BP == 0: #if the black and red prison counters are 0
                                                INPRISON = False #set INPRISON to false (Debugging purposes)
                                                Prison_play = False #set Prison_play to false
                                                
                                            TTx = None #reset the temporary x and y
                                            TTy = None 
                                                                                        
                                            if d1 == 25 - CC and double == False: #if the dice roll is equal to the lane number and the player didnt roll a double
                                                d1 = 0 #reset the dice
                                            if d2 == 25 - CC and double == False: #if the dice roll is equal to the lane number and the player didnt roll a double
                                                d2 = 0 #reset the dice
                                                
                                            move -= 1 #subtract 1 from the move counter
                                            print('Move:', move)
                                            
                                            if move == 2: #if the move counter is 2
                                                double = False #set double to false
                                            CC = 18 #reset CC
                                            
                                            ppc = [] #reset ppc
                                            
                                            
                                elif l.color == 'red': #if the piece is red
                                    
                                    CC = 0 #set CC to 0 (lane number counter of opposite base)
                                    
                                    for o in [l1s1, l2s1, l3s1, l4s1, l5s1, l6s1]: #for every lane in the opposite base
                                        
                                        CC += 1 #add 1 to CC (Changes the lane number)
                                        
                                        if o.x == i.x and o.y == i.y: #find the lane that the player clicked on
                                            
                                            if eval('lane{}'.format(CC)).pieces != [] and eval('lane{}'.format(CC)).pieces[0].color == 'black': #if the lane has a black piece
                                                
                                                eval('lane{}'.format(CC)).pieces[0].move(BLACKprison, 0) #move the black piece to prison
                                                eval('lane{}'.format(CC)).remove_piece(eval('lane{}'.format(CC)).pieces[0]) #remove the black piece from the lane
                                                
                                                BP += 1 #add 1 to the black prison counter
                                                
                                                prisonB = True #set prisonB to true
                                                
                                                INPRISON = True #set INPRISON to true (Debugging purposes)
                                                
                                                print('Black in prison') #print that the black piece is in prison
                                                
                                                Movesequence = True #set Movesequence to true to continue onto next move
                                                
                                                eval('lane{}'.format(CC)).add_piece(l) #add the red piece to the lane
                                                
                                                l.move(o, CC) #move the red piece to the lane
                                                
                                                STUCK = False #set STUCK to false (Debugging purposes)
                                                
                                            else: #if the lane is empty or has a red piece (CANNOT MOVE TO ANOTHER RED PIECE YET, oops)
                                                
                                                eval('lane{}'.format(CC)).add_piece(l) #add the red piece to the lane
                                                
                                                l.move(o, CC) #move the red piece to the lane
                                                
                                                STUCK = False #set STUCK to false (Debugging purposes)
                                                
                                            RP -= 1 #subtract 1 from the red prison counter
                                            
                                            if RP == 0: #if the red prison counter is 0
                                                prisonR = False #set prisonR to false
                                                
                                            if RP == 0 and BP == 0: #if the black and red prison counters are 0
                                                INPRISON = False #set INPRISON to false (Debugging purposes)
                                                Prison_play = False #set Prison_play to false
                                                
                                            TTx = None #reset the temporary x and y
                                            TTy = None
                                            
                                            if d1 == CC and double == False: #if the dice roll is equal to the lane number and the player didnt roll a double
                                                d1 = 0 #reset the dice
                                            if d2 == CC and double == False: #if the dice roll is equal to the lane number and the player didnt roll a double
                                                d2 = 0 #reset the dice
                                                
                                            move -= 1 #subtract 1 from the move counter
                                            print('Move:', move) 
                                            
                                            if move == 2: #if the move counter is 2
                                                double = False #set double to false
                                                
                                            CC = 0 #reset CC
                                            ppc = [] #reset ppc
                                            
                                Window.blit(Background, (0, 0))  # Draw the background
                                
                                for yy in Breal:  # For loop to draw the black pieces
                                    Window.blit(Black_piece, (yy.location.x, yy.location.y))  # type: ignore
                                    
                                for yy in Rreal:  # For loop to draw the red pieces
                                     Window.blit(Red_piece, (yy.location.x, yy.location.y))  # type: ignore
                                     
                                draw_dice(d1, d2) # Draw the dice
                                 
                                pygame.display.update() # Update the display
                                
                                Movesequence = True #set Movesequence to true to continue onto next move
                                
                                if move == 0: #if the move counter is 0
                                    
                                    if Player == 'red': #if the player is red
                                        Player = 'black' #set the player to black
                                        
                                    else:
                                        Player = 'red' #set the player to red
                                        
                                    Turn_play = True #set Turn_play to true

                            
                                
                                
                                
                                
                
            if Loc != [] and Movesequence == False and (RP == 0 or BP == 0): #Move the piece to valid move if the player has no pieces in prison (Could be a function)
                
                for o in Loc: #for every location in Loc
                    
                    if eval(o[0]).x <= mouse[0] <= eval(o[0]).x + 50 and eval(o[0]).y <= mouse[1] <= eval(o[0]).y + 50: #if the player clicks on a location in Loc
                        
                        for l in Real_pieces: #for every piece in Real_pieces
                            
                            if l.location.x == PP.location.x and l.location.y == PP.location.y and click == True: #find the piece that the player clicked on
                                
                                click = False #set click to false 
                                
                                if abs(l.lane - o[1]) == d2 and double == False: #if the distance between the piece and the lane is equal to the dice roll and the player didnt roll a double
                                    d2 = 0 #reset the dice
                                    
                                elif abs(l.lane - o[1]) == d1 and double == False: #if the distance between the piece and the lane is equal to the dice roll and the player didnt roll a double
                                    d1 = 0 #reset the dice
                                    
                                eval('lane{}'.format(l.lane)).remove_piece(l) #remove the piece from the lane
                                
                                l.move(eval(o[0]), o[1]) #move the piece to the location
                                
                                eval('lane{}'.format(o[1])).add_piece(l) #add the piece to the lane
                                
                                move -= 1 #subtract 1 from the move counter
                                
                                print('Move:', move)
                                
                                if move == 2: #if the move counter is 2
                                    double = False #set double to false
                                    
                                Loc = [] #reset Loc
                                
                                Window.blit(Background, (0, 0))  # Draw the background
                                
                                for i in Breal:  # For loop to draw the black pieces
                                    Window.blit(Black_piece, (i.location.x, i.location.y))  # type: ignore
                                    
                                for i in Rreal:  # For loop to draw the red pieces
                                     Window.blit(Red_piece, (i.location.x, i.location.y))  # type: ignore
                                     
                                draw_dice(d1, d2) # Draw the dice
                                 
                                pygame.display.update() # Update the display
                                
                                Movesequence = True #set Movesequence to true to continue onto next move
                                
                                if move == 0: #if the move counter is 0
                                    
                                    if Player == 'red': #if the player is red
                                        Player = 'black' #set the player to black
                                        
                                    else:
                                        Player = 'red' #set the player to red
                                        
                                    Turn_play = True #set Turn_play to true
                                    
                                    
                                    
            if poc != [] and Movesequence == False: #Move the piece to valid capture move if the player has no pieces in prison (Could be a function)
                
                for o in poc: #for every location in poc
                    
                    if eval(o[0]).x <= mouse[0] <= eval(o[0]).x + 50 and eval(o[0]).y <= mouse[1] <= eval(o[0]).y + 50: #if the player clicks on a location in poc
                        
                        for l in Real_pieces: #for every piece in Real_pieces
                            
                            if l.location.x == PP.location.x and l.location.y == PP.location.y and click == True: #find the piece that the player clicked on
                                
                                click = False #set click to false
                                
                                if abs(l.lane - o[1]) == d2 and double == False: #if the distance between the piece and the lane is equal to the dice roll and the player didnt roll a double
                                    d2 = 0 #reset the dice
                                elif abs(l.lane - o[1]) == d1 and double == False: #if the distance between the piece and the lane is equal to the dice roll and the player didnt roll a double
                                    d1 = 0 #reset the dice
                                    
                                H = eval('lane{}'.format(o[1])).get() #get the piece in the lane
                                
                                if H[0].color == 'red': #if the piece is red
                                    
                                    H[0].move(REDprison, 0) #move the piece to the prison
                                    
                                    eval('lane{}'.format(o[1])).remove_piece(H[0]) #remove the piece from the lane
                                    
                                    prisonR = True #set prisonR to true
                                    
                                    print('Red in prison') 
                                    
                                    RP += 1 #add 1 to the red prison counter
                                    
                                    INPRISON = True #set INPRISON to true
                                    
                                elif H[0].color == 'black': #if the piece is black
                                    
                                    H[0].move(BLACKprison, 0) #move the piece to the prison
                                    
                                    eval('lane{}'.format(o[1])).remove_piece(H[0])  #remove the piece from the lane
                                    
                                    prisonB = True  #set prisonB to true
                                    
                                    print('Black in prison') 
                                    
                                    BP += 1 #add 1 to the black prison counter
                                    
                                    INPRISON = True #set INPRISON to true
                                    
                                eval('lane{}'.format(l.lane)).remove_piece(l) #remove the piece from the lane
                                
                                l.move(eval(o[0]), o[1]) #move the piece to the location
                                
                                eval('lane{}'.format(o[1])).add_piece(l) #add the piece to the lane
                                
                                move -= 1 #subtract 1 from the move counter
                                
                                print('Move:', move)
                                
                                if move == 2: #if the move counter is 2
                                    double = False #set double to false
                                    
                                poc = [] #reset poc
                                
                                Window.blit(Background, (0, 0))  # Draw the background
                                
                                for i in Breal:  # For loop to draw the black pieces
                                    Window.blit(Black_piece, (i.location.x, i.location.y))  # type: ignore
                                    
                                for i in Rreal:  # For loop to draw the red pieces
                                     Window.blit(Red_piece, (i.location.x, i.location.y))  # type: ignore
                                     
                                draw_dice(d1, d2) # Draw the dice
                                
                                pygame.display.update() # Update the display
                                
                                Movesequence = True #set Movesequence to true to continue onto next move
                                 
                                if move == 0: #if the move counter is 0
                                    
                                    if Player == 'red': #if the player is red
                                        Player = 'black' #set the player to black
                                        
                                    else:
                                        Player = 'red' #set the player to red
                                        
                                    Turn_play = True #set Turn_play to true
            
                                    
                                
            # Move sequence DONE (almost)
            # onto extra
            
            
            
            if ((D1.x <= mouse[0] <= D1.x + 20 and D1.y <= mouse[1] <= D1.y + 20) or (D2.x <= mouse[0] <= D2.x + 20 and D2.y <= mouse[1] <= D2.y + 20)) and Turn_play == True: # if the player clicks on the dice
                
                Turn_play = False # set Turn_play to false
                
                print('Dice rolled')    
                
                d1, d2 = roll_dice() # roll the dice
                
                print(d1, d2) # print the dice roll
                
                if d1 == d2: # if the dice roll is a double
                    move = 4 # set the move counter to 4
                    double = True # set double to true
                    
                else:
                    move = 2 # set the move counter to 2
                    
                draw_dice(d1, d2) # Draw the dice                 
        
        
        # win condition
        LL = [] # Temp list for red
        
        for i in Rreal: # for every piece in Rreal
            
            if i.lane in [19, 20, 21, 22, 23, 24, -1]: # if the piece is in the win lane
                LL.append(i.lane) # add the lane to LL
                
        if len(LL) == 15: # if LL has 15 lanes
            winingR = True # set winingR to true
            
            
        
        TT = [] # Temp list for black
        
        for i in Breal: # for every piece in Breal
            
            if i.lane in [1, 2, 3, 4, 5, 6, -1]: # if the piece is in the win lane
                TT.append(i.lane) # add the lane to TT
                
        if len(TT) == 15: # if TT has 15 lanes
            winingB = True # set winingB to true



        # win
        if RW == 15: # if RW is 15
            messagebox.showinfo('Winner', 'Red Wins') # show a message box saying red wins
            pygame.quit() # quit the game
            
        elif BW == 15: # if BW is 15
            messagebox.showinfo('Winner', 'Black Wins') # show a message box saying black wins
            pygame.quit() # quit the game
                

        
        
            
        # lane more then 5
        for i in List_lane: # for every lane in List_lane
            
            jj = i.number # set jj to the lane number
            
            if jj <7: # if jj is less then 7
                Window.blit(number_empty, (35+(60*(jj-1)), 0)) # draw the number empty at specific location
                
            elif jj < 13: # if jj is less then 13
                Window.blit(number_empty, (35+(60*(jj-1))+30, 0)) # draw the number empty at specific location
                
            elif jj < 19: # if jj is less then 19
                Window.blit(number_empty, (35+(60*(jj-13)), 580)) # draw the number empty at specific location
                
            elif jj < 25: # if jj is less then 25
                Window.blit(number_empty, (35+(60*(jj-13))+30, 580)) # draw the number empty at specific location
            
        for i in List_lane: # for every lane in List_lane
            
            if i.length > 5: # if the lane length is more then 5
                
                gg = i.length - 5 # set gg to the lane length - 5
                
                jj = i.number # set jj to the lane number
                
                img = font.render('+{}'.format(gg), True, (255, 255, 255)) # set img to the font render of gg
                
                if jj <7: # if jj is less then 7
                    Window.blit(img, (35+(60*(13-jj)), 5)) # draw the img at specific location
                    
                elif jj < 13: # if jj is less then 13
                    Window.blit(img, (35+(60*(13-jj))+30, 5)) # draw the img at specific location
                    
                elif jj < 19: # if jj is less then 19
                    Window.blit(img, (35+(60*(jj-13)), 580)) # draw the img at specific location
                    
                elif jj < 25: # if jj is less then 25
                    Window.blit(img, (35+(60*(jj-13))+30, 580)) # draw the img at specific location
                    
                    
                    
                    
                    
                    
        # Main loop DONE

        pygame.display.update() # Update the display
            

                
        
        
    #For Debugging
    print('Player: ', Player)
    print('Turn_play: ', Turn_play)
    print('Movesequence: ', Movesequence)
    print('move: ', move)
    print('Loc: ', Loc)
    print('poc: ', poc)
    print('ppc: ', ppc)
    print('RP: ', RP)
    print('BP: ', BP)
    print('double: ', double)
    print('click: ', click)
    print('prisonR: ', prisonR)
    print('prisonB: ', prisonB)
    print('INPRISON: ', INPRISON)
    print('Prison_play: ', Prison_play)
    print('winingR: ', winingR)
    print('winingB: ', winingB)
    print('RW: ', RW)
    print('BW: ', BW)
    pygame.quit()  # Quit the game


# If the file that is being run is the main file (prevents the file from running if it is imported)
if __name__ == "__main__":
    main()  # Run the main function
