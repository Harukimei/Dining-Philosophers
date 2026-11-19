from collections import namedtuple

from Fork import Fork
import time
from random import randrange, randint
from threading import Thread

States = namedtuple('States', ['THINKING', "WAITING",'EATING'])
states = States(THINKING=0, WAITING=1, EATING=2)
min_eating = 10
max_eating = 100

class Philosopher(Thread):
    def __init__(self):
        super().__init__()
        self.state = states.THINKING
        self.leftHand = None
        self.rightHand = None

        self.start()

    def pickUpLeftFork(self, fork: Fork):
        if not fork.is_used:
            pass

    def pickUpRightFork(self, fork: Fork):
        pass

    def cleanFork(self, fork: Fork):
        fork.clean()

    def canEat(self) -> bool: #//troll here be
        return isinstance(self.leftHand, Fork) and isinstance(self.rightHand, Fork)

    def putDownLeftFork(self):
        pass

    def putDownRighFork(self):
        pass

    def putDownBothForks(self):
        self.putDownLeftFork()
        self.putDownRighFork()


    def eat(self):
        if self.canEat():
            self.state = states.EATING
            time.sleep(randrange(min_eating, max_eating))

    def tryEating(self):
        pass
    def philosopher_life(self):
        print(self)

        if self.state == states.THINKING:
            should_eat = randint(0,5)
            if should_eat % 2 == 0:
                self.tryEating()


    def __str__(self):
        return f"Philosopher({self.state})"