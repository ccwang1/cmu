import eventBasedAnimation
import random
import math
from Tkinter import *

class Start(object):
    def __init__(self,x,y):
        self.x=x*40+20
        self.y=y*40+20
        self.r=20
        self.image = PhotoImage(file="Start.gif")

    def __repr__(self):
        return 'Start'

    def onDraw(self,canvas):
        canvas.create_image(self.x,self.y,image=self.image)   

    def containsPoint(self,x,y):
        if self.x-self.r<=x<self.x+self.r and self.y-self.r<=y<self.y+self.r:
            return True

class Path(object):
    def __init__(self,x,y):
        self.x=x*40+20
        self.y=y*40+20
        self.r=20
        self.image = PhotoImage(file="Path.gif")

    def __repr__(self):
        return 'Path'

    def onDraw(self,canvas):
        canvas.create_image(self.x,self.y,image=self.image)   

    def containsPoint(self,x,y):
        if self.x-self.r<=x<self.x+self.r and self.y-self.r<=y<self.y+self.r:
            return True

class End(object):
    def __init__(self,x,y):
        self.x=x*40+20
        self.y=y*40+20
        self.r=20
        self.color='pink'
        self.image = PhotoImage(file="End.gif")


    def __repr__(self):
        return 'End'

    def onDraw(self,canvas):
        canvas.create_image(self.x,self.y,image=self.image)  

    def containsPoint(self,x,y):
        if self.x-self.r<=x<self.x+self.r and self.y-self.r<=y<self.y+self.r:
            return True

class Basictower(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.r=20
        self.damage=2
        self.color='grey'
        self.attackspeed=10
        self.range=100
        self.diagonal=math.sqrt(self.range**2/2)
        self.cost=25
        self.type='normal'
        self.sell=self.cost/2
        self.costdamage=15
        self.costrange=15
        self.costattackspeed=15
        self.rangeupgrade=10
        self.damageupgrade=1
        self.attackspeedupgrade=1
        self.upgradeincrement=20
        self.image = PhotoImage(file="Basictower.gif")
        self.piercehealth=1

    def __repr__(self):
        return 'Basic Tower'

    def __eq__(self,other):
        return type(self)==type(other) and self.x==other.x and self.y==other.y

    def containsPoint(self,x,y):
        size=40
        i=x/size
        j=x/size
        return self.locations[i][j]==None

    def givePosition(self):
        return self.x,self.y

    def onDraw(self,canvas):
        canvas.create_image(self.x,self.y,image=self.image)    

    def showRange(self,canvas):
        canvas.create_oval(self.x-self.range,self.y-self.range,
            self.x+self.range,self.y+self.range,fill=None, outline='black')

    def inRange(self,x,y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5    #taken from dots
        return (d <= self.range)

class Freezetower(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.r=20
        self.damage=1
        self.color='blue'
        self.attackspeed=20
        self.range=125
        self.diagonal=math.sqrt(self.range**2/2)
        self.cost=40
        self.type='freeze'
        self.sell=self.cost/2
        self.costdamage=15
        self.costrange=15
        self.costattackspeed=15
        self.rangeupgrade=20
        self.damageupgrade=1
        self.attackspeedupgrade=1
        self.upgradeincrement=20
        self.image = PhotoImage(file="Freezetower.gif")
        self.piercehealth=1

    def __repr__(self):
        return 'Freeze Tower'

    def __eq__(self,other):
        return type(self)==type(other) and self.x==other.x and self.y==other.y

    def containsPoint(self,x,y):
        size=40
        i=x/size
        j=x/size
        return self.locations[i][j]==None

    def givePosition(self):
        return self.x,self.y

    def onDraw(self,canvas):
        canvas.create_image(self.x,self.y,image=self.image)   


    def showRange(self,canvas):
        canvas.create_oval(self.x-self.range,self.y-self.range,
            self.x+self.range,self.y+self.range,fill=None, outline='black')

    def inRange(self,x,y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5    #taken from dots
        return (d <= self.range)

class Piercetower(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.r=20
        self.damage=2
        self.color='purple'
        self.attackspeed=20
        self.range=125
        self.diagonal=math.sqrt(self.range**2/2)
        self.cost=70
        self.type='pierce'
        self.sell=self.cost/2
        self.costdamage=15
        self.costrange=15
        self.costattackspeed=15
        self.rangeupgrade=20
        self.damageupgrade=1
        self.attackspeedupgrade=1
        self.upgradeincrement=20
        self.piercehealth=3
        self.image = PhotoImage(file="Piercetower.gif")

    def __repr__(self):
        return 'Pierce Tower'

    def __eq__(self,other):
        return type(self)==type(other) and self.x==other.x and self.y==other.y

    def containsPoint(self,x,y):
        size=40
        i=x/size
        j=x/size
        return self.locations[i][j]==None

    def givePosition(self):
        return self.x,self.y

    def onDraw(self,canvas):
        canvas.create_image(self.x,self.y,image=self.image)   


    def showRange(self,canvas):
        canvas.create_oval(self.x-self.range,self.y-self.range,
            self.x+self.range,self.y+self.range,fill=None, outline='black')

    def inRange(self,x,y):
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5    #taken from dots
        return (d <= self.range)

class Bullet(object):
    def __init__(self,x1,y1,x2,y2,bullettype='normal',damage=1,piercehealth=1):
        self.towerx1=x1
        self.towery1=y1
        self.x=x1
        self.y=y1
        self.r=3
        self.speed=13
        self.unit=math.sqrt((x2-x1)**2+(y2-y1)**2)
        if self.unit==0:
            self.unit=1
        self.dx=(x2-x1)/self.unit*2
        self.dy=(y2-y1)/self.unit*2
        self.attackspeed=1
        self.damage=damage
        self.slow=1
        self.type=bullettype
        self.piercehealth=piercehealth
        if bullettype=='normal':
            self.color='dark grey'
        if bullettype=='freeze':
            self.color='light blue' 
        if bullettype=='pierce':
            self.color='purple'

    def onMove(self):
        self.x+=self.dx*self.speed
        self.y+=self.dy*self.speed

    def onDraw(self,canvas):
        canvas.create_oval(self.x-self.r,self.y-self.r,self.x+self.r,
            self.y+self.r,fill=self.color)

    def givePosition(self):
        return self.x,self.y

    def giveZ(self):
        return int(self.x**2+self.y**2)**.5

    def onCollision(self, x, y,r):      #taken from dot demo
        return r>((self.x - x)**2 + (self.y - y)**2)**0.5

    def isOffScreen(self):
        if -30<self.x<630 and -30<self.y<630:
            return False
        return True

class Monster(object):
    def __init__(self,x,y,path,wave=0):
        self.x=x
        self.y=y
        self.r=17
        self.speed=2.5
        self.totalhealth=10+6*wave
        self.health=10+6*wave
        self.pathcount=0
        self.path=path
        self.directionnum=0
        self.barh=self.r+3
        self.amountwalked=0
        self.bounty=3
        self.image=PhotoImage(file='mup1.gif')
        self.upimg = PhotoImage(file="mup1.gif")
        self.downimg = PhotoImage(file="mdown1.gif")
        self.leftimg = PhotoImage(file="mleft1.gif")
        self.rightimg = PhotoImage(file="mright1.gif")

    def __repr__(self):
        return 'Monster'

    def onMove(self,direction):
        if direction=='up':
            self.image=self.upimg
            self.y-=self.speed
        if direction=='down':
            self.image=self.downimg
            self.y+=self.speed
        if direction=='left':
            self.image=self.leftimg
            self.x-=self.speed
        if direction=='right':
            self.image=self.rightimg
            self.x+=self.speed
        self.amountwalked+=self.speed

    def onDraw(self,canvas):
        if self.speed!=2.5:
            hpcolor='light blue'    #change hp color is frozen
        else:
            hpcolor='red'
        canvas.create_image(self.x,self.y,image=self.image)   
        canvas.create_rectangle(self.x-self.r,  #displays hp
            self.y-self.barh,
            self.x+self.r,
            self.y-self.r,
            fill=None) 
        canvas.create_rectangle(self.x-self.r,  #displays hp
            self.y-self.barh,
            self.x-self.r+((self.health*1.0/self.totalhealth)*(2*self.r)),
            self.y-self.r,
            fill=hpcolor) 

    def givePosition(self):
        return self.x,self.y,self.r

    def isOffScreen(self):
        if -30<self.x<630 and -30<self.y<630:
            return False
        return True

    def isDead(self):
        if self.health<=0:
            return True
        return False

    def atEnd(self,x,y):
        if self.x==x and self.y==y:
            return True

class StrongMonster(object):
    def __init__(self,x,y,path,wave):
        self.x=x
        self.y=y
        self.r=18
        self.speed=2
        self.totalhealth=20+10*wave
        self.health=20+10*wave
        self.pathcount=0
        self.path=path
        self.directionnum=0
        self.barh=self.r+3
        self.amountwalked=0
        self.bounty=5
        self.image=PhotoImage(file='mup2.gif')
        self.upimg = PhotoImage(file="mup2.gif")
        self.downimg = PhotoImage(file="mdown2.gif")
        self.leftimg = PhotoImage(file="mleft2.gif")
        self.rightimg = PhotoImage(file="mright2.gif")

    def __repr__(self):
        return 'StrongMonster'

    def onMove(self,direction):
        if direction=='up':
            self.image=self.upimg
            self.y-=self.speed
        if direction=='down':
            self.image=self.downimg
            self.y+=self.speed
        if direction=='left':
            self.image=self.leftimg
            self.x-=self.speed
        if direction=='right':
            self.image=self.rightimg
            self.x+=self.speed
        self.amountwalked+=self.speed

    def onDraw(self,canvas):
        if self.speed!=2:
            hpcolor='light blue'    #change hp color is frozen
        else:
            hpcolor='red'
        canvas.create_image(self.x,self.y,image=self.image)   
        canvas.create_rectangle(self.x-self.r,  #displays hp
            self.y-self.barh,
            self.x+self.r,
            self.y-self.r,
            fill=None) 
        canvas.create_rectangle(self.x-self.r,  #displays hp
            self.y-self.barh,
            self.x-self.r+((self.health*1.0/self.totalhealth)*(2*self.r)),
            self.y-self.r,
            fill=hpcolor) 

    def givePosition(self):
        return self.x,self.y,self.r

    def isOffScreen(self):
        if -30<self.x<630 and -30<self.y<630:
            return False
        return True

    def isDead(self):
        if self.health<=0:
            return True
        return False

    def atEnd(self,x,y):
        if self.x==x and self.y==y:
            return True

class Boss(object):
    def __init__(self,x,y,path,wave=0):
        self.x=x
        self.y=y
        self.r=20
        self.speed=1
        self.totalhealth=80+35*(wave)
        self.health=80+35*wave
        self.pathcount=0
        self.path=path
        self.directionnum=0
        self.barh=self.r+3
        self.amountwalked=0
        self.bounty=20
        self.image=PhotoImage(file='bossup.gif')
        self.upimg = PhotoImage(file="bossup.gif")
        self.downimg = PhotoImage(file="bossdown.gif")
        self.leftimg = PhotoImage(file="bossleft.gif")
        self.rightimg = PhotoImage(file="bossright.gif")

    def __repr__(self):
        return 'Boss'

    def onMove(self,direction):
        if direction=='up':
            self.image=self.upimg
            self.y-=self.speed
        if direction=='down':
            self.image=self.downimg
            self.y+=self.speed
        if direction=='left':
            self.image=self.leftimg
            self.x-=self.speed
        if direction=='right':
            self.image=self.rightimg
            self.x+=self.speed
        self.amountwalked+=self.speed

    def onDraw(self,canvas):
        hpcolor='red'       #boss cant be frozen
        canvas.create_image(self.x,self.y,image=self.image)   
        canvas.create_rectangle(self.x-self.r,  #displays hp
            self.y-self.barh,
            self.x+self.r,
            self.y-self.r,
            fill=None) 
        canvas.create_rectangle(self.x-self.r,  #displays hp
            self.y-self.barh,
            self.x-self.r+((self.health*1.0/self.totalhealth)*(2*self.r)),
            self.y-self.r,
            fill=hpcolor) 

    def givePosition(self):
        return self.x,self.y,self.r

    def isOffScreen(self):
        if -30<self.x<630 and -30<self.y<630:
            return False
        return True

    def isDead(self):
        if self.health<=0:
            return True
        return False

    def atEnd(self,x,y):
        if self.x==x and self.y==y:
            return True

class game(eventBasedAnimation.Animation):
    def onInit(self):
        self.timerDelay = 30
        self.basictowers = []
        self.freezetowers = []
        self.locations=[]
        self.money=100
        self.bullets=[]
        self.monsters=[]
        self.gameStart=False
        self.gameOver=False
        self.shoots=10
        self.attackspeed=0
        self.lives=10
        self.timer=1
        self.spawning=False
        self.wave=0
        self.nummonsters=15
        self.pathcount=0
        self.showinfo=False
        self.infoindex=0
        for i in range(0,15):                   #eliminates aliasing
            self.locations.append([])           #creates the locations
            for j in range(0,15):               #which is 15x15 None board
                self.locations[-1].append(None) #
        self.placeMonster=False #test
        self.placeBasic=False    #test
        self.placeFreeze=False
        self.send=[[1]*15,
                    [1]*10+[2]*5,
                    [1]*5+[2]*10,
                    [2]*15,
                    [2]*5+[3]]        
        self.showRange=False
        self.build=False
        self.towermovex,self.towermovey=0,0
        self.showbasictower,showx,showy=False,300,300
        self.showfreezetower=False
        self.placePierce=False
        self.showpiercetower=False
        self.towers=[]
        self.basicrange=100
        self.freezerange=125
        self.piercerange=125
        self.background=PhotoImage(file='Background.gif')
        self.splash=PhotoImage(file='splashscreen.gif')
        self.snake = PhotoImage(file="mdown1.gif")
        self.basictowerimage = PhotoImage(file="Basictower.gif")
        self.freezetowerimage = PhotoImage(file="Freezetower.gif")
        self.piercetowerimage=PhotoImage(file='Piercetower.gif')
        self.file=open('map.txt','r')       #opens map
        for i in self.file:
            self.map=eval(i)
        self.file=open('defaultmap.txt','r')    #opens default map
        for i in self.file:
            self.defaultmap=eval(i)
        self.file.close()
        self.instructions=False
        self.mapEditor=False
        self.newmap=[]
        self.initmap=True
        self.surround=False
        self.savesuccess=False
        self.maperror=False
        self.resetsuccess=False

    def buildmap(self,tuplelist):   #creates map from tuple list
        if len(tuplelist)>0:
            (starttuplex,starttuppley)=tuplelist[0]
            self.locations[starttuppley][starttuplex]=Start(starttuplex,
                starttuppley)
            self.startx=starttuplex
            self.starty=starttuppley
        if len(tuplelist)>1:
            (endtuplex,endtupley)=tuplelist[-1]
            self.locations[endtupley][endtuplex]=End(endtuplex,endtupley)
            for coord in tuplelist[1:-1]:
                x=coord[0]
                y=coord[1]
                self.locations[y][x]=Path(x,y)

    def mapEditMouse(self,event):
        self.savesuccess=False
        center=700
        margin=85
        self.maperror=False
        self.resetsuccess=False
        if 0<event.x<600 and 0<event.y<600:
            i,j=event.x/40,event.y/40   #floors it
            if len(self.newmap)==0: #to make start
                self.newmap.append((event.x/40,event.y/40))
            if len(self.newmap)==1: #to make end
                if i!=0 and repr(self.locations[j][i-1])=='Start':
                    self.newmap.append((event.x/40,event.y/40))
                elif i!=14 and repr(self.locations[j][i+1])=='Start':
                    self.newmap.append((event.x/40,event.y/40))
                elif j!=0 and repr(self.locations[j-1][i])=='Start':
                    self.newmap.append((event.x/40,event.y/40))
                elif j!=14 and repr(self.locations[j+1][i])=='Start':
                    self.newmap.append((event.x/40,event.y/40))
            if len(self.newmap)>1: #to make path
                if self.checkSurround(event,i,j):
                    if i!=0 and repr(self.locations[j][i-1])=='End':
                        self.newmap.append((event.x/40,event.y/40))
                    elif i!=14 and repr(self.locations[j][i+1])=='End':
                        self.newmap.append((event.x/40,event.y/40))
                    elif j!=0 and repr(self.locations[j-1][i])=='End':
                        self.newmap.append((event.x/40,event.y/40))
                    elif j!=14 and repr(self.locations[j+1][i])=='End':
                        self.newmap.append((event.x/40,event.y/40))
            if repr(self.locations[j][i])=='End':
                self.newmap.pop()
                self.locations[j][i]=None
            self.buildmap(self.newmap)
        if center-margin<event.x<center+margin and 270<event.y<320: #reset map
            self.map=open('map.txt','w')
            self.map.write(str(self.defaultmap))
            self.map.close()
            self.resetsuccess=True
        if center-margin<event.x<center+margin and 400<event.y<450: #use map
            if len(self.newmap)>2:
                self.mapEditor=False
                self.gameStart=True
                self.initMap()
            else:
                self.maperror=True
        if center-margin<event.x<center+margin and 470<event.y<520: #save map
            if len(self.newmap)>2:
                self.map=open('map.txt','w')
                self.map.write(str(self.newmap))
                self.map.close()
                self.savesuccess=True
            else:
                self.maperror=True
        if center-margin<event.x<center+margin and 540<event.y<590: #back
            self.onInit()


    def checkSurround(self,event,i,j):      #checks if only 1 path bounds it
        numbound=4
        if i==0:    #accounts for edges
            numbound-=1
        if i==14:
            numbound-=1
        if j==0:
            numbound-=1
        if j==14:
            numbound-=1
        if i!=0 and type(self.locations[j][i-1])==type(None):
            numbound-=1
        if i!=14 and type(self.locations[j][i+1])==type(None):
            numbound-=1
        if j!=0 and type(self.locations[j-1][i])==type(None):
            numbound-=1
        if j!=14 and type(self.locations[j+1][i])==type(None):
            numbound-=1
        if numbound==1:
            return True
        if numbound!=1:
            return False

    def mapEditDraw(self,canvas):
        center=700
        margin=85
        size=40
        mapheight=600
        canvas.create_image(300,300,image=self.background)
        canvas.create_rectangle(600,0,800,640,fill='light yellow', 
            outline='')
        canvas.create_rectangle(0,600,800,640,fill='light yellow', 
            outline='')
        for col in (self.locations):
            for spot in col:
                if type(spot)!=type(None):
                    spot.onDraw(canvas)
        for i in range(0,600/size+1):
            canvas.create_line(0,size*i,mapheight,size*i)
            canvas.create_line(size*i,0,size*i,mapheight)
        canvas.create_line(mapheight,0,mapheight,self.height-40)
        canvas.create_text(center,100,text='Map Editor',
            font=('Courier',30,''))
        canvas.create_text(center,130,text='Edit the map',
            font=('Courier',13,''))
        canvas.create_text(center,145,text='to your liking!',
            font=('Courier',13,''))
        canvas.create_text(center,175,text='Click anywhere to start',
            font=('Courier',13,''))
        canvas.create_text(center,190,text='your new map. If you',
            font=('Courier',13,''))
        canvas.create_text(center,205,text='make a mistake, click',
            font=('Courier',13,''))
        canvas.create_text(center,220,text='over it to redraw it!',
            font=('Courier',13,''))
        canvas.create_rectangle(center-margin,270,center+margin,320,
            fill='pink')
        canvas.create_rectangle(center-margin,400,center+margin,450,
            fill='light green')
        canvas.create_rectangle(center-margin,470,center+margin,520,
            fill='light green')
        canvas.create_rectangle(center-margin,540,center+margin,590,
            fill='light green')
        canvas.create_text(center,425,text='Use Map',font=('Courier',18,''))
        canvas.create_text(center,495,text='Save Map',font=('Courier',18,''))
        canvas.create_text(center,565,text='Back',font=('Courier',18,''))
        canvas.create_text(center,295,text='Reset Default',
            font=('Courier',18,''))
        if self.resetsuccess and self.maperror==False:
            canvas.create_text(center,360,text='Map Reset',
                font=('Courier',14,''))
        if self.savesuccess and self.maperror==False:
            canvas.create_text(center,360,text='Map Saved',
                font=('Courier',14,''))
        if self.maperror:
            canvas.create_text(center,350,text='Please add more',
                font=('Courier',14,''))
            canvas.create_text(center,365,text='pieces to the map!',
                font=('Courier',14,''))

    def onMouse(self,event):
        center=700
        margin=85        
        if self.gameOver:
            self.mouseGameOver(event)
        if self.gameStart==False:
            if self.instructions:
                if 670<event.x<770 and 580<event.y<630:
                    self.instructions=False
            if self.mapEditor:
                self.mapEditMouse(event)
            else:
                self.splashMouse(event)
        if self.gameStart==True and not self.gameOver:
            if self.initmap:
                self.initMap()
                self.initmap=False
            self.mouseGameStart(event)
            self.mouseSpawnWave(event)

    def initMap(self):  #creates map
        if self.newmap==[]:
            if self.map==[]:
                self.newmap=self.defaultmap
            else:       #if newmap is empty, use default
                self.newmap=self.map        
        self.buildmap(self.newmap)
        self.startx,self.starty=self.newmap[0][0],self.newmap[0][1]
        self.end=End(self.newmap[-1][0],self.newmap[-1][1])
        self.monsterpath=self.solve()
        self.initmap=False

    def mouseSpawnWave(self,event):
        if 615<event.x<785 and 530<event.y<590:
            if self.spawning==False and len(self.monsters)==0:
                self.spawning=True
                self.wave+=1
                self.timer=0

    def mouseGameStart(self,event):
        center=700
        margin=85
        floorx,floory=event.x/40*40,event.y/40*40
        if 0<event.x<40 and 600<event.y<640:    #if click on 1
            if self.money>=25:
                self.placeFreeze=False
                self.build=True
                self.placeBasic=True    #test
                self.showinfo=False
                self.placePierce=False
        if 40<event.x<80 and 600<event.y<640:   #if click on 2
            if self.money>=40:
                self.placeBasic=False
                self.build=True
                self.placeFreeze=True
                self.showinfo=False
                self.placePierce=False
        if 80<event.x<120 and 600<event.y<640:   #if click on 3
            if self.money>=40:
                self.placePierce=True
                self.build=True
                self.placeFreeze=False
                self.placeBasic=False
                self.showinfo=False
        if 0<=floorx<600 and 0<=floory<600: #if click on board
            spot=self.locations[floory/40][floorx/40]
            if type(spot)==type(None):
                if self.placeBasic: #places basic tower
                    self.locations[floory/40][floorx/40]=Basictower(floorx+20,
                        floory+20)
                    self.towers.append(Basictower(floorx+20, floory+20))
                    self.money-=self.towers[self.towers.index(
                        Basictower(floorx+20,floory+20))].cost
                    self.placeBasic=False
                    self.showbasictower=False
                elif self.placeFreeze:  #places freeze tower
                    self.locations[floory/40][floorx/40]=Freezetower(
                        floorx+20,floory+20)
                    self.towers.append(Freezetower(floorx+20, floory+20))
                    self.money-=self.towers[self.towers.index(
                        Freezetower(floorx+20,floory+20))].cost
                    self.placeFreeze=False
                    self.showfreezetower=False
                elif self.placePierce:  #places freeze tower
                    self.locations[floory/40][floorx/40]=Piercetower(
                        floorx+20,floory+20)
                    self.towers.append(Piercetower(floorx+20, floory+20))
                    self.money-=self.towers[self.towers.index(
                        Piercetower(floorx+20,floory+20))].cost
                    self.placePierce=False
                    self.showpiercetower=False
            # elif type(spot)==Path:  #checks if its a path
            #     if spot.containsPoint(floorx+20,floory+20):
            #         pass
            elif type(spot)==Basictower or type(
                spot)==Freezetower or type(spot)==Piercetower: 
            #for displaying info of tower
                if type(spot)==Basictower:
                    self.infoindex=self.towers.index(Basictower(floorx+20,
                        floory+20))
                elif type(spot)==Freezetower:
                    self.infoindex=self.towers.index(Freezetower(floorx+20,
                        floory+20))
                elif type(spot)==Piercetower:
                    self.infoindex=self.towers.index(Piercetower(floorx+20,
                        floory+20))
                self.showinfo=True
            if not (type(spot)==Basictower or type(
                spot)==Freezetower or type(spot)==Piercetower):
                self.showinfo=False
            self.build=False
            self.placeBasic,self.showbasictower=False,False
            self.placeFreeze,self.showfreezetower=False,False
            self.placePierce,self.showpiercetower=False,False
        if self.showinfo==True:     #for the info of tower
            tower=self.towers[self.infoindex]
            if center-margin<event.x<center+margin and 312<event.y<355: 
            #damage
                if self.money>=tower.costdamage:
                    self.money-=tower.costdamage
                    tower.cost+=tower.costdamage
                    tower.costdamage+=tower.upgradeincrement
                    tower.damage+=tower.damageupgrade
            elif center-margin<event.x<center+margin and 362<event.y<405: 
            #atk speed
                if self.money>=tower.costattackspeed and tower.attackspeed!=1:
                    self.money-=tower.costattackspeed
                    tower.cost+=tower.costattackspeed
                    tower.costattackspeed+=tower.upgradeincrement
                    tower.attackspeed-=tower.attackspeedupgrade
            elif center-margin<event.x<center+margin and 412<event.y<455: 
            #range
                if self.money>=tower.costrange:
                    self.money-=tower.costrange
                    tower.cost+=tower.costrange
                    tower.costrange+=tower.upgradeincrement
                    tower.range+=tower.rangeupgrade
            elif center-margin<event.x<center+margin and 462<event.y<505: 
            #sell
                self.money+=tower.cost/2
                self.towers.remove(tower)
                for i in range(len(self.locations)):
                    for j in range(len(self.locations[i])):
                        if self.locations[i][j]==tower:
                            self.locations[i][j]=None
                self.showinfo=False

    def buildInfo(self,canvas):
        center=700
        margin=85
        if self.build==True:
            if self.placeBasic:
                tower=Basictower(0,0)
                canvas.create_rectangle(center-margin,150,center+margin,300,
                fill='light yellow')  #info
                canvas.create_text(center,170,
                    text=repr(tower),font=('Courier',20,'bold'))
                canvas.create_text(center,200,
                    text='Damage: '+str(tower.damage),font='Courier')
                canvas.create_text(center,225,
                    text='Attack Speed: '+str(tower.attackspeed),
                    font='Courier')
                canvas.create_text(center,250,
                    text='Range: '+str(tower.range),font='Courier')
                canvas.create_text(center,275,
                    text='Worth: '+str(tower.cost),font='Courier')
                self.basicInfo(canvas)
            elif self.placeFreeze:
                tower=Freezetower(0,0)
                canvas.create_rectangle(center-margin,150,center+margin,300,
                fill='light yellow')  #inf
                canvas.create_text(center,170,
                    text=repr(tower),font=('Courier',20,'bold'))
                canvas.create_text(center,200,
                    text='Damage: '+str(tower.damage),font='Courier')
                canvas.create_text(center,225,
                    text='Attack Speed: '+str(tower.attackspeed),
                    font='Courier')
                canvas.create_text(center,250,
                    text='Range: '+str(tower.range),font='Courier')
                canvas.create_text(center,275,
                    text='Worth: '+str(tower.cost),font='Courier')
                self.freezeInfo(canvas)
            elif self.placePierce:
                tower=Piercetower(0,0)
                canvas.create_rectangle(center-margin,150,center+margin,300,
                fill='light yellow')  #inf
                canvas.create_text(center,170,
                    text=repr(tower),font=('Courier',20,'bold'))
                canvas.create_text(center,200,
                    text='Damage: '+str(tower.damage),font='Courier')
                canvas.create_text(center,225,
                    text='Attack Speed: '+str(tower.attackspeed),
                    font='Courier')
                canvas.create_text(center,250,
                    text='Range: '+str(tower.range),font='Courier')
                canvas.create_text(center,275,
                    text='Worth: '+str(tower.cost),font='Courier')
                self.pierceInfo(canvas)

    def basicInfo(self,canvas):
        center=700
        margin=85
        canvas.create_rectangle(center-margin,325,center+margin,500,
        fill='light green')  #inf
        canvas.create_text(center,340,
            text='The Basic Tower has',font=('Courier',11))
        canvas.create_text(center,355,
            text='deals lots of damage',font=('Courier',11))
        canvas.create_text(center,370,
            text='and has a fast attack',font=('Courier',11))
        canvas.create_text(center,385,
            text='speed but it has a',font=('Courier',11))
        canvas.create_text(center,400,
            text='short range. It is',font=('Courier',11))
        canvas.create_text(center,415,
            text='the most basic ',font=('Courier',11))
        canvas.create_text(center,430,
            text='defensive tower.',font=('Courier',11))

    def freezeInfo(self,canvas):
        center=700
        margin=85
        canvas.create_rectangle(center-margin,325,center+margin,500,
        fill='light green')  #inf
        canvas.create_text(center,340,text='The Freeze Tower has',
            font=('Courier',11))
        canvas.create_text(center,355,text='a crippling attack',
            font=('Courier',11))
        canvas.create_text(center,370,text='which permanently ',
            font=('Courier',11))
        canvas.create_text(center,385,text='slows any monster it',
            font=('Courier',11))
        canvas.create_text(center,400,text='hits by 50%. Though ',
            font=('Courier',11))
        canvas.create_text(center,415,text='it may be expensive,',
            font=('Courier',11))
        canvas.create_text(center,430,text='this tactical tower ',
            font=('Courier',11))
        canvas.create_text(center,445,text='can strengthen your',
            font=('Courier',11))
        canvas.create_text(center,460,text='defense significantly.',
            font=('Courier',11))

    def pierceInfo(self,canvas):
        center=700
        margin=85
        canvas.create_rectangle(center-margin,325,center+margin,500,
        fill='light green')  #inf
        canvas.create_text(center,340,text='The Pierce Tower has',
            font=('Courier',11))
        canvas.create_text(center,355,text='a special type of ',
            font=('Courier',11))
        canvas.create_text(center,370,text='bullet which is capable',
            font=('Courier',11))
        canvas.create_text(center,385,text='of piercing through',
            font=('Courier',11))
        canvas.create_text(center,400,text='three enemies before',
            font=('Courier',11))
        canvas.create_text(center,415,text='it gets destroyed.',
            font=('Courier',11))
        canvas.create_text(center,430,text='It can strengthen your',
            font=('Courier',11))
        canvas.create_text(center,445,text='defense immensely in',
            font=('Courier',11))
        canvas.create_text(center,460,text='the right location.',
            font=('Courier',11))

    def showInfo(self,canvas):
        if self.showinfo==True:
            center=700
            margin=85
            tower=self.towers[self.infoindex]
            canvas.create_rectangle(center-margin,150,center+margin,300,
            fill='light yellow')  #info
            canvas.create_rectangle(center-margin,312,center+margin,355,
            fill='light yellow')  #damage
            canvas.create_rectangle(center-margin,362,center+margin,405,
            fill='light yellow')  #attack speed
            canvas.create_rectangle(center-margin,412,center+margin,455,
            fill='light yellow')  #range
            canvas.create_rectangle(center-margin,462,center+margin,505,
            fill='pink')  #sell
            canvas.create_text(center,170,text=repr(tower),
                font=('',20,'bold'))
            canvas.create_text(center,200,
                text='Damage: '+str(tower.damage))
            canvas.create_text(center,225,
                text='Attack Speed: '+str(tower.attackspeed))
            canvas.create_text(center,250,
                text='Range: '+str(tower.range))
            canvas.create_text(center,275,
                text='Worth: '+str(tower.cost))
            canvas.create_text(center,325,
                text='Upgrade Damage: '+str(tower.costdamage),
                font=('',13,'bold'))
            canvas.create_text(center,325+20,
                text=str(tower.damage)+'->'+str(tower.damage+
                    tower.damageupgrade))
            if tower.attackspeed==1:    #max attack speed
                canvas.create_text(center,375,
                    text='Upgrade Attack Speed',font=('',13,'bold'))
                canvas.create_text(center,375+20,
                    text='Maxed')
            if tower.attackspeed!=1:
                canvas.create_text(center,375,
                    text='Upgrade Attack Speed: '+str(tower.costattackspeed),
                    font=('',13,'bold'))
                canvas.create_text(center,375+20,
                    text=str(tower.attackspeed)+'->'+str(tower.attackspeed-
                        tower.attackspeedupgrade))
            canvas.create_text(center,425,
                text='Upgrade Range: '+str(tower.costrange),
                font=('',13,'bold'))
            canvas.create_text(center,425+20,
                text=str(tower.range)+'->'+str(
                    tower.range+tower.rangeupgrade))
            canvas.create_text(center,475,
                text='Sell Tower',font=('',13,'bold'))
            canvas.create_text(center,475+20,
                text=str(tower.cost/2))
            tower.showRange(canvas)
        #basictower
        canvas.create_image(23,self.height-20,image=self.basictowerimage)
        canvas.create_text(23,self.height-20,
            text='1',fill='red',font=('',18,'bold'))
        #freezetower
        canvas.create_image(63,self.height-20,image=self.freezetowerimage)
        canvas.create_text(63,self.height-20,
            text='2',fill='red',font=('',18,'bold'))
        #piercetower
        canvas.create_image(103,self.height-20,image=self.piercetowerimage)
        canvas.create_text(103,self.height-20,
            text='3',fill='red',font=('',18,'bold'))


    def Range(self,canvas):
        if self.showRange:
            for tower in self.towers:
                tower.showRange(canvas)

    def onMouseMove(self,event):    #creates tower to follow mouse
        if self.gameStart and not self.gameOver:
            if 0<=event.x<600 and 0<=event.y<600:   #on board
                floorx,floory=event.x/40*40,event.y/40*40   
                #floors to lowest multiple of 40
                self.oldlocationy,self.oldlocationx=floory/40,floorx/40
                if self.placeBasic:
                    spot=self.locations[floory/40][floorx/40]
                    self.showbasictower=True
                    self.showx=event.x
                    self.showy=event.y
                    self.showfreezetower=False
                    self.showpiercetower=False
                if self.placeFreeze:
                    spot=self.locations[floory/40][floorx/40]
                    self.showfreezetower=True
                    self.showx=event.x
                    self.showy=event.y
                    self.showbasictower=False
                    self.showpiercetower=False
                if self.placePierce:
                    spot=self.locations[floory/40][floorx/40]
                    self.showfreezetower=False
                    self.showx=event.x
                    self.showy=event.y
                    self.showbasictower=False
                    self.showpiercetower=True
    def solve(self):
        path=[]
        for i in range(0,(len(self.locations))):
            for j in range(0,(len(self.locations[i]))):
                if type(self.locations[i][j])==Start:
                    x,y=i,j
        for i in range(0,len(self.locations)*len(self.locations[0])):
            if x!=len(self.locations)-1 and (type(
                self.locations[x+1][y])==Path or type(
                self.locations[x+1][y])==End):
                #checks if first move is legal or if it is end
                if path==[] or path[-1]!='up':      #checks last move
                    path.append('down')     #adds next move is down
                    x+=1        #changes the x value to current spot
            if x!= 0 and (type(self.locations[x-1][y]) == Path or type(
                self.locations[x-1][y]) == End):
                if path==[] or path[-1]!='down':
                    path.append('up')
                    x-=1
            if y!=len(self.locations[x])-1 and (type(
                self.locations[x][y+1]) == Path or type(
                self.locations[x][y+1]) == End):
                if path==[] or path[-1]!='left':
                    path.append('right')
                    y+=1
            if y!=0 and (type(self.locations[x][y-1]) == Path or type(
                self.locations[x][y-1]) == End):
                if path==[] or path[-1]!='right':   #checks last move
                    path.append('left')
                    y-=1
            if type(self.locations[x][y])==End:    #if it is end, end the loop
                return path
        return False

    def startMonsters(self):
        if self.timer%100==0:
            if self.timer<=100*(len(self.send[(self.wave-1)%5])):
                if self.send[(self.wave-1)%5][(self.timer-100)/100]==1:  #weak
                    self.monsters.append(Monster(self.startx*40+20,
                        self.starty*40+20,self.monsterpath,self.wave/2))
                if self.send[(self.wave-1)%5][(self.timer-100)/100]==2:  #med
                    self.monsters.append(StrongMonster(self.startx*40+20,
                        self.starty*40+20,self.monsterpath,self.wave/2))
                if self.send[(self.wave-1)%5][(self.timer-100)/100]==3:  #boss
                    self.monsters.append(Boss(self.startx*40+20,
                        self.starty*40+20,self.monsterpath,self.wave/2))
        if self.timer>=100*(len(self.send[(self.wave-1)%5])):
            if self.monsters==[]:
                self.spawning=False

    def movebullet(self):
        for bullet in self.bullets:     #keep moving bullets if no monsters
            bullet.onMove()

    def hitbullet(self):
        for monster in self.monsters:
            (monsterx,monstery,monsterr)=monster.givePosition()
            for bullet in self.bullets:
                if bullet.isOffScreen():
                    self.bullets.remove(bullet)
                if bullet.onCollision(monsterx,monstery,monsterr):
                    monster.health-=bullet.damage
                    if bullet.type=='freeze':
                        if repr(monster)=='Monster':
                            monster.speed=1.25
                        if repr(monster)=='StrongMonster':
                            monster.speed=1
                    bullet.piercehealth-=1
                    if bullet.piercehealth<=0:
                        self.bullets.remove(bullet)
            if monster.isDead():
                self.money+=monster.bounty
                self.monsters.remove(monster)

    def shootbullet(self):
        shoot=False
        for tower in self.towers:
            if self.attackspeed%tower.attackspeed==0:
                closest=tower.range   #furthest point
                closemx,closemy=None,None
                for monster in self.monsters:
                    tx,ty=tower.givePosition()
                    mx,my,mr=monster.givePosition()
                    if math.sqrt((tx-mx)**2+(ty-my)**2)<=closest:
                        closest=math.sqrt((tx-mx)**2+(ty-my)**2)
                        closemx,closemy=mx,my
                if closest<tower.range:
                    if closemx != None and closemy!=None:
                        self.bullets.append(Bullet(tower.x,tower.y,closemx,
                        closemy,tower.type,tower.damage,tower.piercehealth))

    def moveMonster(self):
        for monster in self.monsters:
            if monster.directionnum<len(monster.path):
                if monster.path[monster.directionnum]=='up':
                    monster.onMove('up')
                elif monster.path[monster.directionnum]=='down':
                    monster.onMove('down')
                elif monster.path[monster.directionnum]=='left':
                    monster.onMove('left')
                elif monster.path[monster.directionnum]=='right':
                    monster.onMove('right')
                if monster.isOffScreen():
                    self.monsters.remove(monster)
                monster.pathcount+=monster.speed
                if monster.pathcount%40==0:
                    monster.pathcount=0
                    monster.directionnum+=1
            if monster.atEnd(self.end.x,self.end.y):
                self.monsters.remove(monster)
                self.lives-=1
                if self.lives==0:
                    self.gameOver=True

    def onStep(self):
        if self.gameStart==True:
            self.timer+=5
            self.attackspeed+=1
            self.shootbullet()
            self.movebullet()
            self.hitbullet()
            self.startMonsters()
            self.moveMonster()

    def splashMouse(self,event):
        center=self.width/2
        margin=150
        if center-margin<event.x<center+margin and 300<event.y<350:
            self.gameStart=True
        if center-margin<event.x<center+margin and 375<event.y<425:
            self.instructions=True
        if center-margin<event.x<center+margin and 450<event.y<500:
            self.mapEditor=True

    def drawInstructions(self,canvas):
        center=self.width/2
        canvas.create_image(center,self.height/2,image=self.splash)
        canvas.create_text(center,300,text='Your castle is under siege \
by giant snakes escaping the volcano!',font=('Courier',15))
        canvas.create_text(center,325,text='Your job is to protect your \
castle from the onslaught of snakes',font=('Courier',15))
        canvas.create_text(center,350,text='with your array of different \
towers.',font=('Courier',15))
        canvas.create_text(center,375,text='Press R to show the range of \
your towers',font=('Courier',15))
        canvas.create_text(center,400,text='Press Space to send the next \
wave',font=('Courier',15))
        canvas.create_text(center,450,text='The basic tower is your most \
general tower used to defend against the enemies',
         font=('Courier',15))
        canvas.create_text(center,475,text='The freeze tower can be used \
to slow enemies and enhance your defense',font=('Courier',15))
        canvas.create_text(center,500,text='The pierce tower can be used \
to hit three enemies at once',font=('Courier',15))
        canvas.create_rectangle(670,580,770,630,fill='light yellow')
        canvas.create_text(720,605,text='Back',font=('Courier',25))

    def drawSplash(self,canvas):
        center=self.width/2
        margin=150
        canvas.create_image(center,self.height/2,image=self.splash)
        canvas.create_image(center,250,image=self.snake)
        canvas.create_rectangle(center-margin,300,center+margin,350,
            fill = 'light yellow')
        canvas.create_text(center,325,text='Play',font=('Courier',25,'bold'))
        canvas.create_rectangle(center-margin,375,center+margin,425,
            fill = 'light yellow')
        canvas.create_text(center,400,text='Instructions',
            font=('Courier',25,'bold'))
        canvas.create_rectangle(center-margin,450,center+margin,500,
            fill = 'light yellow')
        canvas.create_text(center,475,text='Map Editor',
            font=('Courier',25,'bold'))

    def drawGameOver(self,canvas):
        center=self.width/2
        margin=150
        canvas.create_text(center,200,text='Game Over',fill='red4',
            font=('Courier',80,'bold'))
        canvas.create_text(center,280,text='You failed to protect \
your castle!',font=('Courier',25,'bold'))
        canvas.create_text(center,320,text='The snakes have invaded \
it!',font=('Courier',25,'bold'))
        canvas.create_rectangle(center-margin,375,center+margin,425,
            fill = 'light yellow')
        canvas.create_text(center,400,text='Quit',font=('Courier',25,'bold'))

    def mouseGameOver(self,event):
        center=self.width/2
        margin=150
        if center-margin<event.x<center+margin and 375<event.y<425:
            self.onInit()
            event.x=0
            event.y=0

    def onDraw(self, canvas):
        size=40
        mapheight=600
        if self.gameStart==False:
            if self.instructions==True:
                self.drawInstructions(canvas)
            elif self.mapEditor:
                self.mapEditDraw(canvas)
            else:
                self.drawSplash(canvas)
        if self.gameStart==True:
            canvas.create_image(300,300,image=self.background)
            canvas.create_rectangle(600,0,800,640,fill='light grey',
                outline='')
            canvas.create_rectangle(0,600,800,640,fill='light grey',
                outline='')
            for col in self.locations:
                for spot in col:
                    if type(spot)!=type(None):
                        spot.onDraw(canvas)
            if self.build:
                for i in range(0,600/size+1):
                    canvas.create_line(0,size*i,mapheight,size*i)
                    canvas.create_line(size*i,0,size*i,mapheight)
            canvas.create_line(mapheight,0,mapheight,self.height)
            for bullet in self.bullets:
                bullet.onDraw(canvas)
            for monster in reversed(self.monsters):
                monster.onDraw(canvas)
            self.Range(canvas)
            if self.showbasictower:
                canvas.create_image(self.showx,self.showy,
                    image=self.basictowerimage)
                canvas.create_oval(self.showx-self.basicrange,
                    self.showy-self.basicrange,
                    self.showx+self.basicrange,self.showy+self.basicrange,
                    fill=None, outline='black')
            elif self.showfreezetower:
                canvas.create_image(self.showx,self.showy,
                    image=self.freezetowerimage)
                canvas.create_oval(self.showx-self.freezerange,
                    self.showy-self.freezerange,
                    self.showx+self.freezerange,self.showy+self.freezerange,
                    fill=None, outline='black')
            elif self.showpiercetower:
                canvas.create_image(self.showx,self.showy,
                    image=self.piercetowerimage)
                canvas.create_oval(self.showx-self.piercerange,
                    self.showy-self.piercerange,
                    self.showx+self.piercerange,self.showy+self.piercerange,
                    fill=None, outline='black')
            canvas.create_text(700,30,text='Money: '+str(self.money),
                font=('Courier',17))
            canvas.create_text(700,60,text='Lives: '+str(self.lives),
                font=('Courier',17))
            canvas.create_text(700,90,text='Wave: '+str(self.wave),
                font=('Courier',17))
            if self.spawning :
                canvas.create_rectangle(615,530,785,590,fill='red')
                canvas.create_text(700,(530+590)/2,text='Spawn Wave',
                    font=('Courier',22))
            if not self.spawning:
                canvas.create_rectangle(615,530,785,590,fill='green')
                canvas.create_text(700,(530+590)/2,text='Spawn Wave',
                    font=('Courier',22))
            self.showInfo(canvas)
            self.buildInfo(canvas)
        if self.gameOver:
            self.drawGameOver(canvas)

    def onKey(self,event):
        if self.gameStart==True and self.gameOver==False:
            if event.keysym=='Up':
                self.money+=50000
            if event.keysym=='1':    #place tower
                if self.money>=25:
                    self.placeFreeze=False
                    self.build=True
                    self.placeBasic=True    #test
                    self.showinfo=False
                    self.placePierce=False
            if event.keysym=='2':
                if self.money>=40:
                    self.placeBasic=False
                    self.build=True
                    self.placeFreeze=True
                    self.showinfo=False
                    self.placePierce=False
            if event.keysym=='3':
                if self.money>=40:
                    self.placeBasic=False
                    self.build=True
                    self.placeFreeze=False
                    self.placePierce=True
                    self.showinfo=False
            if event.keysym=='Escape':
                self.placeBasic=False
                self.build=False
                self.placeFreeze=False
                self.showinfo=False
                self.showbasictower=False
                self.showfreezetower=False
                self.placePierce=False
                self.showpiercetower=False
            if event.keysym=='r':
                if self.showRange==True:
                    self.showRange=False
                else:
                    self.showRange=True
            if event.keysym=='space':
                if self.spawning==False and len(self.monsters)==0:
                    self.spawning=True
                    self.wave+=1
                    self.timer=0

def Game(width=800, height=640):  #wrapper
    game(width,height,windowTitle='Snake Tower Defense').run()

Game()