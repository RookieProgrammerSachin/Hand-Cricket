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
            User_bowl = input("Vei.. ")
            if not User_bowl or not User_bowl.isdigit():
                print("Number eh illa.. -_-")
                continue
            else:
                Userbowl = int(User_bowl)
                
            if Userbowl<1 or Userbowl>10:
                print("Adingu! Dai",name,"uh, Ozhunga vei daa...")
                continue
            
            if Userbowl == bat_PC:
                if scoreofpc == 0:
                    print("Duck out uh! XD")
                    break
                print()
                print(ene_name,"Out-uh! Sooper ra",name,"...!")
                print("Nee vechadhu:",Userbowl,ene_name,"vechadhu:",bat_PC)
                print(ene_name," Score:",scoreofpc)
                scoreofpc += 1
                print(scoreofpc,"to win")
                break
            
            else:
                print(ene_name,"thappichaan. Avan",bat_PC,"vechaan")
                scoreofpc += bat_PC
                print("Score:",scoreofpc)
                if 50<=scoreofpc<=59:
                    print(ene_name,"Half century da..")
                elif 100<=scoreofpc<=109:
                    print(ene_name,"Century da.. Seekrom out panna paaru..")
                    
        
        print()
        print(name,"Nee ippo batting pannu..")
        print()
        
        a = 0
        score = 0 
        while True:
            b = random.randrange(1,11)
            a = input("Podu.. ")
            if not a or not a.isdigit():
                print("Dhe chi olunga podu... ")
                continue
            else:
                aa = int(a)
                
            if aa<1 or aa>10:
                print("Thambi",name,"uh.. Ozhunga veinga..")
                continue
            
            if scoreofpc == 0  and aa != b:
                print("Win panta daa!")
                print("Un score:",a,"|",ene_name,"score:",scoreofpc)
                break

            if score == scoreofpc and aa!=b:
                score += aa
                print("Nee vechadu:",a,"|",ene_name,"vecadhu:",b)
                print("You Won!")
                print("Un score:",score,"|",ene_name,"score:",scoreofpc)
                break
            
            if aa==b:
                print()
                print(name,"Out ehhh..")
                print("Nee vechadhu:",aa,ene_name,"vechadhu:",b)
                if score < scoreofpc:
                    print("Nee out-uh da..")
                    print("Paravala vidu..")
                    print("Un score:",score,"|",ene_name,"score:",scoreofpc)
                    print(ene_name,"win pannitaanae..")
                    break
                elif score == scoreofpc:
                    print("Draw match")
                    print("Un score:",score,"|",ene_name,"score:",scoreofpc)
                    break
                
            elif score < scoreofpc:
                print("Thappicha da!",ene_name,"vechadhu",b)
                score +=aa
                print("Score:",score)
                if 50<=score<=59:
                    print("Half century da.. Super!")
                elif 100<=score<=109:
                    print("Century da.. Super ra!",name)
                    
            if score > scoreofpc:
                print(name,"Jeichitaa da..! Your Score:",score)
                print(ene_name,"eh Pochu po.. Avan Score:",scoreofpc)
                break

            else:
                score += aa        

    def User_Batting():
        a = 0
        score = 0
        global ManScore 
        while True:
            b = random.randrange(1,11)
            a = input("Podu.. ")
            if not a or not a.isdigit():
                print("Invalid.. -_-")
                continue
            else:
                aa = int(a)
                
            if aa<1 or aa>10:
                print("Thambi",name,"uh.. Ozhunga veinga..")
                continue

            if aa==b:
                print()
                print(name,"Out ehh!..")
                print("Nee vechadhu:",aa,"|",ene_name,"vechadhu:",b)
                print("Score:",score)
                score += 1
                print(score,"to win")
                break
            
            else:
                print("Thappicha da!",ene_name,"vechadhu",b)
                score += aa
                print("Score:",score)
                if 50<=score<=59:
                    print("Half-century!...")
                elif 100<=score<=109:
                    print("Century!..")
                    
        
        print()
        print(name,"ippo nee bowling podu...")
        print()
        
        bat_PC = 0
        User_bowl = 0
        scoreofpc = 0 
        while True:
            bat_PC = random.randrange(1,11)
            User_bowl = input("Vei.. ")
            if not User_bowl or not User_bowl.isdigit():
                print("Error-uh!")
                continue
            else:
                Userbowl = int(User_bowl)
                
            if Userbowl<1 or Userbowl>10:
                print(name,"!!..Ozhunga vei daa..")
                continue

            if score == 0  and bat_PC != Userbowl:
                score += a
                print("You Lost!")
                print("Un score:",score,"PC Score:",bat_PC)
                break

            if score == scoreofpc and Userbowl != bat_PC:
                scoreofpc += bat_PC
                print(ene_name,"vechadhu:",bat_PC,"Nee:",Userbowl)
                print("You lost!")
                print("Un score:",score,ene_name,"score:",scoreofpc)
                time.sleep(3)
                break
            
            if Userbowl == bat_PC:
                print()
                print("You kept",Userbowl,ene_name,"kept:",bat_PC)
                if scoreofpc < score:
                    print(ene_name," Out-uh....! Sooper ra!..")
                    print("Un score:",score,ene_name,"score:",scoreofpc)
                    print("Nee winnu da!!.. Congrats",name)
                    break
                elif scoreofpc == score:
                    print("Draw match!..")
                    print("Un score:",score,"|",ene_name," Score:",scoreofpc)
                    break
                
            elif scoreofpc < score:
                print(ene_name,"thappichaan. Avan",bat_PC,"vechaan")
                scoreofpc += bat_PC
                print("Score:",scoreofpc)
                if 50<=scoreofpc<=59:
                    print(ene_name,"Half-century da..Seekrom out pannu..")
                elif 100<=scoreofpc<=109:
                    print(ene_name,"Century da..")

            if scoreofpc > score: 
                print(ene_name,"won!.. Avan Score:",scoreofpc)
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
            print("Ada chi name type panraa!")
            continue
        elif ask[0] == "y" or ask[0] == "Y":
            name = input("Un per Sollu: ")
            ene_name = input("Un enemy name-ah sollu: ")
            if name == ene_name:
                print("Nee unakke edhiriya irukka koodadhu...")
                continue
            break
        elif ask[0] == "n" or ask[0] =="N":
            print("That's fine")
            name = "Player"
            ene_name = "PC"
            break
        else:
            print("Aiyo .. ozhunga input kudu da..")
            continue

    while True:
        print()
        print("OK",name,"un enemy",ene_name,"Kuda hand cricket aadriya?",end=' ')
        ask_play = input("Y/N? ")
        if not ask_play:
            continue
        elif ask_play[0] == "y" or ask_play[0] == "Y":
            break
        elif ask_play[0] == "n" or ask_play[0] == "N":
            print("Aprom edhukku indha script-ah thorandha..")
            time.sleep(2)
            quit()
        else:
            print("Idhukku poi input thappa thariyae.. unna..")
        

                        
    while True:
        toss = input("Odd ah..? Even ah..? ")
        if toss[0] == "o" or toss[0] == "e":
            break
        else:
            print("Odd ah even ah nu mattum sollu..")
            continue
    
    while True:
        pc_toss = random.randint(1,6)
        user_toss = input("Toss Podu.. ")
        if not user_toss or not user_toss.isdigit():
            print("Invalid input ra dei!")
            continue
        else:
            usertoss = int(user_toss)
            
        if usertoss<1 or usertoss>6:
            print("Thappu .. 6 mela vekkaadha")
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
                choose_for_bat_or_bowl = input("Nee toss win panita.. Enna choose panra? Batting-ah Bowling-ah?.. ")
                if choose_for_bat_or_bowl.lower()[0:3] == "bat":
                    User_Batting()
                    break
                elif choose_for_bat_or_bowl.lower()[0:4] == "bowl":
                    Bowl()
                    break
                else:
                    print("Loosu maari solladha... Thirumba select pannu..")
                    continue
        
        elif total_toss%2 == 0 and toss == "odd":
            print(usertoss,"+",pc_toss,"=",total_toss,"..",tos,"!")
            print("Toss Pochu...")
            pc_b_or_b = random.randint(1,3)
            if pc_b_or_b == 1:
                print("Thinking",end='')
                for y in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"batting panraapla..")
                Bowl()
                break
            else:
                print("Thinking",end='')
                for a in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"bowling podraan...")
                User_Batting()
                break
            
        elif total_toss%2 != 0 and toss == "even":
            print(usertoss,"+",pc_toss,"=",total_toss,"..",tos,"!")
            print(ene_name,"toss win pannitaan...")
            pc_b_or_b = random.randint(1,3)
            if pc_b_or_b == 1:
                print("Thinking",end='')
                for a in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"batting pandraan...")
                Bowl()
                break
            else:
                print("Thinking",end='')
                for a in range(5):
                    print(".",end='')
                    time.sleep(0.5)
                print(".")
                print(ene_name,"bowling podraan..")
                User_Batting()
                break
            
        else:
            print(usertoss,"+",pc_toss,"=",total_toss,"..",tos,"!")
            print("Toss win pannita...")
            while True:
                choose_for_bat_or_bowl = input("Nee toss win panita.. Enna choose panra? Batting-ah Bowling-ah?.. ")
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
        
        if quitter.lower()[0] == "y":
            print("Thank You for playing!")
            credit = "  ***Script created by ***Techno-Sachin***"
            for x in range(0,len(credit)):
                print(credit[x],end='')
                time.sleep(0.05)
            time.sleep(1)
            quit()
        elif quitter.lower()[0] == "n":
            print()
            print("Playing again..")
            print()
            break
        else:
            print("It's a wrong input. Try again")
            continue
    continue
