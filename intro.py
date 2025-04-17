name=input("Hi! I'm your personal AI assistant! What is your name?")

print(f"Hi, {name}! it's nice to meet you.")

feeling=input(f"Ok, {name}, how was your day today?")

if feeling=="good" or feeling=="well":
    print("That's nice!")
elif feeling== "bad" or feeling=="not good":
    print("Oh no! Im sorry to hear that!")
else:
    print("That's fine.")

print(f"Thank you {name}! I hope you have a good day!")