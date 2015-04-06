write = open('45degreeStripes.csv', 'w')
start = 0
#for x in range(0,10000,1000):

''' bbox of polygon '''
# first type in the coordinates of the lower right corner
x_lr = 39000
y_lr = 0

# type in the coordinates of the upper left corner (minus -100000)
x_min = -100000
y_max = 50000
x_max = x_lr
y_min = y_lr

i = 0

#for y in range(35000, 0,100):
while x_max >= x_min:
    write.write('%s;LineString(%s %s, %s %s)\n'%(i, x_max, y_lr, x_lr, y_min))
    i += 1
    x_max -= 100
    y_min += 100
write.close()        