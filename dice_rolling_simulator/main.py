import tkinter
from PIL import Image,ImageTk
import random

# top level widget which represents the main window of an application 
root = tkinter.Tk()
root.geometry('400x400')
root.title('Roll the Dice simulator')


# Adding label into the Frame 
BlankLine = tkinter.Label(root,text='')
BlankLine.pack()

# adding label with different font and formatting 
HeadingLabel = tkinter.Label(root,text= 'Rolling dice',fg='light green',bg='dark green',font='Helvetica 16 bold italic')
HeadingLabel.pack()

# image 
dice = ['/home/aakash/Desktop/python projects 1/dice_rolling_simulator/die1.PNG','/home/aakash/Desktop/python projects 1/dice_rolling_simulator/die2.PNG','/home/aakash/Desktop/python projects 1/dice_rolling_simulator/die3.PNG','/home/aakash/Desktop/python projects 1/dice_rolling_simulator/die4.PNG','/home/aakash/Desktop/python projects 1/dice_rolling_simulator/die5.PNG','/home/aakash/Desktop/python projects 1/dice_rolling_simulator/die6.PNG']

#simulating the dice with random numbers between 0-6 ...
diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#constuct a label width for image
imgLabel = tkinter.Label(root,image=diceImage)
imgLabel.image = diceImage
# packing a widget in the parent widget 
imgLabel.pack(expand=True)

# function activated by button 
def rolling_dice():
    diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image 
    imgLabel.configure(image=diceImage)
    # keep a reference 
    imgLabel.image = diceImage

#adding button and command will use rolling_dice function..
button = tkinter.Button(root,text='Roll the dice',fg='blue',command=rolling_dice)

# pack a widget in the parent widget 
button.pack(expand=True)





root.mainloop()