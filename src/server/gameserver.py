import math
import random
class gameserver:
    def __init__(self, connected):
        # the info in each connected is: [x,y,size,xvel,yvel,food,garbage]
        self.connected = connected
        #self.globalData 
        self.size = 800
        # food: [x,y,foodorgarbage]
        self.food = set()
        self.foodNum = 10
        self.obstacles = set()
        self.obstacleNum = 5
        # init obstacles 
        while len(self.obstacles) < self.obstacleNum:
            self.obstacles.add((random.randint(0,self.size),random.randint(0,self.size)))
        print(self.obstacles)
        

    def update(self):
        print('updating')
        while len(self.food) < self.foodNum:
            self.food.add((random.randint(0,self.size),random.randint(0,self.size),random.randint(0,10)>3))
        print(self.food)

    def getData(self, user):
        # first index is characters, second is food, third is obstacles
        # the first index of characters is the users info
        data = [[]]
        for i in self.connected:
            if i['info'] != None:
                dist = math.sqrt((i['info'][0]-user[0])**2 +(i['info'][1]-user[1])**2)
                if dist < i['info'][2] + user[2] and (i['info'][0] != user[0] and i['info'][1] != user[1]):
                    print('collided')
                    #make it so they bump off each other.
                if dist < 100:
                    data[0].append(i['info'])
        for i in self.food: 
            dist = math.sqrt((i[0]-user[0])**2 +(i[1]-user[1])**2)
            if dist < 10:
                data[1].append(i)
            if dist < 100:
                data[1].append(i)
                data[1][-1][2]=True
        for i in self.obstacles: 
            dist = math.sqrt((i[0]-user[0])**2 +(i[1]-user[1])**2)
            if dist < 100:
                data[2].append(i)
        return data

def main():
    print('---gameserver main---')
    

if __name__ == '__main__':
    main()
