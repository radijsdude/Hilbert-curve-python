
# copyright http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
# wikipedia hilbert curve

#to visualize
import pygame
pygame.init()
displayx, displayy = 1000, 1000
displayxy = displayx, displayy
display = pygame.display.set_mode(displayxy)
clock = pygame.time.Clock()
white = (250,250,250)
black = (0,0,0)

# make da points
# n is the scaling of the amount of squares; it divides a UNIT square in this setup
# x0 and y0 are starting points the rest you should fiddle out, got it setup for a pygame screen (x > 0, y > 0)

file = open('hilbert.txt', 'w')
def hilbert(x0, y0, xi, xj, yi, yj, n):
    if n <= 0:
        X = (x0 + (xi + yi) / 2)
        Y = (y0 + (xj + yj) / 2)

        # Output the coordinates of the current point
        file.write(str(X) + ' ' + str(Y) + '\n')
    else:
        hilbert(x0, y0, yi / 2, yj / 2, xi / 2, xj / 2, n - 1)
        hilbert(x0 + xi / 2, y0 + xj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)
        hilbert(x0 + xi / 2 + yi / 2, y0 + xj / 2 + yj / 2, xi / 2, xj / 2, yi / 2, yj / 2, n - 1)
        hilbert(x0 + xi / 2 + yi, y0 + xj / 2 + yj, -yi / 2, -yj / 2, -xi / 2, -xj / 2, n - 1)

# setup for a UNIT square, play around with the last number here, put it to 7 or less
# n > 10 makes puppys suffer
hilbert(0.0, 0.0, 2, 0, 0, 2, 6)
file.close()

# to visualize we need to scale

pt = open('hilbert.txt','r')
punten = []
for lin in pt:
    x,y = float(lin.split(' ')[0]),float(lin.split(' ')[1])
# scale for the UNIT square should be the 2 ^ x
# to fill the square: I think scale = 2 ^ n, so with n from the hilbert curve function in this setup: n = 7 fills the scaled square
    scale = 256
    x *= scale
    y *= scale
    punten.append([int(x),int(y)])
print(len(punten))
# pygame loop
# pygame polygon connects the beginning and ending points.. don't do that irl, puppys will suffer and die
class loop():
    def __init__(self):
        self.stop = False
    def run(self):
        while not self.stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.stop = True
                    pygame.quit()
                    quit()



                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print(pygame.mouse.get_pos())
            display.fill(white)
            pygame.draw.polygon(display,black,punten,1)
            pygame.display.update()
            clock.tick(1)
loop().run()
# ive been able to plot images with this line when the points are used as list indices so i guess it does what it is supposed to do

# copyright: http://www.fundza.com/algorithmic/space_filling/hilbert/basics/index.html
