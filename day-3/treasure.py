direction = input("choose 'R' or 'L'? ").lower()

if direction == 'l':
    wait_go = input("print 'wait' or 'go' ").lower()
    if wait_go == 'wait':
        color = input("print 'red' or 'yellow' or 'blue' ").lower()
        if color == 'red' or color == 'blue':
            print("game over")
        elif color == 'yellow':
            print("you win")
        else:
            print("you should to choose one of these colors, try again")
    else:
        print("game over")
else:
    print("game over")
