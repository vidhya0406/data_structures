import os, sys
from queue import *

people_queue = Queue()

players = input('Enter player names....').split(',')
rand_number = int(input('Enter number of passes...'))
for player in players:
    people_queue.enqueue(player)
while people_queue.size() > 1:
    for i in range(rand_number):
        people_queue.enqueue(people_queue.dequeue())
    people_queue.dequeue()

print('Remaining: ' + people_queue.dequeue())
