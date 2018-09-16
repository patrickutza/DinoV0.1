from Dino import Dino
from Bush import Bush


bush_index=[]

bush=Bush(5,0)

bush_index.append(bush)

dino=Dino(1,1,0,0)

ok=0

while(dino.running==1):
    for i in bush_index:
        if(i.x<=dino.x):
            dino.stop()
            print("Dino hit a bush")
            ok=1
    if(ok==0):
        dino.move()
     #if action jump event , then dino.jump()
    if(dino.x%4==0):
        dino.speedup()
    #EXIT_ON_CLOSE
