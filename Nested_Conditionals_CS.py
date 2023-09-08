age = input("How old are you? ")
if age:
    age = int(age)
    if int(age) >= 18 and int(age) <21:
        print("You either, but need a wristband!")
        # 18-21 wristband
    elif int(age) >= 21:
        print("You are good to enter and can drink!")
        #21+ drink, normal entry
    else: 
        # too young, sorry
        print("You can't come in little one")

else:
    print("please enter an age")
