import random
import time
while True:
    pc_b_or_b = 0  
    def Bowl():
        bat_PC = 0
        User_bowl = 0
        scoreofpc = 0 
        while True:
            bat_PC = random.randrange(1,11)
            User_bowl = input("Yes.. bowl(type any number from 1 to 10): ")
            if not User_bowl or not User_bowl.isdigit():
                print("No number detected. :-|")
                continue
            else:
                Userbowl = int(User_bowl)
                
            if Userbowl<1 or Userbowl>10:
                print("Hey",name,"! No!")
                continue
            
            if Userbowl == bat_PC:
                if scoreofpc == 0:
                    print("Duck out!")
                    break
                print()
                print(ene_name,"is Out! Good job",name,"...!")
                print("You :",Userbowl,"|",ene_name,":",bat_PC)
                print(ene_name," Score:",scoreofpc)
                scoreofpc += 1
                print(scoreofpc,"to win")
                break
            
            else:
                print(ene_name,"is safe. He chose:",bat_PC)
                scoreofpc += bat_PC
                print("Score:",scoreofpc)
                if 50<=scoreofpc<=59:
                    print(ene_name,"Half century..!")
                elif 100<=scoreofpc<=109:
                    print(ene_name,", that's a Century!.. Try to knock him off soon..")
                    
        
        print()
        print(name,"Your turn to bat now..")
        print()
        
        a = 0
        score = 0 
        while True:
            b = random.randrange(1,11)
            a = input("Yes... type (any num from 1 to 10): ")
            if not a or not a.isdigit():
                print("Invalid")
                continue
            else:
                aa = int(a)
                
            if aa<1 or aa>10:
                print("Dear,",name,"that's wrong input!")
                continue
            
            if scoreofpc == 0  and aa != b:
                print("You Won!")
                print("Your score:",a,"|",ene_name,"score:",scoreofpc)
                break

            if score == scoreofpc and aa!=b:
                score += aa
                print("You:",a,ene_name,":",b)
                print("You Won!")
                print("Your score:",score,"|",ene_name,"score:",scoreofpc)
                break
            
            if aa==b:
                print()
                print(name,"Outeee..")
                print("You:",aa,ene_name,":",b)
                if score < scoreofpc:
                    print("You have lost to",ene_name)
                    print("That's OK..")
                    print("Your score:",score,"|",ene_name,"score:",scoreofpc)
                    print(ene_name,"won the match!...")
                    break
                elif score == scoreofpc:
                    print("Draw match")
                    print("Your score:",score,"|",ene_name,"Score:",scoreofpc)
                    break
                
            elif score < scoreofpc:
                print("Escape!",ene_name,"kept",b)
                score +=aa
                print("Score:",score)
                if 50<=score<=59:
                    print("Half century!.. Keep going!")
                elif 100<=score<=109:
                    print("Century da.. Nice one!",name)
                    
            if score > scoreofpc:
                print(name,"You did it..! Your Score:",score)
                print(ene_name,"Lost.. Their Score:",scoreofpc)
                break

            else:
                score += aa        

    def User_Batting():
        a = 0
        score = 0
        global ManScore 
        while True:
            b = random.randrange(1,11)
            a = input("Yes, proceed (any num from 1 to 10): ")
            if not a or not a.isdigit():
                print("Invalid.. :-|")
                continue
            else:
                aa = int(a)
                
            if aa<1 or aa>10:
                print("NO",name,"! Give correct input only!..")
                continue

            if aa==b:
                print()
                print(name,"is Out..!")
                print("You kept:",aa,"|",ene_name,":",b)
                print("Score:",score)
                score += 1
                print(score,"to win")
                break
            
            else:
                print("Escape!",ene_name,"kept:",b)
                score += aa
                print("Score:",score)
                if 50<=score<=59:
                    print("Half-century!...")
                elif 100<=score<=109:
                    print("Century!..")
                    
        
        print()
        print(name,",now your turn to bowl...")
        print()
        
        bat_PC = 0
        User_bowl = 0
        scoreofpc = 0 
        while True:
            bat_PC = random.randrange(1,11)
            User_bowl = input("Yes... ")
            if not User_bowl or not User_bowl.isdigit():
                print("Error")
                continue
            else:
                Userbowl = int(User_bowl)
                
            if Userbowl<1 or Userbowl>10:
                print(name,"! Give correct input only..")
                continue

            if score == 0  and bat_PC != Userbowl:
                score += a
                print("You Lost!")
                print("Your score:",score,ene_name,"Score:",bat_PC)
                break

            if score == scoreofpc and Userbowl != bat_PC:
                scoreofpc += bat_PC
                print(ene_name,":",bat_PC,"You:",Userbowl)
                print("You lost!")
                print("Your score:",score,ene_name,"score:",scoreofpc)
                time.sleep(3)
                break
            
            if Userbowl == bat_PC:
                print()
                print("You kept",Userbowl,"|",ene_name,"chose:",bat_PC)
                if scoreofpc < score:
                    print(ene_name," Out....! Superb",name,"!..")
                    print("Your score:",score,"|",ene_name,"score:",scoreofpc)
                    print("You won the match!!.. Congrats",name)
                    break
                elif scoreofpc == score:
                    print("Draw match!..")
                    print("Youe score:",score,"|",ene_name," Score:",scoreofpc)
                    break
                
            elif scoreofpc < score:
                print(ene_name,"escaped. He kept:",bat_PC)
                scoreofpc += bat_PC
                print("Score:",scoreofpc)
                if 50<=scoreofpc<=59:
                    print(ene_name,"Half-century!")
                elif 100<=scoreofpc<=109:
                    print(ene_name,"Century..")

            if scoreofpc > score: 
                print(ene_name,"won!.. His Score:",scoreofpc)
                print("You Lost.. Score:",score)
                break
                    

        
    print()
    print("_________________________________________________")
    print()
    print("H A N D   C R C I K E T   W I T H   M A C H I N E")
    
    print("_________________________________________________")
    print()

    
    while True:
        ask = input("Want to enter names? Y/N?")
        if not ask:
            continue
        if ask[0] == "y" or ask[0] == "Y":
            name = input("Your name: ")
            ene_name = input("Your enemy's name: ")
            break
        elif ask[0] == "n" or ask[0] =="N":
            print("That's fine. Setting default names.")
            name = "Player"
            ene_name = "PC"
            break
        else:
            print("Invalid input..")
            continue

    while True:
        print()
        print("OK",name,", are you ready to play with",ene_name,"?",end=' ')
        ask_play = input("Y/N? ")
        if not ask_play:
            continue
        if ask_play[0] == "y" or ask_play[0] == "Y":
            break
        elif ask_play[0] == "n" or ask_play[0] == "N":
            print("Then why did you open up this script... :-| ")
            time.sleep(1)
            quit()
        else:
            print("Invalid input..")
        

                        
    while True:
        toss = input("Odd or Even? ")
        if not toss:
            continue
        if toss[0] == "o" or toss[0] == "e":
            break
        else:
            print("Invalid input..")
            continue
    
    while True:
        pc_toss = random.randint(1,6)
        user_toss = input("Toss (number from 1 to 6): ")
        if not user_toss or not user_toss.isdigit():
            print("Invalid input..")
            continue
        else:
            usertoss = int(user_toss)
            
        if usertoss<1 or usertoss>6:
            print("Please don't give wrong input numbers..")
            continue
        if pc_toss == usertoss:
            print("Same toss!")
            continue
        total_toss = pc_toss + usertoss
        if total_toss %2 == 0:
            tos = "Even"
        else:
            tos = "Odd"
        
        if total_toss%2==0 and toss == "even":
            print(usertoss,"+",pc_toss,"=",total_toss,"..",tos,"!")
            while True:
                choose_for_bat_or_bowl = input("You have won the toss! What do you choose? Batting or Bowling (just type bat or bowl)? ")
                if choose_for_bat_or_bowl[0:3] == "bat":
                    User_Batting()
                    break
                elif choose_for_bat_or_bowl[0:4] == "bowl":
                    Bowl()
                    break
                else:
                    print("Wrong input!..")
                    continue
        
        elif total_toss%2 == 0 and toss == "odd":
            print(usertoss,"+",pc_toss,"=",total_toss,"..",tos,"!")
            print("You lost toss..")
            pc_b_or_b = random.randint(1,3)
            if pc_b_or_b == 1:
                print("Thinking",end='')
                for y in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"has chosen batting")
                Bowl()
                break
            else:
                print("Thinking",end='')
                for a in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"has chose to bowl..")
                User_Batting()
                break
            
        elif total_toss%2 != 0 and toss == "even":
            print(usertoss,"+",pc_toss,"=",total_toss,"..",tos,"!")
            print(ene_name,"won the toss..")
            pc_b_or_b = random.randint(1,3)
            if pc_b_or_b == 1:
                print("Thinking",end='')
                for a in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"is batting..")
                Bowl()
                break
            else:
                print("Thinking",end='')
                for a in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"is bowling")
                User_Batting()
                break
            
        else:
            print(usertoss,"+",pc_toss,"=",total_toss,"..",tos,"!")
            print("You have won toss...",end = ' ')
            while True:
                choose_for_bat_or_bowl = input("What will you choose? Batting or Bowling(just type bat or bowl)? ")
                if choose_for_bat_or_bowl == "bat":
                    User_Batting()
                    break
                elif choose_for_bat_or_bowl == "bowl":
                    Bowl()
                    break
                else:
                    print("Wrong input. Try again")
                    continue
        break


    while True:
        print()
        print()
        quitter = input("Do you wanna Quit? Y/N? ")
        if not quitter:
            print("Wrong Input..")
            continue
        
        if quitter == "yes" or quitter == "y" or quitter == "Y":
            print("Thank You for playing!")
            credit = "   Script created by ***Techno-Sachin***  "
            for x in range(0,len(credit)):
                print(credit[x],end='')
                time.sleep(0.05)
            time.sleep(1)
            quit()
        elif quitter == "n" or quitter == "no" or quitter == "N":
            print()
            print("Playing again..")
            print()
            break
        else:
            print("It's a wrong input. Try again")
            continue
    continue
