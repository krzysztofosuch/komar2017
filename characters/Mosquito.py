class Mosquito:
    x = 0
    y = 0
    acc_x = 0
    acc_y = 0
    speed_x = 0
    speed_y = 0
    acceleration = 0.01
    deceleration = 0.01
    max_speed = 2
    def updateForTime(self, time):
        #print("acc: (%s:%s)"%(self.acc_x, self.acc_y))
        self.x += self.speed_x*time
        self.y += self.speed_y*time
        if self.acc_x != 0:
            self.speed_x = min(self.speed_x+(self.acceleration*time*self.acc_x), self.max_speed)
        else:
            if self.speed_x > 0:
                self.speed_x -= self.deceleration*time
            else:
                self.speed_x += self.deceleration*time
        if self.acc_y != 0:
            self.speed_y = min(self.speed_y+(self.acceleration*time*self.acc_y), self.max_speed)
        else:
            if self.speed_y > 0:
                self.speed_y -= self.deceleration*time
            else:
                self.speed_y += self.deceleration*time
#        if self.acc_y != 0:
#            self.speed_y = min(self.speed_y+(self.acceleration*time*self.acc_y), self.may_speed)
#        else:
#            self.speed_y = self.speed_y/(math.copysign(self.deceleration, -self.speed_y)*time)
        print('ACC = %s, speed: %s'%(self.acc_x, self.speed_x))

import math
