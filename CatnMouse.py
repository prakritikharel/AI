#Prakriti Kharel-- A1
import random
import math
import queue
import heapq
from collections import deque

#maybe use pyplot and map 2d array to grid or figure a way for UI to look nice
#task one: create a 12 by 12 board, an array
#for this, we will first create 2D arrays and intialize it with the val 0
outerloop = 12;
arr  = [0] * outerloop
gamesWon = 0
tMoves = 0

#function that prints the grid
def printfunc ():
    print ("----------------------------------------------------")

    for i in range (outerloop):
        for j in range (outerloop):
            print(arr[i][j], end =' ')
        print()


def cheeseRandom():
    temp = []
    #how many cheese and where
    #amount = random.randint(3,5)
    amount = 3
    # want amount # of cheese # want to figure out h1 and h2 that many times and store it in
    #an array
    for i in range(amount):
        h1 = random.randint(0, 11)
        h2 = random.randint(0, 11)
        arr[h1][h2] = 'H'
        temp.append(h1)
        temp.append(h2)
    return temp

#function that comptues randomly: generate the pos of cat, pos of mouse and the three cheese randomly
def randomly (temp= [], *args ):
    #for the mouse
    m1 = random.randint(0,11)
    m2 = random.randint(0,11)
    arr[m1][m2] = 'M'
    #print(m1, m2)
    #for the cat
    c1 = random.randint(0,11)
    c2 = random.randint(0,11)

    #check to make sure the cat and the mouse don't start in the same pos
    if (c1 == m1 and c2 == m2):
        c1 = random.randint(0, outerloop)
        c2 = random.randint(0, outerloop)
       # print (c1, c2)
    arr[c1][c2] = 'C'
    #for the three cheese , let H represent cheese
    temp[0] = c1;
    temp[1] = c2;
    temp[2] = m1;
    temp[3] = m2;

    return temp


#function that moves the cat
#forgot to check for range
def moveCat(c, c1, c2):
    arr[c1][c2] = 0
    if (c == 'u'):  # case for moving up
        c1 = c1 - 1
        c2 = c2 + 2
    elif (c == 'l'):  # case for moving left
        c1 = c1 - 1
        c2 = c2 - 2
    elif (c == 'd'):  # case for moving down
        c1 = c1 + 1
        c2 = c2 - 2
    elif (c == 'tl'):  # case for moving top left
        c1 = c1 - 2
        c2 = c2 - 1
    elif (c == 'tr'):  # case for moving top right
        c1 = c1 - 2
        c2 = c2 + 1
    elif (c == 'bl'):  # case for moving bottom left
        c1 = c1 + 2
        c2 = c2 - 1
    elif (c == 'br'):  # case for moving bottom right
        c1 = c1 + 2
        c2 = c2 + 1
    else:  # case for moving right
        c1 = c1 + 1
        c2 = c2 + 2
    arr[c1][c2] = 'C'

#function that moves the mouse given which direction to move and where the mouse currently is
def moveMouse(c, m1, m2):
    print("m1, m2 before is ", m1, m2)
    print ("the move for the mouse is ", c)
    arr[m1][m2] = 0
    if (c == 'u'): #case for moving up
        m1 = m1-1
    elif (c == 'l'): #case for moving left
        m2 = m2 -1
    elif (c == 'd'): #case for moving down
        m1 = m1+1
    elif( c == 'tl'): #case for moving top left
        m1 = m1 -1
        m2 = m2 -1
    elif (c =='tr'): #case for moving top right
        m1 = m1 - 1
        m2 = m2 + 1
    elif (c == 'bl'): #case for moving bottom left
        m1 = m1 + 1
        m2 = m2 - 1
    elif (c == 'br'): #case for moving bottom right
        m1 = m1 + 1
        m2 = m2 + 1
    else:               #case for moving right
        m2 = m2 +1

    print("m1 and m2 are ", m1, m2)
    if (arr[m1][m2] == 'H'):
        print ("yum yum yum, cheese eaten at ", m1, m2)
    arr[m1][m2] = 'M'
    pos = [ m1, m2 ]
    return pos

#function to calculate the distance, return an array that is a list of steps that the mouse should take
#to eat all the cheese
#need to still work on calculate distance everytime, instead of all at once so its more acc
def calculateDis(temp = [], *args):
    newArr = [] #stores x coordinate, y coordinate, distance
    distArr = [] # stores distance sorted
    finalArr = [] #stores the coordinates depending on their distance
    charArr = [] #stores a list of chars, the path for all the cheese
    flag = False
    temp1 = []



    m1 = temp[len(temp) - 2] #x coordinate of where the mouse is
    m2 = temp[len(temp)-1] #y coordinate of where the mouse is
    i = 0
    while i < (len(temp) - 2):
        #compute the distance and put it in an array
        distance = math.sqrt(((m1 - temp[i]) ** 2) + ((m2 - temp[i+1]) ** 2)) + .1
        newArr.append(temp[i])
        newArr.append(temp[i + 1])
        for j in range(len(distArr)):
            if (distArr[j] == distance):
                flag = True

        if(flag == False):
            newArr.append(distance)
            distArr.append(distance)
        else:
            newArr.append(distance + 0.00001)
            distArr.append(distance+ 0.00001)
        i = i+2





    distArr.sort() #sort the distance
   # print("leng of distArr is ", len(distArr))
    j = 0
#if 2 cheese same distance take the rightmost, need to deal with that case inside this while loop
 #want to create a new array which consists of coordinates in the order of their distance (to know where to go)
    while j < (len(distArr)):
        temp = newArr.index(distArr[j]) #what index in Newarr, the vlaue of distArr
        finalArr.append(newArr[temp-2])
        finalArr.append(newArr[temp-1])
       # print("index in newArr ", temp)
      #  print ("x coordinate ",newArr[temp - 2])
      #  print("y coordinate ", newArr[temp - 1])
        j += 1


    #now i have the coordinates in order that the mouse needs to get to, now i am going to try to figure out the steps for the mouse to take
    #to get to all the pos



    i = 0
    while i < (len(finalArr)):
        flag = True
        while (flag == True):
            if (m1 == finalArr[i]) and (m2 != finalArr[i + 1]):  # case to move right and left
                if (m2 > finalArr[i + 1]):
                    charArr.append('l')
                    m2 = m2 - 1
                else:
                    charArr.append('r')
                    m2 = m2 + 1
            elif (m2 == finalArr[i + 1] and m1 != finalArr[i]):  # case to move up and down
                if (m1 > finalArr[i]):
                    charArr.append('u')
                    m1 = m1 - 1
                else:
                    charArr.append('d')
                    m1 = m1+1
            else:  # case to move diagonal
                if (m1 > finalArr[i] and m2 > finalArr[i+1]):
                    charArr.append('tl')
                    m1 = m1 -1
                    m2 = m2 - 1
                elif(m1 > finalArr[i] and m2 < finalArr[i+1]):
                    charArr.append('tr')
                    m1 = m1 -1
                    m2 = m2 + 1
                elif (m1 < finalArr[i] and m2 < finalArr[i+1]):
                    charArr.append('br')
                    m1 = m1 + 1
                    m2 = m2 + 1
                else:
                    charArr.append('bl')
                    m1 = m1 + 1
                    m2 = m2 - 1

            if (m1 == finalArr[i] and m2 == finalArr[i+1]):
                i = i+2
                flag = False

    return (charArr)


#first expands the given node ex: if a is given and b and c are its child, then b and c will
#i want it to return a list
def expand(c1, c2): #passed in where the cat currently is
    #first creating a double array
    arr = [0] * 8
    for i in range(8):
        arr[i] = [0] * 2


#quadrant 1
    if (c1 > 1 and c2 > 0):
        arr[0][0] = c1 - 2
        arr[0][1] = c2 - 1
    else:
        arr[0][0] = 'n'
        arr[0][1] = 'n'

    if (c1 > 0 and c2 > 1):
        arr[1][0] = c1 - 1
        arr[1][1] = c2 - 2
    else :
        arr[1][0] = 'n'
        arr[1][1] = 'n'

    #quadrant 2

    if (c1 > 0 and c2 < (outerloop - 2)):
        arr[2][0] = c1 - 1
        arr[2][1] = c2 + 2
    else:
        arr[2][0] = 'n'
        arr[2][1] = 'n'


    if (c1 > 1 and c2 < (outerloop - 1)):
        arr[3][0] = c1 - 2
        arr[3][1] = c2 + 1
    else:
        arr[3][0] = 'n'
        arr[3][1] = 'n'
#quadrant 3
    if (c1 < (outerloop - 2) and c2 > 0):
        arr[4][0] = c1 + 2
        arr[4][1] = c2 - 1
    else:
        arr[4][0] = 'n'
        arr[4][1] = 'n'

    if (c1 < (outerloop - 1) and c2 > 1):
        arr[5][0] = c1 + 1
        arr[5][1] = c2 - 2
    else:
        arr[5][0] = 'n'
        arr[5][1] = 'n'

#quadrant 4
    if (c1 < (outerloop - 2) and c2 < (outerloop - 1)):
        arr[6][0] = c1 + 2
        arr[6][1] = c2 + 1
    else:
        arr[6][0] = 'n'
        arr[6][1] = 'n'

    if (c1 < (outerloop - 1) and c2 < (outerloop - 2)):
        arr[7][0] = c1 + 1
        arr[7][1] = c2 + 2
    else:
        arr[7][0] = 'n'
        arr[7][1] = 'n'

    return arr;
#add the



def bfs(  m1, m2, c1, c2, tempo = [], *args): #given: where the cat initially is
    global tMoves;
    tMoves += len(tempo)
    movesArr = []
    mouseArr = []

    q = queue.Queue()
    q.put([c1,c2])
    temp = [[0] * 2 for k in [0] * outerloop]
    j = 0

    #starting position of the mouse
    temp1 = m1
    temp2 = m2
    flag = 'f'
    #now i want to add all elements to queue
    for i in range(len(tempo)):
        arr[c1][c2] = 0
        temp = expand(c1, c2)
        for l in range(len(temp)):
            if (temp[l] != ['n', 'n']):
                q.put(temp[l])

        #this is b/c i want to do q.get twice at the beginning, to remove the initial, after this i only want to do once
        if (flag == 'f'):
            q.get()
            flag = 't'

        storing = q.get()


        #reset c1 and c2
        c1 = storing[0]
        c2 = storing[1]
        movesArr.append([c1, c2])
        mouseArr.append([temp1, temp2])

        if(arr[c1][c2] == 'M'):
            arr[c1][c2] = 'C'
            printfunc()
            print("the mouse has been caught in", (i + tMoves), "moves after the mouse won", (gamesWon -1), "rounds")
            print("the # of nodes that were searched is ", ((i + tMoves) * 8), "nodes")
            print("the moves taken by the  cat this round are ", movesArr)
            print("the moves taken by the  mouse  this round are ", mouseArr)

            break
        arr[c1][c2] = 'C'


        store = moveMouse(tempo[j], temp1, temp2)
        j = j+1
        temp1 = store[0]  # the current mouse positions, return value of mouseMoves
        temp2 = store[1]

        checking = len(tempo) - 1
        printfunc()

        if (i  == checking):
            print("The mouse has won this round")
            main()




def dfs(  m1, m2, c1, c2, tempo = [], *args): #given: where the cat initially is
    global tMoves;
    tMoves += len(tempo)

    q = deque()
    q.append([c1,c2])
    mouseArr = []
    movesArr = []
    temp = [[0] * 2 for k in [0] * outerloop]
    j = 0

    #starting position of the mouse
    temp1 = m1
    temp2 = m2
    flag = 'f'
    #now i want to add all elements to queue
    for i in range(len(tempo)):


        arr[c1][c2] = 0
        temp = expand(c1, c2)
        for l in range(len(temp)):
            if (temp[l] != ['n', 'n']):
                q.append(temp[l])

        #this is b/c i want to do q.get twice at the beginning, to remove the initial, after this i only want to do once
        if (flag == 'f'):
            q.pop()
            flag = 't'

        storing = q.pop()


        #reset c1 and c2
        c1 = storing[0]
        c2 = storing[1]
        movesArr.append([c1, c2])
        mouseArr.append([temp1, temp2])


        if(arr[c1][c2] == 'M'):
            arr[c1][c2] = 'C'
            printfunc()
            print("the mouse has been caught in",(j +  tMoves) , " total moves. The mouse won", (gamesWon -1), "rounds")
           # print("the # of nodes that were searched is ", ((j + tMoves) * 8), "nodes")
            print("the moves taken by the  cat this round are ", movesArr)
            print("the moves taken by the  mouse  this round are ", mouseArr)
            break
        arr[c1][c2] = 'C'



        store = moveMouse(tempo[j], temp1, temp2)
        j = j+1
        temp1 = store[0]  # the current mouse positions, return value of mouseMoves
        temp2 = store[1]

        checking = len(tempo) - 1
        printfunc()

        if (i  == checking):
            print("The mouse has won this round")
            main()


#for a star
def disCalc(g, temp = [], *args):
    newArr = [] #stores x coordinate, y coordinate, distance
    distArr = [] # stores distance sorted
    finalArr = [] #stores the coordinates depending on their distance
    m1 = temp[len(temp) - 2] #x coordinate of where the mouse is
    m2 = temp[len(temp)-1] #y coordinate of where the mouse is
    i = 0



    while i < (len(temp) - 2):
        #compute the distance and put it in an array
        distance = math.sqrt(((m1 - temp[i]) ** 2) + ((m2 - temp[i+1]) ** 2)) + .1
        newArr.append(temp[i])
        newArr.append(temp[i + 1])
        newArr.append(distance)
        distArr.append(distance)
        i = i+2


    while i < (len(distArr)):
       distArr[i] += g

    distArr.sort() #sort the distance
   # print("leng of distArr is ", len(distArr))
    j = 0
 #want to create a new array which consists of coordinates in the order of their distance (to know where to go)
    while j < (len(distArr)):
        temp = newArr.index(distArr[j]) #what index in Newarr, the vlaue of distArr
        finalArr.append(newArr[temp-2])
        finalArr.append(newArr[temp-1])
       # print("index in newArr ", temp)
      #  print ("x coordinate ",newArr[temp - 2])
      #  print("y coordinate ", newArr[temp - 1])
        j += 1


    return finalArr

#so friggen fast
#the purpose of heuristic is to reduce the statespace
def heuristic1(m1, m2, c1, c2,tempo = [], *args ):
    #calculate the distance of all and put it in the priority queue according to shortest distance
    #the shortest distance is the one that will be opened first
    #get where the cat is expand and get the distance
    #f(n)  = g(n) + h(n)
    #g(n) = cost so far to reach n
    # h(n) = shortest distance
    #expand where the cat currently is
    #send that in calculate dis, lets see what we get
    temp = [[0] * 2 for k in [0] * outerloop]
  #  movesArr = [[0] * 2 for k in [0] * outerloop]
    movesArr = []
    mouseArr = []
    g = 0

    final = []
   # singleArr = []
    currentCat = c1
    currentCat1 = c2
    currentMouse = m1
    currentMouse1 = m2
    counter = 0


    for j in range(len(tempo)):
        singleArr = []

        g += 1
        #first expand where the cat currently is
        arr[currentCat][currentCat1] = 0

        temp = expand(currentCat, currentCat1)
        for i in range (len(temp)):
            # append it to a single array
            if (temp[i] != ['n', 'n']):
                singleArr.append(temp[i][0])
                singleArr.append(temp[i][1])

        #now append where the mouse currently is to the single array
        singleArr.append(currentMouse)
        singleArr.append(currentMouse1)

        final = disCalc(g, singleArr)  # pass in the coordinates of the staatespace + the coordinate of the mouse, it returns an array  sorted
        currentCat = final[0]
        currentCat1 = final[1]

        movesArr.append([currentCat, currentCat1])
        mouseArr.append([currentMouse, currentMouse1])



        if(arr[currentCat][currentCat1] == 'M'):
            j = j+ 1
            arr[currentCat][currentCat1] = 'C'
            printfunc()
            print("the mouse has been caught in", j, "moves after the mouse won ", (gamesWon -1) , "many rounds")
            print("the # of nodes that were searched is ", (j *8) , "nodes" )
            print ("the moves taken by the  cat are ", movesArr)
            print ("the moves taken by the  mouse are ", mouseArr)
            break

        arr[currentCat][currentCat1] = 'C'
        store = moveMouse(tempo[j], currentMouse, currentMouse1)
        j = j + 1
        currentMouse = store[0]  # the current mouse positions, return value of mouseMoves
        currentMouse1 = store[1]

        checking = len(tempo) - 1
        printfunc()
        if (i == checking):
            print("THE MOUSE HAS WON THIS ROUND after ", (j+ 1) , "rounds ")
            main()



#quadrant idea: dfs on a reduced search space
def heuristic2(m1, m2, c1, c2, tempo=[], *args):
    q = deque()
    q.append([c1, c2])
    temp = [[0] * 2 for k in [0] * outerloop]
    quadrant =  [[0] * 2 for k in [0] * outerloop]
    j = 0
    movesArr = []
    mouseArr = []

    # starting position of the mouse
    temp1 = m1
    temp2 = m2
    flag = 'f'
    printfunc()
    # now i want to add all elements to queue
    for i in range(len(tempo)):
        arr[c1][c2] = 0
        temp = expand(c1, c2)
        '''
        
        1 |  2
        3 | 4
       25 34   38 27
              46
        65 54    67 58 
        
        
        '''

        #reset quadrant
        quadrant = []
        #compare x values of c1 and temp1
        if( c1 >= temp1): #only look at quadrant 1 and  quadrant 2
            if (c2 <= temp2): #quadrant 2
                quadrant.append(temp[2])
                quadrant.append(temp[3])
            else: #quadrant 1
                quadrant.append(temp[0])
                quadrant.append(temp[1])
        else:
            if (c2 >= temp2): #quadrant 3
                quadrant.append(temp[4])
                quadrant.append(temp[5])
            else: #quadrant 4
                quadrant.append(temp[6])
                quadrant.append(temp[7])



        #here i only want to append 2 nodes in the right quadrant
        for l in range(2):
            if (quadrant[l] != ['n', 'n']):
                q.append(quadrant[l])
                #deal with the case when its both nn, but that should never be the case

        # this is b/c i want to do q.get twice at the beginning, to remove the initial, after this i only want to do once
        if (flag == 'f'):
            q.pop()
            flag = 't'

        storing = q.pop()

        # reset c1 and c2
        c1 = storing[0]
        c2 = storing[1]

        movesArr.append([c1, c2])
        mouseArr.append([temp1, temp2])

        if (arr[c1][c2] == 'M'):
            i = i+ 1
            arr[c1][c2] = 'C'
            printfunc()
            print("the mouse has been caught in", j, "moves after the mouse won ", (gamesWon -1) , "many rounds")
            print("the # of nodes that were searched is ", (i * 8), "nodes")
            print("the moves taken by the  cat are ", movesArr)
            print("the moves taken by the  mouse are ", mouseArr)

            break
        arr[c1][c2] = 'C'
        print("-------------------------------------------------")
        store = moveMouse(tempo[j], temp1, temp2)
        j = j + 1
        temp1 = store[0]  # the current mouse positions, return value of mouseMoves
        temp2 = store[1]

        checking = len(tempo) - 1
        printfunc()

        if (i == checking):
            print("The mouse has won this round")
            main()


#a mixture of 1 and 2 : calculate the distance of the quadrant that it is valid
def heuristic3(m1, m2, c1, c2, tempo=[], *args):

    temp = [[0] * 2 for k in [0] * outerloop]
    quadrant =  [[0] * 2 for k in [0] * outerloop]
    g = 0

    final = []
    movesArr = []
    mouseArr = []
    currentCat = c1
    currentCat1 = c2
    currentMouse = m1
    currentMouse1 = m2

    for j in range(len(tempo)):
        singleArr = []

        g += 1
        # first expand where the cat currently is
        arr[currentCat][currentCat1] = 0
        temp = expand(currentCat, currentCat1)


        '''

                1 |  2
                3 | 4
               25 34   38 27
                      46
                65 54    67 58 


                '''

        # reset quadrant
        quadrant = []
        # compare x values of c1 and temp1



#dealing with edge cases
        if (currentCat1 ==  0 and currentCat < 5):
            quadrant.append(temp[6])
            quadrant.append(temp[7])
        elif (currentCat1 == 0 and currentCat > 5):
            quadrant.append(temp[2])
            quadrant.append(temp[3])
        elif (currentCat1 == 11 and currentCat > 5):
            quadrant.append(temp[0])
            quadrant.append(temp[1])
        elif (currentCat1 == 11 and currentCat < 5):
            quadrant.append(temp[4])
            quadrant.append(temp[5])

        elif (currentCat == 11 and currentCat1 < 5):
            quadrant.append(temp[0])
            quadrant.append(temp[1])
        elif (currentCat == 11 and currentCat1 > 5):
            quadrant.append(temp[2])
            quadrant.append(temp[3])
        elif (currentCat == 0 and currentCat1 > 5):
            quadrant.append(temp[4])
            quadrant.append(temp[5])
        elif (currentCat == 0 and currentCat1 < 5):
            quadrant.append(temp[6])
            quadrant.append(temp[7])


        else:
            if (currentCat >= currentMouse):  # only look at quadrant 1 and  quadrant 2
                if (currentCat1 <= currentMouse1):  # quadrant 2
                    quadrant.append(temp[2])
                    quadrant.append(temp[3])
                else:  # quadrant 1
                    quadrant.append(temp[0])
                    quadrant.append(temp[1])
            else:
                if (currentCat1 >= currentMouse1):  # quadrant 3

                    quadrant.append(temp[4])
                    quadrant.append(temp[5])
                else:  # quadrant 4

                    quadrant.append(temp[6])
                    quadrant.append(temp[7])

        for i in range(len(quadrant)):
            # append it to a single array, but i only want to append the ones in the right quadrant
            if (quadrant[i] != ['n', 'n']):
                singleArr.append(quadrant[i][0])
                singleArr.append(quadrant[i][1])


        # now append where the mouse currently is to the single array
        singleArr.append(currentMouse)
        singleArr.append(currentMouse1)


        final = disCalc(g, singleArr)  # pass in the coordinates of the staatespace + the coordinate of the mouse, it returns an array  sorted
        currentCat = final[0]
        currentCat1 = final[1]

        movesArr.append([currentCat, currentCat1])
        mouseArr.append([currentMouse, currentMouse1])

        if (arr[currentCat][currentCat1] == 'M'):
            j = j + 1
            arr[currentCat][currentCat1] = 'C'
            printfunc()
            print("the mouse has been caught in", j, "moves after the mouse won ", (gamesWon -1) , "many rounds")
            print("the # of nodes that were searched is ", (j * 8), "nodes")
            print("the moves taken by the  cat are ", movesArr)
            print("the moves taken by the  mouse are ", mouseArr)
            break

        arr[currentCat][currentCat1] = 'C'

        store = moveMouse(tempo[j], currentMouse, currentMouse1)
        j = j + 1
        currentMouse = store[0]  # the current mouse positions, return value of mouseMoves
        currentMouse1 = store[1]
        checking = len(tempo) - 1

        printfunc()
        if (i == checking):
            print("The mouse has won this round")
            main()


#want to try to put everything inside main for good coding practise
def main():


    #initialize the array
     for i in range(outerloop):
        arr[i] = [0] * outerloop

     global gamesWon;
     gamesWon += 1





     c1= c2= h1 =h2 = m1=  m2= 0
     temp = [c1, c2, h1, h2, m1, m2]
     mouseMoves = []

     up = 'u'
     left = 'l'
     top_left = 'tl'
     top_right = 'tr'
     down = 'd'
     bottom_left = 'bl'
     bottom_right = 'br'
     right = 'r'

     temp = randomly(temp)
     c1 = temp[0]
     c2 = temp[1]
     m1 = temp[2]
     m2 = temp[3]
     s = cheeseRandom()



     #moveMouse(bottom_left, m1, m2)
    # moveCat(up, c1, c2)
     printfunc()
     s.append(m1)
     s.append(m2)
     mouseMoves = calculateDis(s) #pass in the coordinates of the cheese + the coordinate of the mouse, it returns an array of chars for all mouse moves
     #bfs(m1, m2, c1, c2, mouseMoves)
     #dfs(m1, m2, c1, c2, mouseMoves)
     #heuristic1(m1, m2, c1, c2, mouseMoves)
     #heuristic2(m1, m2, c1, c2, mouseMoves)
     heuristic3(m1, m2, c1, c2, mouseMoves)



main()


