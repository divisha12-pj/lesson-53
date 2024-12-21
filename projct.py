import random
while(1<2):
    print('\n')
    print("rock,paper,scissors-shoot")
    choice=input("choose your weapon[r]ock,[p]aper,[s]cissor")
    print("[r]ock,[p]aper,[s]cissor.")
    print("you chose: " + choice)
    choices=["r","p","s"]
    opponentchoice=random.choice(choices)
    print( "I choose" + opponentchoice)
    if opponentchoice==str.upper(choice):
        print('tie')
    elif opponentchoice=="r"and choice.upper()=="s":
      print("sciisor baet rock")
      continue
    elif opponentchoice=="s"and choice.upper()=="p":
      print("sciisor beat paper")
      continue
    elif opponentchoice=="p"and choice.upper()=="r":
      print("paper beats rock")
      continue
    else:
       print("you win")