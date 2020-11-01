 #This is the first submission file of readTATE

import csv
import requests
from PIL import Image
from io import BytesIO

class ArtTATE:
    def __init__(self, id, width, depth, height, imageUrl, artist):
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''

    def describe(self):
       print("artist:" + self.artist, "id:" + self.id, "width:" + str(self.width),"depth:" + str(self.depth), "height:" + str(self.height))

    def getImageFile(self):
           if self.imageUrl:
               response = requests.get(self.imageUrl)
               try:
                   im = Image.open(BytesIO(response.content))
               except OSError:
                   return None
               path = "ArtImages/" + self.artist + "_" + self.id + ".jpg"
               self.imagePath = path
               im.save(path, "JPEG")

artPieces = []
with open("CSVFiles/artwork_data.csv", encoding = 'utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['id']
        width = row['width']
        depth = row['depth']
        height = row['height']
        imageUrl = row['thumbnailUrl']
        artist = row['artist']
        if width or depth or height:
            artPiece = ArtTATE(id, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)

for art in artPieces:
    if "Blake, Robert" in art.artist:
        art.getImageFile()
