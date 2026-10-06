word_1 = input("What is the first word that you want to use?\n>")
word_2 = input("What is the second word that you want to use?\n>")
word_3 = input("What is the third word that you want to use?\n>")

print(word_1, word_2, word_3)
#question 1 done (15 points)

number_1 = input(" Give me a number to use that is an integer\n>")
number_2 = input ("give me another number to use that is an integer\n>")
number_3 = input("give me a third number to use that is an integer\n>")
def add_three ( number_1 , number_2 , number_3):
    return int(number_1) + int(number_2) + int(number_3)

result = add_three(number_1, number_2, number_3)
print(result)
#question 2 done (7 points)


def data_three():
    word = input("Enter a word:\n>")
    integer_value = int(input("Enter an integer:\n>"))
    float_value = float(input("Enter a float:\n>"))
    total = integer_value + float_value
    print(word + str(total))

data_three()

#question 3 done (3 points)