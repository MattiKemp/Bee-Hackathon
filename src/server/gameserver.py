import math
import random
class gameserver:
    def __init__(self, connected):
        # the info in each connected is: [x,y,size,xvel,yvel,food,garbage]
        self.connected = connected
        #self.globalData 
        self.size = 3000
        # food: [x,y,foodorgarbage]
        self.food = set()
        self.foodNum = 100
        self.obstacles = set()
        self.obstacleNum = 20
        # init obstacles 
        while len(self.obstacles) < self.obstacleNum:
            self.obstacles.add((random.randint(0,self.size),random.randint(0,self.size)))
        print(self.obstacles)
        self.trashpiles = set()
        self.trashpileNum = 10
        while len(self.trashpiles) < self.trashpileNum:
            self.trashpiles.add((random.randint(0,self.size),random.randint(0,self.size)))
        self.update()

    def update(self):
        print('updating')
        while len(self.food) < self.foodNum:
            self.food.add((random.randint(0,self.size),random.randint(0,self.size),random.randint(0,10)>3))
        toRemove = []
        for i in self.food:
            for j in self.connected:
                if j['info'] != None:
                    dist = math.sqrt((i[0]-j['info'][0])**2 +(i[1]-j['info'][1])**2)
                    #print(dist)
                    if dist < 40:
                        #print(j['info'])
                        toRemove.append(i)
                        #j['info'][5] += 1
                        print('touched')
                        #print(j['info'])
        for i in toRemove:
            self.food.remove(i)

    def getData(self, user):
        # first index is characters, second is food, third is obstacles
        # the first index of characters is the users info
        data = [[],[],[],[]]
        died = False
        killed = False
        for i in self.connected:
            if i['info'] != None:
                dist = math.sqrt((i['info'][0]-user[0])**2 +(i['info'][1]-user[1])**2)
                if dist < i['info'][2]*10 + user[2]*10 and (i['info'] != user):
                    print('collided')
                    # you die
                    if (i['info'][2]==3 or i['info'][2] == 5) and user[2] < i['info'][2]:
                        died = True
                        break
                    # they die and you get some of their score and some of their garbage
                    elif (user[2]==3 or user[2] == 5) and user[2] > i['info'][2]:
                        user[-1] += int(i['info'][-1]*.25)
                        user[-2] += int(i['info'][-2]*.5)
                        i['info'] = [-1,-1,-1,-1,-1,-1,-1]
                        killed = True
                    #make it so they bump off each other? 
                elif dist > 10 and dist < 800:
                    data[0].append(i['info'])
        for i in self.food: 
            dist = math.sqrt((i[0]-user[0])**2 +(i[1]-user[1])**2)
            # how close you need to be to tell if something is food or trash
            if dist < 50 + 25*user[2]:
                data[1].append(i)
            # view distance, everything is set to food.
            elif dist < 800:
                data[1].append(list(i))
                data[1][-1][2]=True
        for i in self.obstacles: 
            dist = math.sqrt((i[0]-user[0])**2 +(i[1]-user[1])**2)
            if dist < 800:
                data[2].append(i)
        if killed:
            data[-1].append(user)
        elif not died:
            data[-1].append(user)
            data[-1][0][5] = 0
            data[-1][0][6] = 0
        else:
            data[-1].append([-1,-1,-1,-1,-1,-1,-1])
        return data

def main():
    print('---gameserver main---')
    

if __name__ == '__main__':
    main()
