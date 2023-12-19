# Importing the PIL library
import os, math
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from config import settings
from definitions import ROOT_DIR
 
# Open an Image

def get_file_name(folder, dir, fileNameImput):
    filename = ROOT_DIR + '/' + settings['directory']['input'] + '/' + folder + '/' + 'image' + '/' + dir + '/' + str(fileNameImput) + '.jpg'
    if (not os.path.isfile(filename)):
        filename = ROOT_DIR + '/' + settings['directory']['input'] + '/' + folder + '/' + 'image' + '/' + dir + '/' + str(fileNameImput) + '.png'
    return filename

def get_file_extension(folder, dir, fileNameImput):
    filename = ROOT_DIR + '/' + settings['directory']['input'] + '/' + folder + '/' + 'image' + '/' + dir + '/' + str(fileNameImput) + '.jpg'
    extension = 'jpg'
    if (not os.path.isfile(filename)):
        extension = 'png'
    return extension

def draw_imagẹ̣̣̣(folder ,dir, fileNameImput, text, outputDir):
    try:
        filename = get_file_name(folder, dir, fileNameImput=fileNameImput)
        extension = get_file_extension(folder, dir, fileNameImput=fileNameImput)
        img = Image.open(filename)
        print(type(img.size))
        w, h = img.size
        print('width: ', w)
        print('height:', h)
        I1 = ImageDraw.Draw(img)
        font_size = settings['image']['font_size'] * h;
        fnt = ImageFont.truetype(ROOT_DIR + "/calibri/" + "calibri.ttf", math.floor(font_size)) 
        # Add Text to an image
        position = settings['image']['position']
        pos = (w/2, h - math.floor(font_size))
        if (position == 'bottom-right'):
            pos = (w/2, h - math.floor(font_size))
        elif (position == 'bottom-left'):
            pos = (10, h - math.floor(font_size))
        elif (position == 'top-right'):
            pos = (w/2, 20)
        elif (position == 'top-left'):
            pos = (10, 20)
        I1.text(pos, text, font=fnt, fill=(255, 255, 255))
        
        # Display edited image
        outputFile = outputDir + "/" + str(fileNameImput) + "." + extension
        print(outputFile)
        img.save(outputFile)
    except Exception as e:
        print(e)
    finally:
        pass
    
