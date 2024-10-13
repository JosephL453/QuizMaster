import random
import pgzrun

TITLE = "QuizMaster"
WIDTH = 870
HEIGHT = 650

marquee_Box = Rect(0, 0, 880, 80)
question_Box = Rect(0, 0, 650, 150)
timer_Box = Rect(0,0,150,150)
answer_Box1 = Rect(0, 0, 300, 150)
answer_Box2 = Rect(0, 0, 300, 150)
answer_Box3 = Rect(0, 0, 300, 150)
answer_Box4 = Rect(0, 0, 300, 150)
skip_Box = Rect(0, 0, 150, 330)

score = 0
time_Left = 10
question_file = "questions.txt"
marquee_Text = " "
is_Game_Over = False

answer_Boxes = [answer_Box1, answer_Box2, answer_Box3, answer_Box4]

questions = []
question_Count = 0
question_Index = 0

marquee_Box.move_ip(0,0)
question_Box.move_ip(20,100)
timer_Box.move_ip(700,100)
answer_Box1.move_ip(20,270)
answer_Box2.move_ip(370,270)
answer_Box3.move_ip(20,450)
answer_Box4.move_ip(370,450)
skip_Box.move_ip(700,270)


def draw():
    global marquee_Text, question_Index, question_Count
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_Box, "black")
    screen.draw.filled_rect(question_Box, "navy blue")
    screen.draw.filled_rect(timer_Box, "navy blue")
    screen.draw.filled_rect(skip_Box, "dark green")

    for i in answer_Boxes:
        screen.draw.filled_rect(i, "orange")
    
    marquee_Text = "WELCOME TO QUIZ MASTER"
    marquee_Text = marquee_Text + f"Q:{question_Index}of{question_Count}"

    screen.draw.textbox( marquee_Text, marquee_Box, color="white")
    screen.draw.textbox( str(time_Left), timer_Box, color="white")
    screen.draw.textbox( "skip", skip_Box, color="black")
    screen.draw.textbox( quest[0], question_Box, color="white")

def read_question_file():
    global question_Count, questions, question_file
    q_file = open(question_file, "r")
    for i in q_file:
        questions.append(i)
        question_Count += 1
    q_file.close()

def read_next_question():
    global question_Index
    question_Index += 1
    return questions.pop(0).split(",")
    

read_question_file()
quest = read_next_question(0)
print(quest)
pgzrun.go()