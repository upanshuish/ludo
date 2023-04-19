from random import randint

results=[]

class Red:

    pos=[0,0,0,0,0]
    unLock=[]
    inCenter=[]
    stops=[0,8,13,21,26,34,39,47]
    temp=0  

    def openPlayer(self):
        unlockPlayer=int(input("Which Player You Want To Unlock: "))
        if(f"PR{unlockPlayer}" in self.unLock):
            print(f"PR{unlockPlayer} is already unlocked,Please choose a Locked One!")
            Red.openPlayer(self)
        elif(f"PR{unlockPlayer}" in self.inCenter):
            print(f"PR{unlockPlayer} is at the Center,Please choose a Locked One!")
            Red.openPlayer(self)
        else:
            self.unLock.insert(unlockPlayer,f"PR{unlockPlayer}")
            print(f"PR{unlockPlayer} is UnLocked!")
            self.temp=unlockPlayer

    def kill(self,playerNumber,drVal):
        val=self.pos[playerNumber]+drVal
        if(val+52 in Blue.pos and val not in self.stops and val<=37):
            idx=Blue.pos.index(val+52)
            Blue.pos[idx]=39
            Blue.unLock.pop(idx)
            print(f"You(Red) killed PB{idx}.")
            self.pos[playerNumber]=val
            print(f"PR{playerNumber} is at '{self.pos[playerNumber]}'.")
            Red.roll(self)
        elif(val in Blue.pos and val not in self.stops and val<=50):
            idx=Blue.pos.index(val)
            Blue.pos[idx]=39
            Blue.unLock.pop(idx)
            print(f"You(Red) killed PB{idx}.")  
            self.pos[playerNumber]=val
            print(f"PR{playerNumber} is at '{self.pos[playerNumber]}'.")
            Red.roll(self) 
        elif(val+52 in Yellow.pos and val not in self.stops and val<=24):
            idx=Yellow.pos.index(val+52)
            Yellow.pos[idx]=26
            Yellow.unLock.pop(idx)
            print(f"You(Red) killed PY{idx}.")
            self.pos[playerNumber]=val
            print(f"PR{playerNumber} is at '{self.pos[playerNumber]}'.")
            Red.roll(self)
        elif(val in Yellow.pos and val not in self.stops and val<=50):
            idx=Yellow.pos.index(val)
            Yellow.pos[idx]=26
            Yellow.unLock.pop(idx)
            print(f"You(Red) killed PY{idx}.")
            self.pos[playerNumber]=val
            print(f"PR{playerNumber} is at '{self.pos[playerNumber]}'.")
            Red.roll(self) 
        elif(val+52 in Green.pos and val not in self.stops and val<=11):
            idx=Green.pos.index(val+52)
            Green.pos[idx]=13
            Green.unLock.pop(idx)
            print(f"You(Red) killed PG{idx}.")
            self.pos[playerNumber]=val
            print(f"PR{playerNumber} is at '{self.pos[playerNumber]}'.")
            Red.roll(self)
        elif(val in Green.pos and val not in self.stops and val<=50):
            idx=Green.pos.index(val)
            Green.pos[idx]=13
            Green.unLock.pop(idx)
            print(f"You(Red) killed PG{idx}.")
            self.pos[playerNumber]=val
            print(f"PR{playerNumber} is at '{self.pos[playerNumber]}'.")
            Red.roll(self)
        else: 
            self.pos[playerNumber]=val
            print(f"PR{playerNumber} is at '{self.pos[playerNumber]}'.")

    def checkAndMove(self,playerNumber,drVal):
        if (self.pos[playerNumber]+drVal<56):
            Red.kill(self,playerNumber,drVal)
        elif(self.pos[playerNumber]+drVal>56):
            print("Can't move Ahead, Choose another Player!") 
            Red.move(self,drVal)
        else:
            self.pos[playerNumber]=self.pos[playerNumber]+drVal
            Red.atCenter(self)

    def atCenter(self):
        idx=self.pos.index(56)
        removed=self.unLock.pop(idx)
        self.inCenter.append(removed)
        self.unLock.insert(idx, "At Center")
        print(f"{removed} reached the Center.")
        Red.roll(self)
        if(len(Red.inCenter)==4):
            results.append("🔴")
        
    def move(self,drVal):
        if(len(self.unLock)==1):
            Red.checkAndMove(self,self.temp,drVal)
        else:
            playerNumber=int(input("Which Player You Want To Move: "))
            if(Red.isUnlocked(self,playerNumber)):
                Red.checkAndMove(self,playerNumber,drVal)  
            else:
                print("Please choose an Unlocked player!")
                Red.move(self,drVal)

    def isUnlocked(self,playerNumber):
        if(f"PR{playerNumber}" in self.unLock):
            return True
        else:
            return False 

    def isFinished(self):
        if(len(self.inCenter)==4):
            return True
        else:
            return False        

    def roll(self):
        redRoll=input("🔴 -> ")
        if(redRoll=="r"):
            dr = randint(1, 6)
            print(f">>> {dr}")
            if(dr==6 and len(self.unLock)==0):
                Red.openPlayer(self) 
                Red.roll(self)     
            elif(1<=len(self.unLock)<4 and dr==6):
                choose=int(input("Press '1' to Move a Player.\nPress '2' to Unlock a New Player.\n"))
                if(choose==1):
                    Red.move(self,dr)
                    Red.roll(self)
                elif(choose==2):
                    Red.openPlayer(self)
                    Red.roll(self)    
            elif(dr!=6 and len(self.unLock)==0):
                pass
            else:
                Red.move(self,dr)
        else:
            pass

    def checkPositions(self):
        print(self.pos)

class Blue:

    pos=[39,39,39,39,39]
    unLock=[]
    inCenter=[]
    stops=[39,47,52,60,65,73,78,84]
    temp=0

    def openPlayer(self):
        unlockPlayer=int(input("Which Player You Want To Unlock: "))
        if(f"PB{unlockPlayer}" in self.unLock):
            print(f"PB{unlockPlayer} is already unlocked,Please choose a Locked One!")
            Blue.openPlayer(self)
        elif(f"PB{unlockPlayer}" in self.inCenter):
            print(f"PB{unlockPlayer} is at the Center,Please choose a Locked One!")
            Blue.openPlayer(self)
        else:
            self.unLock.insert(unlockPlayer,f"PB{unlockPlayer}")
            print(f"PB{unlockPlayer} is UnLocked!")
            self.temp=unlockPlayer
    
    def kill(self,playerNumber,drVal):
        val=self.pos[playerNumber]+drVal
        if(val-52 in Red.pos and val not in self.stops and val<=89):
            idx=Red.pos.index(val-52)
            Red.pos[idx]=0
            Red.unLock.pop(idx)
            print(f"You(Blue) killed PR{idx}.")
            self.pos[playerNumber]=val
            print(f"PB{playerNumber} is at '{self.pos[playerNumber]-39}'.")
            Blue.roll(self)
        elif(val in Red.pos and val not in self.stops and val<=50):
            idx=Red.pos.index(val)
            Red.pos[idx]=0
            Red.unLock.pop(idx)
            print(f"You(Blue) killed PR{idx}.")
            self.pos[playerNumber]=val
            print(f"PB{playerNumber} is at '{self.pos[playerNumber]-39}'.")
            Blue.roll(self)
        elif(val-52 in Yellow.pos and val not in self.stops and val<=89):
            idx=Yellow.pos.index(val-52)
            Yellow.pos[idx]=26
            Yellow.unLock.pop(idx)
            print(f"You(Blue) killed PY{idx}.")
            self.pos[playerNumber]=val
            print(f"PB{playerNumber} is at '{self.pos[playerNumber]-39}'.")
            Blue.roll(self)
        elif(val in Yellow.pos and val not in self.stops and val<=76):
            idx=Yellow.pos.index(val)
            Yellow.pos[idx]=26
            Yellow.unLock.pop(idx)
            print(f"You(Blue) killed PY{idx}.")
            self.pos[playerNumber]=val
            print(f"PB{playerNumber} is at '{self.pos[playerNumber]-39}'.")
            Blue.roll(self)
        elif(val-52 in Green.pos and val not in self.stops and val<=89):
            idx=Green.pos.index(val-52)
            Green.pos[idx]=13
            Green.unLock.pop(idx)
            print(f"You(Blue) killed PG{idx}.")
            self.pos[playerNumber]=val
            print(f"PB{playerNumber} is at '{self.pos[playerNumber]-39}'.")
            Blue.roll(self)
        elif(val in Green.pos and val not in self.stops and val<=63):
            idx=Green.pos.index(val)
            Green.pos[idx]=13
            Green.unLock.pop(idx)
            print(f"You(Blue) killed PG{idx}.")
            self.pos[playerNumber]=val
            print(f"PB{playerNumber} is at '{self.pos[playerNumber]-39}'.")
            Blue.roll(self)
        else:
            self.pos[playerNumber]=val
            print(f"PB{playerNumber} is at '{self.pos[playerNumber]-39}'.")
        
    def checkAndMove(self,playerNumber,drVal):
        if (self.pos[playerNumber]+drVal<95):
            Blue.kill(self,playerNumber,drVal)
        elif(self.pos[playerNumber]+drVal>95):
            print("Can't move Ahead, Choose another Player!") 
            Blue.move(self,drVal)
        else:
            self.pos[playerNumber]=self.pos[playerNumber]+drVal
            Blue.atCenter(self)

    def atCenter(self):
        idx=self.pos.index(95)
        removed=self.unLock.pop(idx)
        self.inCenter.append(removed)
        self.unLock.insert(idx, "At Center")
        print(f"{removed} reached the Center.")
        Blue.roll(self)
        if(len(Blue.inCenter)==4):
            results.append("🔵")


    def move(self,drVal):
        if(len(self.unLock)==1):
            Blue.checkAndMove(self,self.temp,drVal)
        else:
            playerNumber=int(input("Which Player You Want To Move: "))
            if(Blue.isUnlocked(self,playerNumber)):
                Blue.checkAndMove(self,playerNumber,drVal)  
            else:
                print("Please choose an Unlocked player!")
                Blue.move(self,drVal)

    def isUnlocked(self,playerNumber):
        if(f"PB{playerNumber}" in self.unLock):
            return True
        else:
            return False

    def isFinished(self):
        if(len(self.inCenter)==4):
            return True
        else:
            return False

    def roll(self):
        blueRoll=input("🔵 -> ")
        if(blueRoll=="b"):
            dr = randint(1, 6)
            print(f">>> {dr}")
            if(dr==6 and len(self.unLock)==0):
                Blue.openPlayer(self) 
                Blue.roll(self)     
            elif(1<=len(self.unLock)<4 and dr==6):
                choose=int(input("Press '1' to Move a Player.\nPress '2' to Unlock a New Player.\n"))
                if(choose==1):
                    Blue.move(self,dr)
                    Blue.roll(self)
                elif(choose==2):
                    Blue.openPlayer(self)
                    Blue.roll(self)    
            elif(dr!=6 and len(self.unLock)==0):
                pass
            else:
                Blue.move(self,dr)
        else:
            pass
        

    def checkPositions(self):
        print(self.pos)

class Yellow:

    pos=[26,26,26,26,26]
    unLock=[]
    inCenter=[]
    stops=[26,34,39,47,52,60,65,73]
    temp=0

    def openPlayer(self):
        unlockPlayer=int(input("Which Player You Want To Unlock: "))
        if(f"PY{unlockPlayer}" in self.unLock):
            print(f"PY{unlockPlayer} is already unlocked,Please choose a Locked One!")
            Yellow.openPlayer(self)
        elif(f"PY{unlockPlayer}" in self.inCenter):
            print(f"PY{unlockPlayer} is at the Center,Please choose a Locked One!")
            Yellow.openPlayer(self)
        else:
            self.unLock.insert(unlockPlayer,f"PY{unlockPlayer}")
            print(f"PY{unlockPlayer} is UnLocked!")
            self.temp=unlockPlayer

    def kill(self,playerNumber,drVal):
        val=self.pos[playerNumber]+drVal
        if(val in Red.pos and val not in self.stops and val<=50 ):
            idx=Red.pos.index(val)
            Red.pos[idx]=0
            Red.unLock.pop(idx)
            print(f"You(Yellow) killed PR{idx}.")
            self.pos[playerNumber]=val
            print(f"PY{playerNumber} is at '{self.pos[playerNumber]-26}'.")
            Yellow.roll(self)
        elif(val-52 in Red.pos and val not in self.stops and val<=76 ):
            idx=Red.pos.index(val-52)
            Red.pos[idx]=0
            Red.unLock.pop(idx)
            print(f"You(Yellow) killed PR{idx}.")
            self.pos[playerNumber]=val
            print(f"PY{playerNumber} is at '{self.pos[playerNumber]-26}'.")
            Yellow.roll(self)
        elif(val in Blue.pos and val not in self.stops and val<=76):
            idx=Blue.pos.index(val)
            Blue.pos[idx]=39
            Blue.unLock.pop(idx)
            print(f"You(Yellow) killed PB{idx}.")
            self.pos[playerNumber]=val
            print(f"PY{playerNumber} is at '{self.pos[playerNumber]-26}'.")
            Yellow.roll(self)
        elif(val+52 in Blue.pos and val not in self.stops and val<=37):
            idx=Blue.pos.index(val+52)
            Blue.pos[idx]=39
            Blue.unLock.pop(idx)
            print(f"You(Yellow) killed PB{idx}.")
            self.pos[playerNumber]=val
            print(f"PY{playerNumber} is at '{self.pos[playerNumber]-26}'.")
            Yellow.roll(self)
        elif(val in Green.pos and val not in self.stops and val<=63):
            idx=Green.pos.index(val)
            Green.pos[idx]=13
            Green.unLock.pop(idx)
            print(f"You(Yellow) killed PG{idx}.")
            self.pos[playerNumber]=val
            print(f"PY{playerNumber} is at '{self.pos[playerNumber]-26}'.")
            Yellow.roll(self)
        elif(val-52 in Green.pos and val not in self.stops and val<=76):
            idx=Green.pos.index(val-52)
            Green.pos[idx]=13
            Green.unLock.pop(idx)
            print(f"You(Yellow) killed PG{idx}.")
            self.pos[playerNumber]=val
            print(f"PY{playerNumber} is at '{self.pos[playerNumber]-26}'.")
            Yellow.roll(self)
        else:
            self.pos[playerNumber]=val
            print(f"PY{playerNumber} is at '{self.pos[playerNumber]-26}'.")

    def checkAndMove(self,playerNumber,drVal):
        if (self.pos[playerNumber]+drVal<82):
            Yellow.kill(self,playerNumber,drVal)
        elif(self.pos[playerNumber]+drVal>82):
            print("Can't move Ahead, Choose another Player!") 
            Yellow.move(self,drVal)
        else:
            self.pos[playerNumber]=self.pos[playerNumber]+drVal
            Yellow.atCenter(self)

    def atCenter(self):
        idx=self.pos.index(82)
        removed=self.unLock.pop(idx)
        self.inCenter.append(removed)
        self.unLock.insert(idx, "At Center")
        print(f"{removed} reached the Center.")
        Yellow.roll(self)
        if(len(Yellow.inCenter)==4):
            results.append("🟡")

    def move(self,drVal):
        if(len(self.unLock)==1):
            Yellow.checkAndMove(self,self.temp,drVal)
        else:
            playerNumber=int(input("Which Player You Want To Move: "))
            if(Yellow.isUnlocked(self,playerNumber)):
                Yellow.checkAndMove(self,playerNumber,drVal)  
            else:
                print("Please choose an Unlocked player!")
                Yellow.move(self,drVal)

    def isUnlocked(self,playerNumber):
        if(f"PY{playerNumber}" in self.unLock):
            return True
        else:
            return False
    
    def isFinished(self):
        if(len(self.inCenter)==4):
            return True
        else:
            return False

    def roll(self):
        yellowRoll=input("🟡 -> ")
        if(yellowRoll=="y"):
            dr = randint(1, 6)
            print(f">>> {dr}")
            if(dr==6 and len(self.unLock)==0):
                Yellow.openPlayer(self) 
                Yellow.roll(self)     
            elif(1<=len(self.unLock)<4 and dr==6):
                choose=int(input("Press '1' to Move a Player.\nPress '2' to Unlock a New Player.\n"))
                if(choose==1):
                    Yellow.move(self,dr)
                    Yellow.roll(self)
                elif(choose==2):
                    Yellow.openPlayer(self)
                    Yellow.roll(self)    
            elif(dr!=6 and len(self.unLock)==0):
                pass
            else:
                Yellow.move(self,dr)
        else:
            pass   
    
    def checkPositions(self):
        print(self.pos)

class Green:

    pos=[13,13,13,13,13]
    unLock=[]
    inCenter=[]
    stops=[13,21,26,34,39,47,52,60]
    temp=0

    def openPlayer(self):
        unlockPlayer=int(input("Which Player You Want To Unlock: "))
        if(f"PG{unlockPlayer}" in self.unLock):
            print(f"PG{unlockPlayer} is already unlocked,Please choose a Locked One!")
            Green.openPlayer(self)
        elif(f"PG{unlockPlayer}" in self.inCenter):
            print(f"PG{unlockPlayer} is at the Center,Please choose a Locked One!")
            Green.openPlayer(self)
        else:
            self.unLock.insert(unlockPlayer,f"PG{unlockPlayer}")
            print(f"PG{unlockPlayer} is UnLocked!")
            self.temp=unlockPlayer
    
    def kill(self,playerNumber,drVal):
        val=self.pos[playerNumber]+drVal
        if(val in Red.pos and val not in self.stops and val<=50):
            idx=Red.pos.index(val)
            Red.pos[idx]=0
            Red.unLock.pop(idx)
            print(f"You(Green) killed PR{idx}.")
            self.pos[playerNumber]=val
            print(f"PG{playerNumber} is at '{self.pos[playerNumber]-13}'.")
            Green.roll(self)
        elif(val-52 in Red.pos and val not in self.stops and val<=63):
            idx=Red.pos.index(val-52)
            Red.pos[idx]=0
            Red.unLock.pop(idx)
            print(f"You(Green) killed PR{idx}.")
            self.pos[playerNumber]=val
            print(f"PG{playerNumber} is at '{self.pos[playerNumber]-13}'.")
            Green.roll(self)
        elif(val in Yellow.pos and val not in self.stops and val<=63):
            idx=Yellow.pos.index(val)
            Yellow.pos[idx]=26
            Yellow.unLock.pop(idx)
            print(f"You(Green) killed PY{idx}.")
            self.pos[playerNumber]=val
            print(f"PG{playerNumber} is at '{self.pos[playerNumber]-13}'.")
            Green.roll(self)
        elif(val+52 in Yellow.pos and val not in self.stops and val<=76):
            idx=Yellow.pos.index(val+52)
            Yellow.pos[idx]=26
            Yellow.unLock.pop(idx)
            print(f"You(Green) killed PY{idx}.")
            self.pos[playerNumber]=val
            print(f"PG{playerNumber} is at '{self.pos[playerNumber]-13}'.")
            Green.roll(self)
        elif(val in Blue.pos and val not in self.stops and val<=63):
            idx=Blue.pos.index(val)
            Blue.pos[idx]=39
            Blue.unLock.pop(idx)
            print(f"You(Green) killed PB{idx}.")
            self.pos[playerNumber]=val
            print(f"PG{playerNumber} is at '{self.pos[playerNumber]-13}'.")
            Green.roll(self)
        elif(val+52 in Blue.pos and val not in self.stops and val<=37):
            idx=Blue.pos.index(val+52)
            Blue.pos[idx]=39
            Blue.unLock.pop(idx)
            print(f"You(Green) killed PB{idx}.")
            self.pos[playerNumber]=val
            print(f"PG{playerNumber} is at '{self.pos[playerNumber]-13}'.")
            Green.roll(self)
        else:
            self.pos[playerNumber]=val
            print(f"PG{playerNumber} is at '{self.pos[playerNumber]-13}'.")

    def checkAndMove(self,playerNumber,drVal):
        if (self.pos[playerNumber]+drVal<69):
            Green.kill(self,playerNumber,drVal)
        elif(self.pos[playerNumber]+drVal>69):
            print("Can't move Ahead, Choose another Player!") 
            Green.move(self,drVal)
        else:
            self.pos[playerNumber]=self.pos[playerNumber]+drVal
            Green.atCenter(self)

    def atCenter(self):
        idx=self.pos.index(69)
        removed=self.unLock.pop(idx)
        self.inCenter.append(removed)
        self.unLock.insert(idx, "At Center")
        print(f"{removed} reached the Center.")
        Green.roll(self)
        if(len(Green.inCenter)==4):
            results.append("🟢")
            
    def move(self,drVal):
        if(len(self.unLock)==1):
            Green.checkAndMove(self,self.temp ,drVal)
        else:
            playerNumber=int(input("Which Player You Want To Move: "))
            if(Green.isUnlocked(self,playerNumber)):
                Green.checkAndMove(self,playerNumber,drVal)  
            else:
                print("Please choose an Unlocked player!")
                Green.move(self,drVal)

    def isUnlocked(self,playerNumber):
        if(f"PG{playerNumber}" in self.unLock):
            return True
        else:
            return False

    def isFinished(self):
        if(len(self.inCenter)==4):
            return True
        else:
            return False

    def roll(self):
        greenRoll=input("🟢 -> ")
        if(greenRoll=="g"):
            dr = randint(1, 6)
            print(f">>> {dr}")
            if(dr==6 and len(self.unLock)==0):
                Green.openPlayer(self) 
                Green.roll(self)     
            elif(1<=len(self.unLock)<4 and dr==6):
                choose=int(input("Press '1' to Move a Player.\nPress '2' to Unlock a New Player.\n"))
                if(choose==1):
                    Green.move(self,dr)
                    Green.roll(self)
                elif(choose==2):
                    Green.openPlayer(self)
                    Green.roll(self)    
            elif(dr!=6 and len(self.unLock)==0):
                pass
            else:
                Green.move(self,dr)
        else:
            pass 
    def checkPositions(self):
        print(self.pos)
       
if(__name__ == "__main__"):
    r=Red()
    b=Blue()
    y=Yellow()
    g=Green()

    print("\n:::::::::::::::::::::::::::::LUDO:::::::::::::::::::::::::::::\n")
    
    redRoll=input("🔴 -> ")
    if(redRoll=="r"):
        red = randint(1, 6)
        print(f">>> {red}")
    else:
        pass

    blueRoll=input("🔵 -> ")
    if(blueRoll=="b"):
        blue = randint(1, 6)
        print(f">>> {blue}")
    else:
        pass

    yellowRoll=input("🟡 -> ")
    if(yellowRoll=="y"):
        yellow = randint(1, 6)
        print(f">>> {yellow}")
    else:
        pass

    greenRoll=input("🟢 -> ")
    if(greenRoll=="g"):
        green = randint(1, 6)
        print(f">>> {green}")
    else:
        pass
    
    if(red>=max(red,blue,yellow,green)):
        print("Red Rolls The Dice First!")
        while(True):
            if(r.isFinished()==False):
                r.roll()
            if(g.isFinished()==False):
                g.roll()
            if(y.isFinished()==False):
                y.roll()
            if(b.isFinished()==False):
                b.roll()
            if(y.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and y.isFinished()):
                break
            elif(g.isFinished() and y.isFinished() and r.isFinished()):
                break
    elif(blue>=max(red,blue,yellow,green)):
        print("Blue Rolls The Dice First!")
        while(True):
            if(b.isFinished()==False):
                b.roll()
            if(r.isFinished()==False):
                r.roll()
            if(g.isFinished()==False):
                g.roll()
            if(y.isFinished()==False):
                y.roll()
            if(y.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and y.isFinished()):
                break
            elif(g.isFinished() and y.isFinished() and r.isFinished()):
                break
    elif(yellow>=max(red,blue,yellow,green)):
        print("Yellow Rolls The Dice First!")
        while(True):
            if(y.isFinished()==False):
                y.roll()
            if(b.isFinished()==False):
                b.roll()
            if(r.isFinished()==False):
                r.roll()
            if(g.isFinished()==False):
                g.roll()
            if(y.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and y.isFinished()):
                break
            elif(g.isFinished() and y.isFinished() and r.isFinished()):
                break
        
    elif(green>=max(red,blue,yellow,green)):
        print("Green Rolls The Dice First!")
        while(True):
            if(g.isFinished()==False):
                g.roll()
            if(y.isFinished()==False):
                y.roll()
            if(b.isFinished()==False):
                b.roll()
            if(r.isFinished()==False):
                r.roll()
            if(y.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and r.isFinished()):
                break
            elif(g.isFinished() and b.isFinished() and y.isFinished()):
                break
            elif(g.isFinished() and y.isFinished() and r.isFinished()):
                break

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~Resuts~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


    for i in range(0,3):
        if(i==0):
            print(f"{results[i]} is {i+1}st.")
        elif(i==1):
            print(f"{results[i]} is {i+1}nd.")
        else:
            print(f"{results[i]} is {i+1}rd.")



    





    
    
    
