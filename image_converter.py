import time
from config import settings
import argparse

from helpers.images import convert_image
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-i", "--input", help = "input folder")
# Read arguments from command line
args = parser.parse_args()
if args.input:
    start = time.process_time()
# your code here    
    
    print("Bat dau convert anh trong thu muc %s " % args.input)
    convert_image(args.input)
    print("Ket thuc convert anh trong thu muc {} thoi gian thuc hien: {} ".format(args.input, str(time.process_time() - start)))
