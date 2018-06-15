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

    # declare a matrix variable as a list of empty lists
    matrix = [[] for i in range(len(a) + 1)]

    # fill in the base case for the origin
    matrix[0].append((0, 0))

    # fill in the base cases in the first column (first element of all lists)
    for i in range(1, len(a) + 1):
        matrix[i].append((i, Operation.DELETED))

    # flll in the base cases in the first row (all elements in the first list)
    for j in range(1, len(b) + 1):
        matrix[0].append((j, Operation.INSERTED))

    # loop over each row of the matrix, starting from the second row
    for i in range(1, len(a) + 1):
        # loop over each element of within the row, starting from the second element
        for j in range(1, len(b) + 1):
            # find the minimum of the three possible operations
            cost_sub = matrix[i - 1][j - 1][0] + (0 if a[i - 1] == b[j - 1] else 1)
            cost_ins = matrix[i][j - 1][0] + 1
            cost_del = matrix[i - 1][j][0] + 1
            cost_min = min(cost_sub, cost_ins, cost_del)
            if cost_min == cost_sub:
                matrix[i].append((cost_sub, Operation.SUBSTITUTED))
            elif cost_min == cost_ins:
                matrix[i].append((cost_ins, Operation.INSERTED))
            else:
                matrix[i].append((cost_del, Operation.DELETED))

    return matrix
