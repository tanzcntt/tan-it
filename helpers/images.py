# Importing the PIL library
import glob
import os, math
from wand.image import Image as ImageConvert
from pathlib import Path
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
        I1.text(pos, text, font=fnt, fill=(255, 255, 255), anchor=None, spacing=font_size/2)
        
        # Display edited image
        outputFile = outputDir + "/" + str(fileNameImput) + "." + extension
        print(outputFile)
        img.save(outputFile)
    except Exception as e:
        print(e)
    finally:
        pass
    
def convert_image(input_folder):
    try:
        scan_dir = ROOT_DIR + '/image-input/' +  input_folder + '/**/*.HEIC'
        files = glob.glob(scan_dir,  
                   recursive = True) 
        for file in files:
            p_file = Path(file)
            output_file = str(p_file).replace('image-input','image-output').replace("HEIC","jpg")
            output_dir = str(p_file.parent).replace('image-input','image-output')
            os.makedirs(output_dir, exist_ok=True)
            img=ImageConvert(filename=file)
            img.format='jpg'
            img.save(filename=output_file)
            img.close()
            print(p_file) 
    except Exception as e:
        print(e)
    finally:
        pass
    
