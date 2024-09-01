import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
#to add a image as a turtle shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

#create pop up box
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
answer = answer_state.title()

#reading the csv file
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_guesses = []

#checking the answer
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name? (Type 'exit' to quit)").title()
    if answer_state.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'

    if answer_state in state_list and answer_state not in correct_guesses:
        state_info = data[data["state"] == answer_state]
        x_coordinate = int(state_info["x"])
        y_coordinate = int(state_info["y"])

        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(x_coordinate, y_coordinate)
        state_turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))

        correct_guesses.append(answer_state)
        score += 1
    else:
        missing_states.append(answer_state)

# Find the missing states
missing_states = [state for state in state_list if state not in correct_guesses]

turtle.bye()  # Close the turtle graphics window

# Save missing states to a CSV file
missing_states_df = pandas.DataFrame({'Missing States': missing_states})
missing_states_df.to_csv('missing_states.csv', index=False)
turtle.mainloop()