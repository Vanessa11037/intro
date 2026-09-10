print("vad heter du?")

name = input()

print(f"Hej {name}.")

run = True

while run :

    print("Hur gammal är du?")
    age = int(input())
    if age < 0 and age > 120 :
        if age < 18 :
            print(f"du har {18 - age} år kvar tills du är myndig")
            run = False
        elif age > 64 :
            print ("Du är en glad pensionär. Grattis!")
            run = False
        else :
            print("Nämen dåså, du är myndig och inte pensionär(Antagligen)")
            run = False
    else :
        print("Vänligen uppge en korrekt ålder")

print ("Hejdå!")