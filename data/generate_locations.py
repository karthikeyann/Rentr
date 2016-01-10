
#Bangalore boundaries.
toplefx = 13.042092
toplefty = 77.543132
bottomrightx  = 12.918146
bottomrighty = 77.639606



import random

radius = 200
#rangeX = (0, 2500)
#rangeY = (0, 2500)
rangeX = (13.042092,  77.543132)
rangeY = (12.918146,  77.639606)
qty = 100  # or however many points you want

# Generate a set of all points within 200 of the origin, to be used as offsets later
# There's probably a more efficient way to do this.
deltas = set()
for x in range(-radius, radius+1):
    for y in range(-radius, radius+1):
        if x*x + y*y <= radius*radius:
            deltas.add((x,y))

randPoints = []
excluded = set()
i = 0
while i<qty:
    x = random.randrange(*rangeX)
    y = random.randrange(*rangeY)
    if (x,y) in excluded: continue
    randPoints.append((x,y))
    i += 1
    excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
print randPoints


