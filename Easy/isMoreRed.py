#~ Your notoriously Grinchy office has decided to get into the holiday 
#~ spirit this year. They want to make the bulletin boards 
#~ Christmas-themed so they covered them with red paper. This does come 
#~ with some rules though.

#~ Any paper placed on a red background must be colored green;
#~ Any paper placed on a green background must be colored red;
#~ You can have nested backgrounds if you wish (e.g. you can have a red 
#~ paper placed on top of a green paper that is placed on the 
#~ red bulletin board;
#~ Any paper you place on another cannot completely cover the background 
#~ in width, height, or both;
#~ You cannot overlap papers on the same background.
#~ You like red and want to figure out if any given bulletin board has 
#~ more (or equal) red than green.

#~ You are given a matrix of integers. Each array represents a box 
#~ on the bulletin board. Each array has the following 4 values (in order):

#~ The box's id;
#~ The box's width;
#~ The box's height;
#~ The box's parent's id.
#~ A box's "parent" is the box that it is placed on top of. Note: 
#~ the position of the child boxes within the parent box does not matter. 
#~ There can be multiple boxes with the same parent, but the boxes 
#~ will not overlap.

#~ The outermost box will have a parent id of 0 and will be red. 
#~ The child of a red box will be green and the child of a green box 
#~ will be red.

#~ Given this, determine whether there is more visible red area than green.

#~ Example
#~ For input = [[1, 5, 5, 0], [2, 3, 4, 1]]
#~ the output should be
#~ isMoreRed(input) = true.
#~ The outermost box is red and has an area of 25. That box is then 
#~ covered by a green box that has an area of 12. That means the total 
#~ visible area is 13 for red and 12 for green.

#~ Input/Output

#~ [time limit] 4000ms (py3)

#~ [input] array.array.integer input

#~ A matrix representing a bulletin board where each row is a 
#~ square on the board (including the board itself).

#~ Guaranteed constraints:
#~ input.length <= 100,
#~ input[i].length = 4,
#~ 0 < a[0] < 10000,
#~ 0 < a[1] < 100,
#~ 0 < a[2] < 100,
#~ 0 <= a[3] < 10000.

#~ [output] boolean

#~ Whether the board is mostly red or not. 
#~ True if the color is evenly split.

def isMoreRed(matirx):
	matirx.sort()
	#red = 1 green = 0
	n = matrix[0][1]*matrix[0][2]
	red = [n]
	green = []
	matirx[0] += [n]
	matirx[0] += [1]
	for i in range(1,len(matirx)):
		matirx[i] += [matrix[i][1]*matrix[i][2]]
		if matirx[matirx[i][3]-1][5]==1:
			matirx[i] += [0]
			red.append(-1*matrix[i][4])
			green.append(matrix[i][4])
		else:
			matirx[i] += [1]
			red.append(matrix[i][4])
			green.append(-1*matrix[i][4])
	return sum(red)>sum(green)
	
def isMoreRed(m):
    m.sort()
    r = m[0][1]*m[0][2]
    g = 0
    m[0] += [1]
    for i in range(1,len(m)):
        t = [m[i][1]*m[i][2]]
        #red = 1 green = 0
        if m[m[i][3]-1][4]==1:
            m[i] += [0]
            r -= t
            g += t
        else:
            m[i] += [1]
            r += t
            g -= t
    return r>g

matrix = [[1,10,10,0], 
			[2,3,4,1], 
			[3,6,7,1], 
			[4,2,5,1], 
			[5,3,5,3]]
isMoreRed(matrix)
print(matrix)
