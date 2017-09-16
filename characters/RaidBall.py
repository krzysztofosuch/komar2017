from characters.Character import Character
class RaidBall(Character):
    speed = 1
    killer = 1
    def updateForTime(self, time):
        self.ttl -= time
        self.x = self.x + self.speed_x * time
        new_y = self.y + self.speed_y*time
        self.y = new_y
