print("Var redo för en HISTORIA!!!!")
hero_name = input("Vem ska denna historia handla om? ")
hero_age = int(input("Hur gammal är hen "))
print("Detta är storyn om hur", hero_name, "blev en hjälte")
print("Hen var", hero_age, "år gammal")
print("Nu var", hero_name, "påväg till vapen affären när hen såg en park. De var några barn som lekte tills en man åkte ditt med sin vita skåpbil, ska", hero_name, "1:kolla vad som pågår eller 2:gå till vapen affären?")

def oneWay(x):
   print(f"Detta är väg 1, med valet: {x}")


def anotherWay(x):
   if x == "ja" or x == "Ja":
      print(f"{x}, du känner igen kidnapparna. Berätta det för polisen!")
   elif x == "nej":
      print(f"Trist för dig.")
   else:
      print("")

choice = int(input("(Svara 1 eller 2):"))
if (choice == 1):
   print("Du valde att gå till parken!!")
elif (choice == 2):
   print()
   print("Barnen blev kidnappade, du valde att ignorera barnen som var i en farlig situation, gör om och gör rätt.")
   print()
   print()
   print("Ending 1: Kidnappning")
   print()
   print()
   oneWay(choice)
else:
   print()
   print("Du skulle ha valt 1 eller 2, eftersom du inte valde att göra något så blev barnen kidnappade, gör om och gör rätt")
   print()
   print()
   print("Ending 1: Kidnappning")
   input = input("Känner du igen kidnapparna (ja/nej)?")
   print()
   anotherWay(input)

# import random
##print(random.randrange(1,20))
