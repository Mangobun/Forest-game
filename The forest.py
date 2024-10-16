import random

#Starting user
userHealth = 100
userDamagePrim = 20
userDamageSecond = 35
userSpeed = 20 

skillPoints = 3

#Starting monster
monstHealth = random.randint(50,150)
monstSpeed = random.randint(10,30)

if monstHealth < 90 :
    monstType = 'Common'
    monstDamage = random.randint(10,30)
elif monstHealth >= 90 < 120 :
    monstType = 'Rare'
    monstDamage = random.randint(25,50)
elif monstHealth >= 120 :
    monstType = 'Unique'
    monstDamage = random.randint(40,70)

#point variables
strengthPoints = 0
speedPoints = 0
healthPoints = 0
skillPoints = 3

#skill menu
def skill ():
    global skillPoints, strengthPoints, healthPoints, speedPoints, userDamagePrim, userHealth, userSpeed
    skillContinue = input("\nUse skill points? (Y/N) ")
    
    while skillContinue == 'y' or skillContinue == 'Y' :
              
            print("\nPoints available: %d" %(skillPoints))
            skillSelect = input("A) Strength = %d\nB) Speed = %d\nC) Health = %d\nSelect your skill type: "%(strengthPoints, speedPoints, healthPoints))
        
           
            if skillSelect == 'A' or skillSelect == 'a':
                print("STRENGTH\nDamage: %d\nPoints used: %d" %(userDamagePrim, strengthPoints))
                skillUseStrength = int(input("Type how many points you'd like to spend(+)/refund(-) on 'STRENGTH': "))
                if skillUseStrength > skillPoints:
                    while skillUseStrength > skillPoints:
                        skillUseStrength = int(input("Sorry you dont have that many points. Try again: "))
                else:
                    skillPoints -= skillUseStrength
                    strengthPoints += skillUseStrength
                    userDamagePrim += ((15)*skillUseStrength)

                print("Strength Points used: %d\nDamage: %d" %(strengthPoints, userDamagePrim))
                skillContinue = input("Continue?(Y/N) ")

            if skillSelect == 'B' or skillSelect == 'b':
                print("SPEED\nSpeed: %d\nPoints used: %d" %(userSpeed, speedPoints))
                skillUseSpeed = int(input("Type how many points you'd like to spend(+)/refund(-) on 'SPEED': "))
                if skillUseSpeed > skillPoints:
                    while skillUseSpeed > skillPoints:
                        skillUseSpeed = int(input("Sorry you dont have that many points. Try again: "))
                    else: continue
                else:
                    skillPoints -= skillUseSpeed
                    speedPoints += skillUseSpeed
                    userSpeed += ((15)*skillUseSpeed)

                print("Speed Points used: %d\nSpeed: %d" %(speedPoints, userSpeed))
                skillContinue = input("Continue?(Y/N) ")

            if skillSelect == 'C' or skillSelect == 'c':
                print("HEALTH\nHealth: %d\nPoints used: %d" %(userHealth, healthPoints))
                skillUseHealth = int(input("Type how many points you'd like to spend(+)/refund(-) on 'HEALTH': "))
                if skillUseHealth > skillPoints:
                    while skillUseHealth > skillPoints:
                        skillUseHealth = int(input("Sorry you dont have that many points. Try again: "))
                    else: continue
                else:
                    skillPoints -= skillUseHealth
                    healthPoints += skillUseHealth
                    userHealth += ((15)*skillUseHealth)

                print("Health Points used: %d\nHealth: %d" %(healthPoints, userHealth))
             
                skillContinue = input("Continue?(Y/N) ")

            elif skillContinue == 'n' or skillContinue == 'N':
                break
                

    return

#menu
def menu():
    beginJourney = input('MENU\nStart your journey?(enter "start")\nSkill points menu(enter "skill")\nExit(enter "exit")\n')
    while beginJourney != ('exit') or beginJourney != ('skill') or beginJourney != ('start') :
        if beginJourney == 'skill':
            skill()
        if beginJourney == 'exit':
            print("Bye! ")
            quit()
        else:
            print("Your answer isnt recognized. Try again.")
            

        if beginJourney == 'start':
            break
    return    

#intro
menu()
print("Hello! Welcome to 'The Forest'!")
print("You have 3 skill points to start with.\nThroughout the game you can earn and use these points to give yourself boosts.")
print("\nSkills:\nA) Strength \nB) Speed\nC) Health" )
skill()

    