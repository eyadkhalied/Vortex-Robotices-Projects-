import pgzrun
import random

WIDTH = 1170
HEIGHT = 720
TITLE = "THE MILLIONAIRES"

gameStarted = False
timeleft = 15
score = 0

main_box = Rect(50, 40, 880, 240)
answer_boxes = [
    Rect(50, 358, 440, 165),
    Rect(520, 358, 440, 165),
    Rect(50, 538, 440, 165),
    Rect(520, 538, 440, 165),
]

prize_box = Rect(990, 680, 240, 30)
prizes = [
    "0$",
    "1,000$",
    "2,000$",
    "6,000$",
    "16,000$",
    "32,000$",
    "64,000$",
    "125,000$",
    "250,000$",
    "500,000$",
    "1,000,000$",
]
questions = [
    "What is the capital of France?,London,Paris,Berlin,Tokyo,1",
    "What is 5+7?,12,10,14,8,0",
    "What is the seventh month of the year?,April,May,June,July,3",
    "Which planet is closest to the Sun?,Saturn,Neptune,Mercury,Venus,2",
    "Where are the pyramids?,India,Egypt,Morocco,Canada,1",
    "What is the largest desert in the world?,Sahara Desert,Gobi Desert,Mojave Desert,Arabian Desert,0",
    "What is the currency of South Africa?,Euro,Dollar,Rand,Pound,2",
    "What is the largest country in South America?,Brazil,Argentina,Chile,Colombia,0",
    "What is the largest lake in Africa?,Lake Victoria,Lake Tanganyika,Lake Malawi,Lake Chad,0",
    "What is the capital of Spain?,Madrid,Barcelona,Valencia,Seville,0",
    "What is the official language of the Netherlands?,Dutch,English,French,German,0",
    "What is the largest island in the world?,Greenland,Madagascar,Borneo,Sumatra,0",
    "What is the currency of India?,Euro,Dollar,Rupee,Pound,2",
    "What is the capital of Mexico?,Mexico City,Cancun,Guadalajara,Monterrey,0",
    "What is the smallest country in the world by land area?,Monaco,Vatican City,San Marino,Liechtenstein,1",
    "What is the largest river in South America?,Amazon River,Orinoco River,Parana River,Rio Grande,0",
    "What is the currency of Canada?,Euro,Dollar,Canadian Dollar,Pound,2",
    "What is the capital of Russia?,Moscow,St. Petersburg,Novosibirsk,Yekaterinburg,0",
    "What is the largest country in Europe?,Russia,Germany,France,Spain,0",
    "What is the smallest planet in our solar system?,Mars,Earth,Pluto,Mercury,3",
    "Which planet is famous for its rings?,Jupiter,Saturn,Uranus,Mars,1",
    "What is the world's largest ocean?,Atlantic Ocean,Pacific Ocean,Indian Ocean,Arctic Ocean,1",
    "What is the currency of Japan?,Yen,Euro,Dollar,Pound,0",
    "Who created the theory of relativity?,Albert Einstein,Isaac Newton,Galileo Galilei,Stephen Hawking,0",
    "What is the largest mammal in the world?,Blue Whale,Elephant,Rhinoceros,Giraffe,0",
    "Who painted the Mona Lisa?,Michelangelo,Leonardo da Vinci,Vincent van Gogh,Pablo Picasso,1",
    "What is the tallest mountain in the world?,Mount Everest,Mount Kilimanjaro,Mount Fuji,Mount McKinley,0",
    "Which city is known as the Big Apple?,Los Angeles,Chicago,New York City,Houston,2",
    "What is the largest country in the world?,China,India,Russia,Brazil,2",
    "What is the official language of Brazil?,Spanish,Portuguese,French,Italian,1",
    "What is the currency of Germany?,Euro,Dollar,Yen,Pound,0",
    "Which country is home to the Great Pyramid of Giza?,Egypt,Sudan,Ethiopia,Kenya,0",
    "What is the smallest continent in the world?,Asia,Europe,Africa,Australia,3",
    "What is the capital of Canada?,Ottawa,Toronto,Vancouver,Montreal,0",
    "Which country gifted the Statue of Liberty to the United States?,France,Spain,Italy,Germany,0",
    "Who invented the telephone?,Alexander Graham Bell,Thomas Edison,Nikola Tesla,Benjamin Franklin,0",
    "What is the currency of Mexico?,Peso,Euro,Yen,Pound,0",
    "What is the capital of Australia?,Sydney,Melbourne,Brisbane,Canberra,3",
    "What is the value of x in the equation 3x - 7 = 8?,5,7,9,11,0",
    "What is the value of y in the equation 2y + 4 = 14?,5,6,7,8,0",
    "What is the value of k in the equation 2k/3 = 8?,9,12,16,24,1",
    "What is the value of m in the equation 5m/2 = 25?,5,10,15,20,1",
    "What is the value of o in the equation 3o/5 = 9?,12,15,18,21,1",
    "What is the value of s in the equation 2s/3 = 12?,18,20,22,24,0",
    "What is the value of u in the equation 3u/4 = 21?,24,28,32,36,1",
    "What is the value of w in the equation 2w - 7 = 11?,9,10,11,12,0",
    "What is the value of pi to two decimal places?,3.14,3.16,3.18,3.20,0",
    "What is the value of x in the equation 2x + 5 = 13?,2,3,4,5,2",
    "What is the sum of angles in a triangle?,90 degrees,180 degrees,270 degrees,360 degrees,1",
    "What is the area of a rectangle with length 5cm and width 8cm?,13 cm^2,30 cm^2,40 cm^2,45 cm^2,2",
    "What is the value of y in the equation 4y - 8 = 20?,3,4,5,7,3",
    "What is the perimeter of a square with side length 3cm?,6 cm,9 cm,12 cm,15 cm,2",
    "What is the value of z in the equation 5z + 10 = 30?,4,5,6,7,0",
    "What is the volume of a cube with side length 4cm?,8 cm^3,16 cm^3,32 cm^3,64 cm^3,3"
]


# with open("questions.txt") as file:
#     questions = file.readlines()

for index, line in enumerate(questions):
    questions[index] = line.strip().split(",")

currentQuestion = random.choice(questions)
questions.remove(currentQuestion)


def draw():
    screen.clear()
    screen.blit("background", pos=(0, 0))

    if gameStarted:
        screen.draw.filled_rect(main_box, "steel blue")
        screen.draw.textbox(currentQuestion[0], main_box, color="white")

        screen.draw.filled_circle((1110, 150), 125, "golden rod")
        screen.draw.text(str(timeleft), center=(1110, 160), fontsize=250, color="black")

        for index, box in enumerate(answer_boxes):
            screen.draw.filled_rect(box, "midnight blue")
            screen.draw.textbox(currentQuestion[index + 1], box, color="white")

        screen.draw.filled_rect(prize_box, "orange")

        for counter, prize in enumerate(prizes):
            screen.draw.text(
                prize,
                center=(1110, 695 - 40 * counter),
                fontsize=50,
                color="white",
            )
    else:
        screen.draw.text(
            "START?", center=(WIDTH / 2, HEIGHT / 2), fontsize=250, color="blue"
        )


def updateTime():
    global timeleft, gameStarted
    if gameStarted and timeleft > 0:
        timeleft -= 1
    if timeleft == 0:
        print("Game_Over")


clock.schedule_interval(updateTime, 1.0)


def on_mouse_down(pos):
    global gameStarted, currentQuestion, timeleft
    if not gameStarted:
        gameStarted = True
    else:
        for index, box in enumerate(answer_boxes):
            if box.collidepoint(pos):
                if index == int(currentQuestion[5]):
                    correct_answer()
                else:
                    game_over()


def correct_answer():
    global currentQuestion, timeleft, score, questions
    score += 1
    prize_box.move_ip(0, -40)

    if score < 10 and questions:
        currentQuestion = random.choice(questions)
        questions.remove(currentQuestion)
        timeleft = 10
    else:
        game_over()


def game_over():
    global currentQuestion, timeleft
    message = "YOU WIN " + prizes[score]
    currentQuestion = [message, "-", "-", "-", "-", "5"]
    timeleft = 0
    clock.unschedule(updateTime)


def update():
    pass


pgzrun.go()
