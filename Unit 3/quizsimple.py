print("This quiz is about the Clone Commanders during the Clone wars there will be 10 questions")
answer_1 = "Fox"
answer_2 = "Cody"
answer_3 = "Rex"
answer_4 = "Colt"
answer_5 = "Wolfee"
answer_6 = "Bacara"
answer_7 = "Thorn"
answer_8 = "Neyo"
answer_9 = "Doom"
answer_10 = "Gree"
question_1 = input("Who is the Commander of the Coruscaunt Guard?\n>")
question_2 = input("Who is the Commander of the 212th?\n>")
question_3 = input("Who is the Commander of the 501st?\n>")
question_4 = input("Who is the Commander of the ARC Company?\n>")
question_5 = input("Who is the Commander of the 104th?\n>")
question_6 = input("Who is the Commander of the 21st?\n>")
question_7 = input("Who is the Commander who yelled FOR THE REPUBLIC while saving Senator Amidala?\n>")
question_8 = input("Who is the Commander of the 91st?\n>")
question_9 = input("Who is the Commander of the 41st?\n>")
question_10 = input("Who is the Senior Commander of the 41st?\n>")
global score
score = 0
def tally_score():
    global score
    score = 0
    if question_1 == answer_1:
        score += 1
    if question_2 == answer_2:
        score += 1
    if question_3 == answer_3:
        score += 1
    if question_4 == answer_4:
        score += 1
    if question_5 == answer_5:
        score += 1
    if question_6 == answer_6:
        score += 1
    if question_7 == answer_7:
        score += 1
    if question_8 == answer_8:
        score += 1
    if question_9 == answer_9:
        score += 1
    if question_10 == answer_10:
        score += 1
print(f"Your final score is: {score}/10")