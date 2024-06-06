from config import settings
import argparse
from helpers.excel import read_excel_and_draw_image

 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-i", "--input", help = "input folder")
# Read arguments from command line
args = parser.parse_args()
if args.input:
    print("Displaying input as: % s" % args.input)
    read_excel_and_draw_image(args.input)