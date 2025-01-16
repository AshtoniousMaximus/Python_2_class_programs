import tkinter as tk
from utilities import path
from tkinter import *

# creates a tkinter window
window = tk.Tk()

# creates the frames for the gif animation
frames = [
    # takes the file path of the gif and gives an index within the PhotoImage
    PhotoImage(file=path("C:\\Users\\green\\Documents\\python_programs\\thing.gif"), format="gif -index %i" % (i))
    # runs through the 60 frames of the image, making the animation work
    for i in range(60)
]

# taken and modified from stackexchange
# creates a function called update
def update(ind):
    """ 
    This function uses an if statement that runs in an odd recursive loop to continuously update the framerate. 
    It does this by increasing the frame value and the if statement resets the value if it is over 59, causing it to start over again.
    """

    # sets the frame to be at the frame at ind
    frame = frames[ind]
    # adds 1 to the value ind
    ind += 1
    # With this condition it will play gif infinitely
    # if the framerate is greater than 59, the frame is set back to 0
    if ind > 59:
        ind = 0
        # configures the image for the current frame
    label.configure(image=frame)
    # after the duration of update speed, the frame changes
    window.after(update_speed, update, ind)

# sets the variable update speed equal to 1
update_speed = 1

# creates a function increase_speed to increase the animation speed
def increase_speed():
    """
    This function takes the global variable update_speed and subtracts two from its value, unless the value is 1 in which case the function limits itself from subtracting more
    
    """
    # accesses the global variable update speed for use in the function
    global update_speed
    # sets the update_speed 2 units lower, limiting the lowest value to 1
    update_speed = max(1, update_speed -2)

# creates a function decrease_speed to decrease the animation speed
def decrease_speed():
    """
    This function takes the global variable update_speed and adds two to its value, unless the value is 100 in which case the function limits itself from adding more
    
    """
    # accesses the global variable update_speed
    global update_speed
    # increases the delay between frames by 2, limiting the max delay to 100
    update_speed = min(100, update_speed +2)

# creates a function set_rpm that sets the delay between frames
def set_delay():
    """gets the input of the text box and takes the global update_speed
    as long as the speed is an integer and between 1 and 100, the frame update speed is set as the input value.
    
    """
    # sets the variable speed as the text entry from the user
    speed = speed_entry.get()
    # accesses the global value update_speed 
    global update_speed
    # checks if the user input is a digit 
    if speed.isdigit():
        # turns the input into an integer value
        speed = int(speed_entry.get())
        # checks if the there is an and if the input value is between 1 and 100
        if update_speed and speed >= 1 and speed <= 100:
            # sets the update speed to the entered value
            update_speed = speed
            # sets the output text to be a blank line
            error_label.configure(text='')
        #  otherwise an instruction message is given
        else:
            # sets display_text equal to the instructions
            display_text = f'please enter an integer between 1 and 100'
            # sets the error_label to be displayed
            error_label.configure(text=display_text)
    # otherwise, again an instruction message is given
    else:
        # sets the displayed text to the instructions
        display_text = f'please enter an integer between 1 and 100'
        # sets the error_label to be displayed
        error_label.configure(text=display_text)

#aliases the word label with the Label function in tkinter
label = Label(window)
# packs the label function
label.pack()
# sets the title of the window
window.title("engine animation")
# sets the window update delay which in this case is 0
window.after(0, update, 0)

# creates and displays a button titled increase speed that activates the increase_speed function when called upon
fast_button = tk.Button(window, text='increase speed', command = increase_speed)
fast_button.pack()

# creates and displays a button titled decrease speed that activates the decrease_speed function when called upon
slow_button = tk.Button(window, text='decrease speed', command = decrease_speed)
slow_button.pack()

# creates a text entry box with width 20
speed_entry = tk.Entry(window, text='set speed', width=20)
speed_entry.pack()

# creates a button titled "press here to set the framerate" that activates the set_delay function when called upon
set_speed = tk.Button(window, text="press here to set the framerate", command = set_delay)
set_speed.pack()

# creates a label for an error message
error_label = tk.Label(window)
# packs the message
error_label.pack()

# makes the window loop through so it runs continuously
window.mainloop()