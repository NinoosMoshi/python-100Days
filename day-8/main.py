import math


def paint_calc(height, width, cover):
    number_of_cans = height * width / cover
    numCans_roundUp = math.ceil(number_of_cans)  # math.ceil() -> roundUP
    print(f"You'll need {numCans_roundUp} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
