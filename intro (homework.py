def hobby():
    hobby = input("What do you like to do in your free time?")

    if hobby == "sports":
        print("Oh! that's nice!")
        if feeling == "bad" or feeling == "not good":
            sportbad = input("Does your bad day have to do with sports?").lower()
            if sportbad == "yes":
                print("Oh I'm sorry to hear that!")
            else:
                print("Oh, nevermind!")
        elif feeling == "good" or feeling == "well":
            sportgood = input("Did something good happen that made your day?")
            if sportgood == "yes":
                sportgood2 = input("Oh, what happened?")
                print("That's nice!")
            else:
                sportgood3 = input("What happened?")
                print("Cool!")

    elif hobby == "watching tv":
        tv1 = input("Oh, what do you like to watch?")
        print("That's nice! I like watching that too!")
        if feeling == "good" or feeling == "well":
            tv2 = input("Does this have to do with your good day? Did you get any sort of achievement?")
            if tv2 == "yes":
                print("That's nice to hear!")
                tv205 = input("What happened?")
                print("That's nice!")
            elif tv2 == "no":
                tv205 = input("Oh, sorry for the misunderstanding!")
                print("Oh, I see!")
        else:
            tv3 = input("Oh! Did you lose in the game?")
            if tv3 == "yes":
                print("I'm so sorry! I hope you feel better!")
            elif tv3 == "no":
                print("Oh ok, maybe it's something else")

    elif hobby == "playing video games":
        vg1 = input("What game do you play?")
        if vg1 == "Minecraft":
            print("Oh, I love that game, too!")
        else:
            print(f"{vg1} sounds fun!")

        if feeling == "good" or feeling == "well":
            vg2 = input("Did something in the game make you happy?")
            if vg2 == "yes":
                vg3 = input("What happened?")
                print("Nice!")
            else:
                print("Ok cool!")
        elif feeling == "bad" or feeling == "not good":
            vg4 = input("Did something go wrong in the game?")
            if vg4 == "yes":
                print("Oh no! I hope it goes better next time!")
            else:
                print("Maybe something else made your day bad")

    else:
        print("That sounds like a cool hobby!")


print("Hi! I'm AI guy.")
name = input("What's your name? ").strip()
print(f"Hi, {name}! Nice to meet you.")

feeling = input(f"How was your day today, {name}? ").strip().lower()

if feeling == "good" or feeling == "well":
    print("That's nice!")
elif feeling == "bad" or feeling == "not good":
    print("Oh no! I'm sorry to hear that!")
else:
    print("That's okay.")

hobby()

favorite_food = input(f"By the way, {name}, what's your favorite food? ")
print(f"Yum! I like {favorite_food} too.")

print(f"Thanks for chatting, {name}! Have a great day!")
