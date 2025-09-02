class Enemy:
    life = 3

    def attack(self):
        print("Ouch")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()              # enemy1 is an object of the class Enemy
enemy1.attack()
enemy1.checklife()