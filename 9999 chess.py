#chess
#TO DO:
#check
#checkmate?
#mouse to move - next
#new pieces?
#colours:light square khaki, dark squares saddle brown 
import random, time, turtle
def boardSetup():
    board=[["wRo","wKn","wBi","wQu","wKi","wBi","wKn","wRo"],["wPa"]*8,["   "]*8,["   "]*8,["   "]*8,["   "]*8,["bPa"]*8,["bRo","bKn","bBi","bQu","bKi","bBi","bKn","bRo"]]
    return board

def empty(colour):
    turtle.color(colour)
    turtle.pd
    turtle.begin_fill()
    for i in range(0,4):
        turtle.fd(50)
        turtle.rt(90)
    turtle.end_fill()
    turtle.pu

def pawnB(colour,team):
    if team=="w":
        team="white"
    elif team=="b":
        team="black"
    empty(colour)
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(10)
    turtle.pd()
    turtle.fillcolor(team)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fd(30)
    turtle.lt(120)
    turtle.fd(20)
    turtle.rt(90)
    turtle.circle(10,300)
    turtle.rt(90)
    turtle.fd(20)
    turtle.end_fill()
    turtle.pu()
    turtle.rt(60)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(180)

def bishopB(colour,team):
    if team=="w":
        team="white"
    elif team=="b":
        team="black"
    empty(colour)
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(10)
    turtle.pd()
    turtle.fillcolor(team)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fd(30)
    turtle.lt(120)
    turtle.fd(20)
    turtle.rt(90)
    turtle.circle(10,120)
    turtle.lt(80)
    turtle.fd(12)
    turtle.rt(140)
    turtle.fd(12)
    turtle.lt(90)
    turtle.circle(12,152)
    turtle.rt(90)
    turtle.fd(18)
    turtle.end_fill()
    turtle.pu()
    turtle.rt(60)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(180)
    turtle.goto(x,y)
    turtle.seth(90)
    

def rookB(colour,team):
    if team=="w":
        team="white"
    elif team=="b":
        team="black"
    empty(colour)
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(10)
    turtle.pd()
    turtle.fillcolor(team)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fd(30)
    turtle.lt(90)
    turtle.fd(5)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(25)
    turtle.rt(90)
    turtle.fd(5)
    turtle.lt(90)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(6)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(6)
    turtle.rt(90)
    turtle.fd(5)
    turtle.lt(90)
    turtle.fd(6)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(6)
    turtle.rt(90)
    turtle.fd(5)
    turtle.lt(90)
    turtle.fd(6)
    turtle.lt(90)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(25)
    turtle.rt(90)
    turtle.fd(5)
    turtle.lt(90)
    turtle.fd(5)
    turtle.end_fill()
    turtle.pu()
    turtle.rt(90)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(180)

def knightB(colour,team):
    if team=="w":
        team="white"
    elif team=="b":
        team="black"
    empty(colour)
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(20)
    turtle.pd()
    turtle.fillcolor(team)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fd(20)
    turtle.lt(90)
    turtle.circle(70,25)
    turtle.circle(10,65)
    turtle.rt(75)
    turtle.fd(10)
    turtle.lt(150)
    turtle.fd(10)
    turtle.rt(115)
    turtle.fd(10)
    turtle.lt(150)
    turtle.fd(10)
    turtle.rt(90)
    turtle.circle(20,50)
    turtle.lt(50)
    turtle.fd(10)
    turtle.lt(140)
    turtle.circle(-10,200)
    turtle.rt(40)
    turtle.circle(15,40)
    turtle.end_fill()
    turtle.pu()
    turtle.rt(90)
    turtle.fd(10)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(180)
    turtle.goto(x,y)
    turtle.seth(90)
    

def queenB(colour,team):
    if team=="w":
        team="white"
    elif team=="b":
        team="black"
    empty(colour)
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(15)
    turtle.pd()
    turtle.fillcolor(team)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fd(20)
    turtle.lt(75)
    turtle.fd(30)
    turtle.lt(90)
    turtle.circle(-5)
    turtle.lt(50)
    turtle.fd(12)
    turtle.rt(80)
    turtle.fd(10)
    turtle.lt(45)
    turtle.circle(-5)
    turtle.lt(45)
    turtle.fd(10)
    turtle.rt(80)
    turtle.fd(12)
    turtle.lt(50)
    turtle.circle(-5)
    turtle.lt(90)
    turtle.fd(30)
    turtle.lt(75)
    turtle.end_fill()
    turtle.pu()
    turtle.goto(x,y)
    turtle.seth(90)

def kingB(colour,team):
    if team=="w":
        team="white"
    elif team=="b":
        team="black"
    empty(colour)
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.fd(5)
    turtle.rt(90)
    turtle.fd(15)
    turtle.pd()
    turtle.fillcolor(team)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.fd(20)
    turtle.lt(75)
    turtle.fd(30)
    turtle.lt(90)
    turtle.lt(50)
    turtle.fd(12)
    turtle.rt(80)
    turtle.fd(10)
    turtle.lt(45)
    turtle.lt(45)
    turtle.fd(10)
    turtle.rt(80)
    turtle.fd(12)
    turtle.lt(50)
    turtle.lt(90)
    turtle.fd(30)
    turtle.lt(75)
    turtle.end_fill()
    turtle.pu()
    turtle.goto(x,y)
    turtle.seth(90)
    
def boardBuild():
    turtle.pu()
    turtle.goto(-175,-175)
    turtle.pd()
    rookB("saddle brown","w")
    adjust()
    knightB("khaki","w")
    adjust()
    bishopB("saddle brown","w")
    adjust()
    queenB("khaki","w")
    adjust()
    kingB("saddle brown","w")
    adjust()
    bishopB("khaki","w")
    adjust()
    knightB("saddle brown","w")
    adjust()
    rookB("khaki","w")
    up()
    for i in range(0,4):
        pawnB("khaki","w")
        adjust()
        pawnB("saddle brown","w")
        adjust()
    unadjust()
    for i in range(0,2):
        up()
        for x in range(0,4):
            empty("saddle brown")
            adjust()
            empty("khaki")
            adjust()
        unadjust()
        up()
        for x in range(0,4):
            empty("khaki")
            adjust()
            empty("saddle brown")
            adjust()
        unadjust()
    up()
    for i in range(0,4):
        pawnB("saddle brown","b")
        adjust()
        pawnB("khaki","b")
        adjust()
    unadjust()
    up()
    rookB("khaki","b")
    adjust()
    knightB("saddle brown","b")
    adjust()
    bishopB("khaki","b")
    adjust()
    queenB("saddle brown","b")
    adjust()
    kingB("khaki","b")
    adjust()
    bishopB("saddle brown","b")
    adjust()
    knightB("khaki","b")
    adjust()
    rookB("saddle brown","b")
    turtle.pu()
    turtle.goto(-175,-175)
    turtle.rt(180)
    turtle.fd(50)
    turtle.rt(180)
    turtle.write("a",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.write("b",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.write("c",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.write("d",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.write("e",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.write("f",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.write("g",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.write("h",False, align="left", font=('Arial', 40, 'normal'))
    adjust()
    turtle.goto(-175,-175)
    turtle.lt(90)
    turtle.fd(5)
    turtle.rt(90)
    turtle.write("1",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    turtle.write("2",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    turtle.write("3",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    turtle.write("4",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    turtle.write("5",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    turtle.write("6",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    turtle.write("7",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    turtle.write("8",False, align="right", font=('Arial', 40, 'normal'))
    turtle.fd(50)
    
def adjust():
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)

def unadjust():
    turtle.lt(90)
    turtle.fd(50)
    turtle.rt(90)

def up():
    turtle.lt(90)
    turtle.fd(350)
    turtle.rt(90)
    turtle.fd(50)

def action(start, finish, piece, team):  #[row][column]
    up=start[0]*50
    across=start[1]*50
    turtle.goto(-175,-175)
    turtle.fd(up)
    turtle.rt(90)
    turtle.fd(across)
    turtle.lt(90)
    a=start[0]%2
    b=start[1]%2
    if a==b:
        empty("saddle brown")
    else:
        empty("khaki")
    up=finish[0]*50
    across=finish[1]*50
    turtle.goto(-175,-175)
    turtle.fd(up)
    turtle.rt(90)
    turtle.fd(across)
    turtle.lt(90)
    a=finish[0]%2
    b=finish[1]%2
    if a==b:
        colour="saddle brown"
    else:
        colour="khaki"
    if piece=="Pa":
        pawnB(colour,team)
    elif piece=="Ro":
        rookB(colour,team)
    elif piece=="Bi":
        bishopB(colour,team)
    elif piece=="Kn":
        knightB(colour,team)
    elif piece=="Qu":
        queenB(colour,team)
    elif piece=="Ki":
        kingB(colour,team)

def passaint(target,adjustment):
    up=(target[0]+adjustment)*50
    across=target[1]*50
    print(target,up,across)
    turtle.goto(-175,-175)
    turtle.fd(up)
    turtle.rt(90)
    turtle.fd(across)
    turtle.lt(90)
    a=target[0]%2
    b=target[1]%2
    if a==b:
        empty("khaki")
    else:
        empty("saddle brown")

def boardPrint(board):
    print("8 ","|",board[7][0],"|",board[7][1],"|",board[7][2],"|",board[7][3],"|",board[7][4],"|",board[7][5],"|",board[7][6],"|",board[7][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print("7 ","|",board[6][0],"|",board[6][1],"|",board[6][2],"|",board[6][3],"|",board[6][4],"|",board[6][5],"|",board[6][6],"|",board[6][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print("6 ","|",board[5][0],"|",board[5][1],"|",board[5][2],"|",board[5][3],"|",board[5][4],"|",board[5][5],"|",board[5][6],"|",board[5][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print("5 ","|",board[4][0],"|",board[4][1],"|",board[4][2],"|",board[4][3],"|",board[4][4],"|",board[4][5],"|",board[4][6],"|",board[4][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print("4 ","|",board[3][0],"|",board[3][1],"|",board[3][2],"|",board[3][3],"|",board[3][4],"|",board[3][5],"|",board[3][6],"|",board[3][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print("3 ","|",board[2][0],"|",board[2][1],"|",board[2][2],"|",board[2][3],"|",board[2][4],"|",board[2][5],"|",board[2][6],"|",board[2][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print("2 ","|",board[1][0],"|",board[1][1],"|",board[1][2],"|",board[1][3],"|",board[1][4],"|",board[1][5],"|",board[1][6],"|",board[1][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print("1 ","|",board[0][0],"|",board[0][1],"|",board[0][2],"|",board[0][3],"|",board[0][4],"|",board[0][5],"|",board[0][6],"|",board[0][7])
    print("---+-----+-----+-----+-----+-----+-----+-----+-----")
    print(":D |  a  |  b  |  c  |  d  |  e  |  f  |  g  |  h")
    
def coordTranslator(coord):
    try:
        valid=False
        for x in range(0,10):
            if coord[1] == str(x):
                valid=True
        if valid==False:
            return [8,8]
        rank=int(coord[1])
        if rank == 0 or rank == 9:
            return [8,8]
        file=coord[0]
        rank=rank-1
        file=fileTranslator(file)
        return [rank,file]
    except ValueError and IndexError:
        return [8,8]

def fileTranslator(file):
    if file=="a":
        return 0
    elif file=="b":
        return 1
    elif file=="c":
        return 2
    elif file=="d":
        return 3
    elif file=="e":
        return 4
    elif file=="f":
        return 5
    elif file=="g":
        return 6
    elif file=="h":
        return 7
    else:
        return 8
    
def playerTurn(team,board):
    global bki, wki, BLC,BSC,WLC,WSC, croissant
    valid=False
    piece=[8,8]
    final=[8,8]
    castle=False
    if team=="w":
        teem="White"
    elif team=="b":
        teem="Black"
    while valid==False:
        vaalid=False
        while vaalid==False:
            piece="None"
            while piece=="None":
                piece=str(turtle.textinput(teem+" to move","Enter the coordinates of the piece you want to move (e.g. e4). O-O for short castle, O-O-O for long castle."))
            if piece!="O-O" and piece!="O-O-O":
                piece=coordTranslator(piece)
                if piece[0]==8 or piece[1] == 8:
                    vaalid=False
                elif board[piece[0]][piece[1]]==(team+"Pa"):
                    vaalid=True
                    move="Pa"
                elif board[piece[0]][piece[1]]==(team+"Ro"):
                    vaalid=True
                    move="Ro"
                elif board[piece[0]][piece[1]]==(team+"Kn"):
                    vaalid=True
                    move="Kn"
                elif board[piece[0]][piece[1]]==(team+"Bi"):
                    vaalid=True
                    move="Bi"
                elif board[piece[0]][piece[1]]==(team+"Qu"):
                    vaalid=True
                    move="Qu"
                elif board[piece[0]][piece[1]]==(team+"Ki"):
                    vaalid=True
                    move="Ki"
                valid=False
                final="None"
                while final=="None":
                    final=str(turtle.textinput(teem+" to move","Choose a place to move to with its coordinates."))
                final=coordTranslator(final)
            elif piece=="O-O" and team=="w" and board[0][5]=="   " and board[0][6]=="   " and WSC==True:
                castle=True
                board[0][6]=board[0][4]
                board[0][4]="   "
                action([0,4], [0,6], "Ki", "w")
                board[0][5]=board[0][7]
                board[0][7]="   "
                action([0,7], [0,5], "Ro", "w")
                valid=True
            elif piece=="O-O-O" and team=="w" and board[0][1]=="   " and board[0][2]=="   " and board[0][3]=="   " and WLC==True:
                castle=True
                board[0][2]=board[0][4]
                board[0][4]="   "
                action([0,4], [0,2], "Ki", "w")
                board[0][3]=board[0][0]
                board[0][0]="   "
                action([0,0], [0,3], "Ro", "w")
                valid=True
            elif piece=="O-O" and team=="b" and board[7][5]=="   " and board[7][6]=="   " and BSC==True:
                castle=True
                board[7][6]=board[7][4]
                board[7][4]="   "
                action([7,4], [7,6], "Ki", "b")
                board[7][5]=board[7][7]
                board[7][7]="   "
                action([7,7], [7,5], "Ro", "b")
                valid=True
            elif piece=="O-O-O" and team=="w" and board[7][1]=="   " and board[7][2]=="   " and board[7][3]=="   " and BLC==True:
                castle=True
                board[7][2]=board[7][4]
                board[7][4]="   "
                action([7,4], [7,2], "Ki", "b")
                board[7][3]=board[7][0]
                board[7][0]="   "
                action([7,0], [7,3], "Ro", "b")
                valid=True
        if final[0]!=8 and final[1]!=8 and piece!="O-O" and piece!="O-O-O":
            if board[final[0]][final[1]][0]!=team:
                if move=="Pa" and team=="w":
                    valid=WPawn(piece,final,board)
                elif move=="Pa" and team=="b":
                    valid=BPawn(piece,final,board)
                elif move=="Ro":
                    valid=Rook(piece,final,board,team)
                elif move=="Kn":
                    valid=Knight(piece,final,board,team)
                elif move=="Bi":
                    valid=Bishop(piece,final,board,team)
                elif move=="Qu":
                    valid=Queen(piece,final,board,team)
                elif move=="Ki":
                    valid=King(piece,final,board,team)
            #test=board
            #test[final[0]][final[1]]=test[piece[0]][piece[1]]
            #board2[piece[0]][piece[1]]="   " #WHY WONT IT WORK
            #print(board)
            #print(test)
            #if team=="w":
            #    valid2=Checker(boardb, wki[0], wki[1], "b") #i hate this
            #elif team=="b":
            #    valid2=Checker(boardb, bki[0], bki[1], "w")
    if move=="Ki" and team=="b":
        bki=final
    elif move=="Ki" and team=="w": #[row][column]
        wki=final
    if piece==[0,0] or final==[0,0]:
        WLC=False
    elif piece==[0,7] or final==[0,7]:
        WSC=False
    elif piece==[7,0] or final==[7,0]:
        BLC=False
    elif piece==[7,7] or final==[7,7]:
        BSC=False
    elif piece==[0,4] or final==[0,4] or ((piece=="O-O-O" or piece=="O-O") and team=="w"):
        WSC=False
        WLC=False
    elif piece==[7,4] or final==[7,4] or ((piece=="O-O-O" or piece=="O-O") and team=="b"):
        BSC=False
        BLC=False
    if piece!="O-O" and piece!="O-O-O":
        board[final[0]][final[1]]=board[piece[0]][piece[1]]
        board[piece[0]][piece[1]]="   "
        action(piece, final, move, team)
    if move=="Pa" and team=="w" and final[0]==7:
        promo=str(promotion())
        board[final[0]][final[1]]=str("w")+promo
        action(piece, final, promo, team)
        print(promo)
    elif move=="Pa" and team=="b" and final[0]==7:
        promo=str(promotion())
        board[final[0]][final[1]]=str("b")+promo
        action(piece, final, promo, team)
    if move=="Pa" and team=="w" and final==croissant:
        board[(final[0]-1)][final[0]]="   "
        passaint(croissant,-1)
    elif move=="Pa" and team=="b" and final==croissant:
        board[(final[0]+1)][final[0]]="   "
        passaint(croissant,1)
    if (not(move=="Pa" and (piece[0]-final[0])==-2 and team=="w")) and (not(move=="Pa" and (piece[0]-final[0])==2 and team=="b")):
        croissant=[8,8]
    return board

def promotion():
    while True:
        choice="None"
        while choice=="None":
            choice=int(turtle.textinput("Promote to:","1:Knight,2:Bishop,3:Rook,4:Queen"))
        if choice==1:
            return "Kn"
        elif choice==2:
            return "Bi"
        elif choice==3:
            return "Ro"
        elif choice==4:
            return "Qu"

def WPawn(piece,final,board):
    global croissant
    if piece[0]==1 and final[0]==3 and final[1]==piece[1] and board[2][final[1]]=="   " and board[3][final[1]]=="   ": #double step
        croissant=[(piece[0]+1),piece[1]]
        return True
    elif (int(piece[0])+1)==final[0] and final[1]==piece[1] and board[final[0]][final[1]]=="   ": #normal move
        return True
    elif (int(piece[0])+1)==final[0] and (piece[1]+1==final[1] or piece[1]-1==final[1]) and (board[final[0]][final[1]][0]=="b" or final==croissant): #capture
        return True
    else:
        return False

def BPawn(piece,final,board):
    global croissant
    if piece[0]==6 and final[0]==4 and final[1]==piece[1] and board[5][final[1]]=="   " and board[4][final[1]]=="   ": #double step
        croissant=[(piece[0]-1),piece[1]]
        return True
    elif (int(piece[0])-1)==final[0] and final[1]==piece[1] and board[final[0]][final[1]]=="   ": #normal move
        return True
    elif (int(piece[0])-1)==final[0] and (piece[1]+1==final[1] or piece[1]-1==final[1]) and (board[final[0]][final[1]][0]=="w" or final==croissant): #capture
        return True
    else:
        return False
   
def Rook(piece,final,board,team):
        if piece[0]==final[0]:
            num=final[1]-piece[1]
            if num>0:
                increment=-1
                skip=False
            elif num<0:
                increment=1
                skip=False
            else:
                skip=True
            if skip==False:
                valid=True
                if board[final[0]][final[1]][0]==team:
                    valid=False
                for i in range((final[1]+increment),piece[1],increment):
                    if board[final[0]][i]!="   ":
                        return False
                return True
        elif piece[1]==final[1]: #a1->a3 -- 0, 0
            num=final[0]-piece[0]  #2,2,0
            if num>0:
                increment=-1   #-1
                skip=False
            elif num<0:
                increment=1
                skip=False
            else:
                skip=True
            if skip==False:
                valid=True
                if board[final[0]][final[1]][0]==team:
                    valid=False
                for i in range((final[0]+increment),piece[0],increment):  #1, 0, -1
                    if board[i][final[1]]!="   ":
                        return False
                return True
        else:
            return False
        
def Knight(piece,final,board,team):
    p1=piece[0]
    p2=piece[1]
    f1=final[0]
    f2=final[1]
    d1=p1-f1
    d2=p2-f2
    if (d1==2 or d1==-2) and (d2==1 or d2==-1):
        return True
    elif (d1==1 or d1==-1) and (d2==2 or d2==-2):
        return True
    else:
        return False

def Bishop(piece,final,board,team): #[row][column]
    p1=piece[0]
    p2=piece[1]
    f1=final[0]
    f2=final[1]
    d1=p1-f1
    d2=p2-f2
    d3=p2-p1
    if d1==d2:
        if d1>0:
            increment=-1
        elif d1<0:
            increment=1
        else:
            return False
        for i in range((p1+increment),(f1),increment):
            if board[i][i+d3]!="   ":
                return False
        return True
    elif (d1*-1)==d2:
        if d1>0:
            increment=-1
        elif d1<0:
            increment=1
        else:
            return False
        x=p2
        for i in range((p1+increment),(f1),increment):
            x=x-increment
            if board[i][x]!="   ":
                return False
        return True
    else:
        return False
def Queen(piece,final,board,team):
    if Bishop(piece,final,board,team)==True or Rook(piece,final,board,team)==True:
        return True
    else:
        return False

def Checker(board,p1,p2,eteam):
    return False
    knight=[[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
    for i in range(0,8):
        try:
            if board[knight[i][0]][knight[i][1]]==eteam+"Kn":
                return False
        except IndexError:
            a=1
    return True
    square1=p1
    empty=True
    while empty==True:
        try:
            square1=square1+1
            if board[square1][p2]=="   ":
                empty=True
            elif board[square1][p2]==eteam+"Qu" or board[square1][p2]==eteam+"Ro":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    square1=p1
    empty=True
    while empty==True:
        try:
            square1=square1-1
            if board[square1][p2]=="   ":
                empty=True
            elif board[square1][p2]==eteam+"Qu" or board[square1][p2]==eteam+"Ro":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    square2=p2
    empty=True
    while empty==True:
        try:
            square2=square2+1
            if board[p1][square2]=="   ":
                empty=True
            elif board[p1][square2]==eteam+"Qu" or board[p1][square2]==eteam+"Ro":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    square2=p2
    empty=True
    while empty==True:
        try:
            square2=square2-1
            if board[p1][square2]=="   ":
                empty=True
            elif board[p1][square2]==eteam+"Qu" or board[p1][square2]==eteam+"Ro":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    square1=p1
    square2=p2
    empty=True
    while empty==True:
        try:
            square1=square1+1
            square2=square2+1
            if board[square1][square2]=="   ":
                empty=True
            elif board[square1][square2]==eteam+"Qu" or board[p1][square2]==eteam+"Bi":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    square1=p1
    square2=p2
    empty=True
    while empty==True:
        try:
            square1=square1-1
            square2=square2+1
            if board[square1][square2]=="   ":
                empty=True
            elif board[square1][square2]==eteam+"Qu" or board[p1][square2]==eteam+"Bi":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    square1=p1
    square2=p2
    empty=True
    while empty==True:
        try:
            square1=square1+1
            square2=square2-1
            if board[square1][square2]=="   ":
                empty=True
            elif board[square1][square2]==eteam+"Qu" or board[p1][square2]==eteam+"Bi":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    square1=p1
    square2=p2
    empty=True
    while empty==True:
        try:
            square1=square1-1
            square2=square2-1
            if board[square1][square2]=="   ":
                empty=True
            elif board[square1][square2]==eteam+"Qu" or board[p1][square2]==eteam+"Bi":
                return False
            else:
                empty=False
        except IndexError:
            empty=False
    return True
                    
def King(piece,final,board,team):
    d1=piece[0]-final[0]
    d2=piece[1]-final[1]
    if d1>=-1 and d1<=1 and d2>=-1 and d2<=1: 
        return True
    else:
        return False

croissant=[8,8]
wki=[0,4]
bki=[7,4]
WSC=True
WLC=True
BSC=True
BLC=True
turtle.screensize(450,450)
turtle.speed(0)
turtle.ht()
turtle.pu()
turtle.goto(-175,-125)
turtle.pd()
turtle.lt(90)
boardBuild()
board=boardSetup()
boardPrint(board)
while True:
    board=playerTurn("w", board)
    boardPrint(board)
    board=playerTurn("b", board)
    boardPrint(board)

