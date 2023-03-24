import subprocess
import time
import random

# A script for sending input to minimized tibia window (Linux)
#
# Change winName accordingly to your character
# Localize local map and mini map windows' corners by xdotool getmouselocation
# Run script
#
# At the bottom there is list of tasks to be completed while script runs.
# Input values should be probably randomized in time (waitRand >> 0)  
#
#                           xdotool getmouselocation
#TIBIA SQM GRID: 15 x 11  (n=15, m=11)		(CENTER x=8, y=6)
#center of SQM of index n (for x-es): SQMn = x0 + (n-1)dx + dx/2		( l/n = dx = SQM's width)
#getmouselocation UPPER LEFT CORNER (x0, y0)  LOWER RIGHT CORNER (xE, yE)		( xE-x0 = l, yE-y0 = h)

#LOCAL MAP COORDINATES:
x0 = 116
y0 = 71
xE = 1037
yE = 745

l = xE-x0
h = yE-y0
n = 15
m = 11
movex = 8 #for centering coordinates at character
movey = 6 #for centering coordinates at character
dx = l/n 
dy = h/m   

#MINI MAP COORDINATES        when minimap corners' coordinates = x:1148 y:68 (NW)  x:1257 y:177 (SE)
XDx = 1225
XDy = 116
DBx = 1154
DBy = 131

winName = "Tibia - Goshnar"

winSearch = subprocess.run(["xdotool", "search", "--name", winName], capture_output=True, text=True)
winFound = winSearch.stdout
winTibiaID = winFound
print('Tibia WinID:' + str(winFound) + 'Botting in progress...')

def randwait(const, rand): #input in ms, output in s
    time.sleep((const + random.randrange(rand))/1000)
    #print((const + random.randrange(rand))/1000)

# clickSQM(0,0) clicks in the middle (at your character), clickSQM(-7,-5) is upper left corner
def clickSQM(x, y, button, waitTime, waitRand, repeat):
    for i in range (repeat):
        SQMxRand = int(random.randrange(-int(dx/5), int(dx/5), 2))
        SQMyRand = int(random.randrange(-int(dy/5), int(dy/5), 2))
        SQMxCoord = x0 + (movex + x-1)*dx + dx/2 + SQMxRand
        SQMyCoord = y0 + (movey - y-1)*dy + dy/2 + SQMyRand   # -y, now coordinates are normal
        subprocess.call( ["xdotool", "mousemove", str(SQMxCoord), str(SQMyCoord), "click", "--clearmodifiers", "--window", str(winTibiaID), str(button), "mousemove", "restore"] )
        randwait(waitTime,waitRand)

def clickCoord(x, y, waitTime, waitRand, repeat):
    for i in range (repeat):
        subprocess.call( ["xdotool", "mousemove", str(x), str(y), "click", "--clearmodifiers", "--window", str(winTibiaID), "1", "mousemove", "restore"] ) # 1 = LMB
        randwait(waitTime,waitRand)
        #print("clickCoord waitend")

def type(hotkey):
    subprocess.call( ["xdotool", "type", "--window", str(winTibiaID), str(hotkey)] )

def key(hotkey):
    subprocess.call( ["xdotool", "key", "--window", str(winTibiaID), str(hotkey)] )

def attack(repeat, eachstack, waitTime, waitRand):
    for i in range (repeat):
        for j in range (eachstack):
            type(0)
            randwait(100,100)
        randwait(waitTime, waitRand)

def eat():
    type(2)
    randwait(500,1000)

def heal(repeat):
    for i in range (repeat):
        type(1)
        randwait(500,1000)

def ring():
    type(3)
    randwait(500,1000)
    
def rune():
    type(4)
    randwait(500,1000)
            
def goUp(repeat):
    for i in range (repeat):
        key('Up')
        randwait(100,100)

#functions preview:
# attack(repeat, eachstack, waitTime, waitRand)
# clickCoord(x, y, waitTime, waitRand, repeat)
# clickSQM(x, y, button, waitTime, waitRand, repeat)     # 1=LMB, 3=RMB

i = 0
while True:
    i = i+1
    start = time.time()
    attack(1 ,3, 100, 100)
    clickSQM(1, 2, 3, 450, 100, 3)
    heal(1)
    randwait(500,1000)
    attack(1 ,3, 200, 100)
    ring()
    #(X > D)
    clickCoord(XDx, XDy, 7000, 500, 1)
    #(D)
    clickSQM(2, -1, 3, 350, 50, 1)
    randwait(350,200)
    clickSQM(0, 1, 1, 250, 100, 2)
    attack(45 ,3, 1500, 400)
    # (D > X)
    # ...
    end = time.time()
    print( "loop (" + str(i) + ") time = " + str(end - start) + "s")