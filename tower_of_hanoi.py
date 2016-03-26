def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("Moving disk from",fp,"to",tp)

num_of_disks = int(input('Number of disks in hanoi..'))
moveTower(num_of_disks,"A","B","C")
print('Number of moves: ' + str(2**num_of_disks - 1))
