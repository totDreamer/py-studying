class Gun:
    def __init__(self):
        self.count = 0

    def shoot(self):
        self.count += 1
        if self.count % 2 == 1:
            print("pif")
        else:
            print("paf")

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0


gun = Gun()

print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
