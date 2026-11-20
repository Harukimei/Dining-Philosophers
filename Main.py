from Fork import Fork
from Philosopher import Philosopher

N = 5
forks = [Fork(i) for i in range(1, N+1)]
print(forks)
philosophers = [Philosopher(i, forks[i-2], forks[i-1]) for i in range(1, N+1)]
print(philosophers, forks)

for philo in philosophers:
    philo.start()

for philo in philosophers:
    philo.join(timeout=5)





print("All philosophers eaten")