def getLayers(matrixLen):
    return [x for x in range(int(matrixLen/2), 0, -1)]
def getInitailCoord(layer, matrixLen):
    return int(matrixLen/2) - layer, int(matrixLen/2) - layer

def rotateMatrix(matrix):
    for layer in getLayers(len(matrix)):
        loopComplete = False
        i, j = getInitailCoord(layer, len(matrix))
        while not loopComplete:
            k, l = newPosition(i, j, layer)
            matrix[i][j], matrix[k][l] = matrix[k][l], matrix[i][j]
            i, j = newStep(i, j, layer)
            if compare(i, j, getInitailCoord(layer)): loopComplete = True