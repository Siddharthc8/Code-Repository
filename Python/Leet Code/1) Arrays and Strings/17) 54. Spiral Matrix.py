name = "Sid"
def spiral(matrix):
    res = []
    m = len(matrix)
    n = len(matrix[0])
    i, j = 0, 0
    UP, RIGHT, LEFT, DOWN = 0, 1 ,2 , 3  # More like enum
    direction = RIGHT

    UP_WALL = 0              # Since it starts we consider the same line
    RIGHT_WALL = n
    DOWN_WALL = m
    LEFT_WALL = -1

    while len(res) != m*n:
        if direction == RIGHT:
            while j < RIGHT_WALL:
                res.append(matrix[i][j])
                j+=1
            i, j = i+1, j-1
            RIGHT_WALL -= 1
            direction = DOWN

        elif direction == DOWN:
            while i < DOWN_WALL:
                res.append(matrix[i][j])
                i+=1
            i, j = i-1, j-1
            DOWN_WALL -= 1
            direction = LEFT

        elif direction == LEFT:
            while j > LEFT_WALL:
                res.append(matrix[i][j])
                j-=1
            i, j = i-1, j+1
            LEFT_WALL += 1
            direction = UP

        elif direction == UP:
            while i > UP_WALL:
                res.append(matrix[i][j])
                i-=1
            i, j = i+1, j+1
            UP_WALL += 1
            direction = RIGHT
    print(res)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
Expected = [1,2,3,6,9,8,7,4,5]
spiral(matrix)

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Expected1 = [1,2,3,4,8,12,11,10,9,5,6,7]
spiral(matrix1)