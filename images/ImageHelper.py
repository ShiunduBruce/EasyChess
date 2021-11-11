import base64
from io import BytesIO
from images import imagedata

# Convert images to binary


class ImageHelper:

    # Converts almages to binary
    def convertImagesToBinary(self):
        images = ['rookwhite.png', 'bishopwhite.png', 'knightwhite.png', 'pawnwhite.png', 'rookblue.png', 'bishopblue.png', 'knightblue.png', 'pawnblue.png']
        
        for file in images:
            image = open(file, 'rb')
            content = '{} = {}\n'.format(file.split('.')[0], base64.b64encode(image.read()))
            image.close()

            with open('imagedata.py', 'a') as f:
                f.write(content)

    # Gets the image data
    def getImageData(self, imageName):
        imageData = []

        if imageName == 'rookwhite':
            imageData = imagedata.rookwhite

        if imageName == 'bishopwhite':
            imageData = imagedata.bishopwhite

        if imageName == 'knightwhite':
            imageData = imagedata.rookwhite

        if imageName == 'pawnwhite':
            imageData = imagedata.pawnwhite

        if imageName == 'rookblue':
            imageData = imagedata.rookblue

        if imageName == 'bishopblue':
            imageData = imagedata.bishopblue

        if imageName == 'knightblue':
            imageData = imagedata.knightblue

        if imageName == 'pawnblue':
            imageData = imagedata.pawnblue
        
        byte_data = base64.b64decode(imageData)
        image_data = BytesIO(byte_data)
        
        return image_data
