from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generateCharacterMatrix(character, fontPath, fontSize):
    image = Image.new('L', (fontSize, fontSize), color=0)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontPath, fontSize)

    # Dibujar el caracter en la imagen
    draw.text((0, 0), character, font=font, fill=255)

    # Convertir la imagen a una matriz de numpy
    matrix = np.array(image)
    
    return matrix

def transformMatrixValues(matrix):
    transformedMatrix = np.where(matrix != 0, 1, matrix)
    transformedMatrix = np.where(transformedMatrix == 0, -1, transformedMatrix)
    return transformedMatrix

def writeMatrixToFile(matrix, fileName):
    with open(fileName, 'w') as f:
        for row in matrix:
            rowStr = ' '.join(map(str, row))
            f.write(f"{rowStr}\n")


fontPath = "./31khz-futuristic1412/31khz-futuristic1412.ttf"
character = "A"
fontSize = 16

C = np.resize(transformMatrixValues(generateCharacterMatrix("C",fontPath,fontSize)),(1,256)).tolist()[0]
L = np.resize(transformMatrixValues(generateCharacterMatrix("L",fontPath,fontSize)),(1,256)).tolist()[0]
J = np.resize(transformMatrixValues(generateCharacterMatrix("J",fontPath,fontSize)),(1,256)).tolist()[0]
R = np.resize(transformMatrixValues(generateCharacterMatrix("R",fontPath,fontSize)),(1,256)).tolist()[0]
T = np.resize(transformMatrixValues(generateCharacterMatrix("T",fontPath,fontSize)),(1,256)).tolist()[0]
X = np.resize(transformMatrixValues(generateCharacterMatrix("X",fontPath,fontSize)),(1,256)).tolist()[0]
Z = np.resize(transformMatrixValues(generateCharacterMatrix("Z",fontPath,fontSize)),(1,256)).tolist()[0]