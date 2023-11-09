
#TODO: Conviene convertir la lista a np.array?
def fonts_to_bitmap(fonts):
    bitmaps = {}
    for (character, hexaList) in fonts:
        bitmap = []
        for byte in hexaList:
            binary = format(byte, '08b')  
            row = [int(bit) for bit in binary[-5:]]  # Los caracteres tienen 3 bits de padding
            bitmap.extend(row)
        bitmaps[character] = bitmap
    return bitmaps