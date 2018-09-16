class Dino:
    def __init__(self,running,velocity,x,y):
        self.running=running
        self.velocity=velocity
        self.x=x
        self.y=y

    def move(self):
        self.x += self.velocity
        print("Dino has moved to coordinate " + str(self.x))

    def speedup(self):
        self.velocity += 1

    def stop(self):
        self.velocity = 0
        self.running = 0

    def jump(self):
        self.y += self.velocity
        print("Dino has moved to coordinate " + str(self.y))
        while(y>0):
            y-=1
            time.sleep(1/velocity)

