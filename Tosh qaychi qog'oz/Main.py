import random
rockimg="""
    __
---'   )
      ()
      ()
      ()
---.()
"""
paperimg="""
    __
---'   )
          __)
          __)
         __)
---.__)
"""
scissorsimg="""
    __
---'   )
          __)
       __)
      (__)
---.(___)
"""

# ======================================
# ======================================
# Ascii
# ======================================
# ======================================
print("""
███████ ████████  █████  ██████  ████████      ██████   █████  ███    ███ ███████ 
██         ██    ██   ██ ██   ██    ██        ██       ██   ██ ████  ████ ██      
███████    ██    ███████ ██████     ██        ██   ███ ███████ ██ ████ ██ █████   
     ██    ██    ██   ██ ██   ██    ██        ██    ██ ██   ██ ██  ██  ██ ██      
███████    ██    ██   ██ ██   ██    ██         ██████  ██   ██ ██      ██ ███████                                                               
""")
def ComputerWins():
    print("""
 ██████  ██████  ███    ███ ██████  ██    ██ ████████ ███████ ██████      ██     ██ ██ ███    ██ ███████ 
██      ██    ██ ████  ████ ██   ██ ██    ██    ██    ██      ██   ██     ██     ██ ██ ████   ██ ██      
██      ██    ██ ██ ████ ██ ██████  ██    ██    ██    █████   ██████      ██  █  ██ ██ ██ ██  ██ ███████ 
██      ██    ██ ██  ██  ██ ██      ██    ██    ██    ██      ██   ██     ██ ███ ██ ██ ██  ██ ██      ██ 
 ██████  ██████  ██      ██ ██       ██████     ██    ███████ ██   ██      ███ ███  ██ ██   ████ ███████ 
    """)
def YouWin():
    print("""    
██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██ 
   ██     ██████   ██████       ███ ███  ██ ██   ████ 
""")
def Draw():
    print("""
██████  ██████   █████  ██     ██ 
██   ██ ██   ██ ██   ██ ██     ██ 
██   ██ ██████  ███████ ██  █  ██ 
██   ██ ██   ██ ██   ██ ██ ███ ██ 
██████  ██   ██ ██   ██  ███ ███                         
""")

# ======================================
# ======================================
#Main codes
# ======================================
# ======================================
print(f"{rockimg}Rock")
print(f"{paperimg}Peper")
print(f"{scissorsimg}Scissorsimg\n\n\n\n\n")

UserChoise = input("Your choise (rock , paper , scissors) :").lower()
array = ["rock","paper","scissors"]
RandomComp = random.choice(array)

if UserChoise == "rock" or UserChoise == "paper" or UserChoise == "scissors":
    if UserChoise == "rock" and RandomComp == "scissors":
        YouWin()
        print(f"You choise {UserChoise} Compyuter choise {RandomComp}")
        print(f"You choise {rockimg} Compyuter choise {scissorsimg}")
    elif UserChoise == "scissors" and RandomComp == "paper":
        YouWin()
        print(f"You choise {UserChoise} Compyuter choise {RandomComp}")
        print(f"You choise {scissorsimg} Compyuter choise {paperimg}")
    elif UserChoise == "paper" and RandomComp == "rock":
        YouWin()
        print(f"You choise {UserChoise} Compyuter choise {RandomComp}")
        print(f"You choise {paperimg} Compyuter choise {rockimg}")
    elif UserChoise == RandomComp:
        Draw()
        print(f"You choise {UserChoise}. Compyuter choise {RandomComp}")
        if UserChoise == "rock" or RandomComp == "rock":
            print(f"You choise {rockimg} Compyuter choise {rockimg}")
        elif UserChoise == "paper" or RandomComp == "paper":
            print(f"You choise {paperimg} Compyuter choise {paperimg}")
        else:
            print(f"You choise {scissorsimg} Compyuter choise {scissorsimg}")
    else:
        print(ComputerWins())
        print(f"You choise {UserChoise}. Compyuter choise {RandomComp}")
        if UserChoise == "rock" or RandomComp == "paper":
            print(f"You choise {rockimg} Compyuter choise {paperimg}")
        elif UserChoise == "paper" or RandomComp == "scissors":
            print(f"You choise {paperimg} Compyuter choise {scissorsimg}")
        else:
            print(f"You choise {scissorsimg} Compyuter choise {rockimg}")
else:
    print("To'g'ri yoz")