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
    def __init__(self, id: int, left_fork:Fork, right_fork:Fork):
        super().__init__()
        self.state = states.THINKING
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.id = id

    def cleanFork(self, fork: Fork):
        fork.clean()

    def canEat(self) -> bool:
        first, second = (self.left_fork, self.right_fork)

        print(f"{self.id} próbuje podnieść lewy widelec ({self.left_fork.id})")
        first.lock.acquire()
        print(f"{self.id} podniósł lewy widelec ({self.left_fork.id})")
        time.sleep(0.2)
        print(f"{self.id} próbuje podnieść [prawy] widelec ({self.right_fork.id})")
        second.lock.acquire()
        print(f"{self.id} podniósł prawy widelec ({self.right_fork.id})")

        return True



    def eat(self):
        while self.state == states.WAITING:
            if self.canEat():
                self.state = states.EATING
                eating_time = randrange(min_eating, max_eating)

                print(f"Philosopher {self.id} is eating for {eating_time}")
                time.sleep(eating_time)

                self.state = states.THINKING
                continue
            print(f"Philosopher NO.{self.id} is waiting for forks")
            print(self.left_fork, self.right_fork)


    def run(self):
            while True:
                print(self)

                if self.state == states.THINKING:
                    should_eat = randint(0,5)
                    if should_eat % 2 == 0:
                        self.state = states.WAITING
                        self.eat()
                time.sleep(3)

    def __str__(self):
        return f"Philosopher NO.{self.id} - ({self.state}) "