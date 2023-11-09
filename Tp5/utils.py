
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