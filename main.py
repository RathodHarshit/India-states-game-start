import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
image = "India-locator-map-blank.jpeg.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("india_state_co-ordinate.csv")
all_states = data.states.to_list()
guessed_states = []

while len(guessed_states) < 28:
    guess_answer = screen.textinput(title="Guess the State", prompt="Whats another State name").title()

    if guess_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if guess_answer in all_states:
        guessed_states.append(guess_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == guess_answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(guess_answer)

    #if guess ans is correct from all the states file


screen.exitonclick()

