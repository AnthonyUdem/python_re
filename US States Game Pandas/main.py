import turtle
import pandas

screen = turtle.Screen()
screen.title("Lonasctech U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
track_List = []  # Todo-5 record the correct guesses in alist
us_states = pandas.read_csv("50_states.csv")
while len(track_List) < 50:  # Todo-4 use a loop to allow the user to keep guessing
    user_guess = screen.textinput(title=f"{len(track_List)}/50 States Correct", prompt="what's another state's name?").title()  # Todo-1/6 convert to title case
    if user_guess == "Exit":
        break
    if user_guess in track_List:
        print(f"{user_guess} is already on the map")
    else:
        us_states_list = us_states.state.to_list()
        if user_guess in us_states_list:  # Todo-2 check if te guess is among the 50 states
            track_List.append(user_guess)
            state_name = us_states[us_states.state == user_guess]
            state_x_cor = int(state_name.x)
            state_y_cor = int(state_name.y)
            state_coordinate = (state_x_cor, state_y_cor)
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state.goto(state_coordinate)
            state.write(f"{state_name.state.item()}", font=("Courier", 12, "bold"), align="center")  # Todo-3 write correct guesses onto the map

states_to_learn = [state for state in us_states.state if state not in track_List]
states_to_learn_frame = pandas.DataFrame(states_to_learn)
states_to_learn_frame.to_csv("states to learn.csv")

# turtle.mainloop()
