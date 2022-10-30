import turtle
import pandas

data_file = pandas.read_csv(r'Depth_python\C_States_Game\50_states.csv')
state_list = data_file['state'].tolist()
total_state = len(state_list)

screen = turtle.Screen()
screen.setup(740, 500)
screen.title("U.S. States Game")
image_background = r"Depth_python\C_States_Game\blank_states_img.gif"
screen.addshape(image_background)
bg = turtle.shape(image_background)
text_turtle = turtle.Turtle()
correct_guesses = []
count = 0
score = 0


def get_location(x, y, text):
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.setposition(x, y)
    text_turtle.write(text)
    text_turtle.pendown()


def check_answer():
    global answer_state, count, score
    for index, state in enumerate(state_list):
        if answer_state == state:
            score += 5
            count += 1
            correct_guesses.append(answer_state)
            result_x = data_file[data_file.state ==
                                 answer_state]['x'].values[0]
            result_y = data_file[data_file.state ==
                                 answer_state]['y'].values[0]
            get_location(int(result_x), int(result_y), answer_state)


while len(correct_guesses) < total_state:
    answer_state = screen.textinput(
        title=f"Guess the states {count}/{total_state} ", prompt="What\'s the another state\'s name?").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in state_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r'Depth_python\C_States_Game\missing_states.csv')
        break
    check_answer()
    print(correct_guesses)

# getting coordinates from mouse pos
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
