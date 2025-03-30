def treasure_hunt():
    user_input = input("Please choose between left and right:")
    if user_input.lower()=="left":
        print("Correct Choice!")
        wait_or_swim = input("Do you want to wait or swim")
        if wait_or_swim.lower() == "wait":
            print("Correct Choice!")
            door = input("do you want to choose the red door, the blue door, or the yellow door")
            # if door.lower() == "yellow":
            #     print("Correct Choice You Win!")
            #     return
            # elif door.lower() =="red":
            #     print("You get Burned by a Fire, Game Over")
            #     return
            # elif door.lower() == "blue":
            #     print("You get Eaten by a Beast, Game Over")
            #     return
            # else:
            #     print("Game Over")
            #     return
            match door.lower():
                case "yellow":
                    print("Correct You Win!")
                    return
                case "red":
                    print("You get Burned by a Fire, Game Over")
                    return
                case "blue":
                    print("You get Eaten by a Beast, Game Over")
                    return
                case _:
                    print("Game Over")
        else :
            print("You get attacked by a trout, Game over")
            return
    else:
        print("You fall into a hole, Game over")
        return
