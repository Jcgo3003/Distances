from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""

    # Getting data
    i = len(a)
    j = len(b)

    # Creating the matrix
    matrix = [[0 for x in range(j+1)] for y in range(i+1)]


    ####### Columns #######
    # Delition cost
    count_i = 0
    for y in range( 0, i + 1):
        matrix [y][0] = count_i , Operation.DELETED
        count_i += 1

    ####### Rows #######
    # Insertions
    count_j = 0
    for x in range( 0 , j + 1 ):
        matrix [0][x] = count_j , Operation.INSERTED
        count_j += 1

    matrix[0][0] = 0, None

    #  Calculing the cost and the operations
    # while vertical
    y = 1
    while y < i + 1:

        # while horizotal
        x = 1
        while x < j + 1:

            # Evaluating sustitution
            s = 0
            if a[y-1] == b[x-1]:
                s = 0
            else:
                s = 1

            # Determining each operation value
            de = matrix[y-1][x][0] + 1
            ins = matrix [y][x-1][0] + 1
            sust = matrix[y-1][x-1][0] + s

            # Finding the minumal cost
            minimal = min( de, ins, sust  )

            #setting up operation into the matrix

            if sust == minimal:
                matrix[y][x] = sust, Operation.SUBSTITUTED

            if de == minimal:
                matrix[y][x] = de , Operation.DELETED
            if ins == minimal:
                matrix[y][x] = ins, Operation.INSERTED
            x += 1

        y += 1

    return(matrix)