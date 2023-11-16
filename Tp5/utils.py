
#TODO: Conviene convertir la lista a np.array?
def fonts_to_bitmap(fonts:dict):
    bitmaps = {}
    for (character, hexaList) in fonts.items():
        bitmap = []
        for byte in hexaList:
            binary = format(byte, '08b')  
            row = [int(bit) for bit in binary[-5:]]  # Los caracteres tienen 3 bits de padding
            bitmap.extend(row)
        bitmaps[character] = bitmap
    return bitmaps

# Imprime un bitmap de 7x5
def print_bitmap(bitmap:list):
    for i in range(7):
        for j in range(5):
            print(bitmap[i*5 + j], end='')
        print()

# Devuelve una matriz de 7x5
def bitmap_as_matrix(bitmap:list): 
    return [[bitmap[i*5 + j] for j in range(5)] for i in range(7)]
