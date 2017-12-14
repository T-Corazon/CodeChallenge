#~ A set of points is said to be convex if the line segment between
 #~ any two points in the set is also contained in the set. By including
 #~ all such segments, we can form the smallest convex set which contains 
 #~ our original set; this is called its convex hull.

#~ A point in the plane whose coordinates are both integers is called 
#~ a lattice point. We will say a set of lattice points is lattice convex 
#~ if any lattice point on the line segment between two points in our set 
#~ is also in the set. Analogously, the lattice convex hull of a set of 
#~ lattice points is the smallest set which contains those points and is 
#~ lattice convex.

#~ Note that our notion of lattice convexity is not equivalent to that of 
#~ ordinary convexity applied to lattice points. See the second example below.

#~ Given a list of points in the form [x, y], find their lattice 
#~ convex hull, and return the sum of x * y, taken over all of
 #~ those points, modulo 109 + 7.

#~ Example

#~ For points = [[1, 1], [4, 4]], the output should be
#~ latticeConvexHull(points) = 30.
#~ To make this set lattice convex, we must include the lattice points 
#~ on the segment between these two points, which are [2, 2] and [3, 3].
#~ Then the output is 1 * 1 + 2 * 2 + 3 * 3 + 4 * 4 = 30.

#~ For points = [[1, 1], [2, 3], [3, 2]], the output should be
#~ latticeConvexHull(points) = 13.
#~ Even though [2, 2] is in the ordinary convex hull of this set, 
#~ it's not in the lattice convex hull. In fact, this set is already 
#~ lattice convex, so the output is 1 * 1 + 2 * 3 + 3 * 2 = 13.

#~ Input/Output

#~ [time limit] 4000ms (py3)

#~ [input] array.array.integer points

#~ A list of points in the form [x, y].

#~ Guaranteed constraints:
#~ 1 <= points.length <= 500,
#~ points[i].length = 2,
#~ 0 <= points[i][0], points[i][1] <= 5000.

#~ [output] integer

#~ The sum of x * y, taken over all points in the lattice convex hull of points, mod 109 + 7.

# Here is the key result:
# If there is a 2x2 square in the set, then Lattice Convexity is equivalent to true Convexity

from bisect import insort
from time import time
from math import atan2, floor, ceil, pi

def latticeConvexHull(points):
    t = time()
    MAX = 5000
    EPSILON = MAX**-2
    PF = primeFactors(MAX)
    rows = []
    width = [0]*(max(p[1] for p in points)+1)
    
    # Add a point to the current list of points
    # Update rows and width as necessary
    def add(x,y):
        if not width[y]:
            insort(rows, y)
            width[y] = [x,x]
            return True
        else:
            a, b = width[y]
            c, d = width[y] = [min(x, a), max(x, b)]
            return d - c > b - a
    
    # Try to add m points, continuing in a line in direction (dx,dy) from (x,y)
    def addLine(x, y, dx, dy, m):
        flag = False
        for i in range(m):
            x += dx
            y += dy
            flag = add(x,y) or flag
        return flag
    
    def check(k):
        flag = True
        for i in range(len(rows)):
            for j in range(max(0,i-k),i):
                if compareRows(rows[j], rows[i]):
                    flag = False
        return flag
    
    def squareCheck():
        for i in range(len(rows)-1):
            y1, y2 = rows[i], rows[i+1]
            if y2 - y1 == 1:
                w1, w2 = width[y1], width[y2]
                if (w1[1] - w1[0]) and (w2[1] - w2[0]) and (w1[0] < w2[1]) and (w2[0] < w1[1]):
                    return [max(w1[0], w2[0]) + 0.5, y1 + 0.5]
        return []
    
    def compareRows(y1, y2):
        if y2 - y1 <= 1:
            return False
        flag = False
        for p in PF[y2-y1]:
            dy = (y2-y1)//p
            a1, b1 = width[y1]
            a2, b2 = width[y2]
            c1 = (a2 - a1 - 1)//p + 1
            c2 = (a1 - a2 - 1)//p + 1
            d1 = (b2 - b1)//p
            d2 = (b1 - b2)//p
            if a1 + p*c1 <= b2:
                g = gcd(c1, dy)
                flag = addLine(a1, y1, c1//g, dy//g, p*g - 1) or flag
            if a2 + p*c2 <= b1:
                g = gcd(c2, dy)
                flag = addLine(a2, y2, c2//g, -dy//g, p*g - 1) or flag
            if b1 + p*d1 >= a2:
                g = gcd(d1, dy)
                flag = addLine(b1, y1, d1//g, dy//g, p*g - 1) or flag
            if b2 + p*d2 >= a1:
                g = gcd(d2, dy)
                flag = addLine(b2, y2, d2//g, -dy//g, p*g - 1) or flag
        return flag
    
    def convexify():
        xt, yt = square
        corners = sorted((p for p in points if p[0] in width[p[1]]), key= lambda p: atan2(p[1] - yt, p[0] - xt))
        corners += corners[:2]
        def reduceCorners():
            reduced = True
            i = 0
            while i < len(corners)-2:
                # Test whether the middle point m is made redundant by p and q
                xp, yp, xm, ym, xq, yq = *corners[i], *corners[i+1], *corners[i+2]
                good = True
                if yp == yq:
                    good = (yt > yp) ^ (ym >= yp)
                else:
                    slope = (xq - xp)/(yq - yp)
                    good = (xt > slope*(yt - yp) + xp) ^ (xm >= slope*(ym - yp) + xp)
                    # The usual test might wrongly reject a good point if the angle changed by more than pi
                angle = atan2(yq - yt, xq - xt) - atan2(yp - yt, xp - xt)
                if angle < 0:
                    angle += 2*pi
                if not good and angle > pi - EPSILON:
                    good = True
                if not good:
                    reduced = False
                    if i == 0:
                        corners[-1] = corners[2]
                    if i == len(corners)-3:
                        corners[0] = corners[-3]
                    corners.pop(i+1)
                else:
                    i += 1
            return reduced
        
        def ceilE(x):
            return ceil(x - EPSILON)
        
        def floorE(x):
            return floor(x + EPSILON)
        
        while not reduceCorners():
            pass
        for i in range(len(corners)-2):
            xp, yp, xq, yq = *corners[i], *corners[i+1]
            if yp == yq:
                continue
            dy = 1 if yq > yp else -1
            slope = (xq - xp)/(yq - yp)
            # Is the test point to the right of our line?
            right = xt > slope*(yt - yp) + xp
            y = yp + dy
            x = xp
            while y != yq:
                x += slope*dy
                if not width[y]:
                    insort(rows, y)
                    if right:
                        width[y] = [ceilE(x), ceilE(x)-1]
                    else:
                        width[y] = [floorE(x)+1, floorE(x)]
                elif width[y][1] < width[y][0]:
                    if right:
                        width[y][0] = ceilE(x)
                    else:
                        width[y][1] = floorE(x)
                else:
                    if right:
                        if ceilE(x) < width[y][1]:
                            add(ceilE(x), y)
                    else:
                        if floorE(x) > width[y][0]:
                            add(floorE(x), y)
                y += dy

    for p in points:
        add(*p)
    SQRT_RANGE = round((rows[-1] - rows[0])**0.5)
    convex = False
    # Square acts like a boolean, but also stores the position of the square
    square = []
    while not convex and not square:
        # Make one pass, the easy way
        convex = check(SQRT_RANGE)
        # Always check whether a 2x2 square exists yet
        square = squareCheck()
        if convex and not square:
            # Check again, the thorough way
            convex = check(MAX)
    if square:
        convexify()
    s = 0
    for y in rows:
        a, b = width[y]
        s += y*(b*(b+1) - a*(a-1))/2
    s %= 10**9 + 7
    print(time() - t)
    return s

# Some auxiliary functions

def gcd(a,b):
    while a:
        a,b = b%a,a
    return abs(b)

# This will save us from computing a whole bunch of gcds, maybe
# Outputs a list A such that A[k] is a list of the prime factors of k
def primeFactors(n):
    A = [[],[]]
    for k in range(2,n+1):
        f = []
        if k % 2 == 0:
            f.append(2)
            while k % 2 == 0:
                k //= 2
        d = 3
        while d <= k**0.5:
            if k % d == 0:
                f.append(d)
                while k % d == 0:
                    k //= d
            d += 2
        if k > 1:
            f.append(k)
        A.append(f)
    return A
