from PIL import Image
import glob
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--source_path', help='path of the input images.', required=True)
parser.add_argument('--resized_width', help='path of the input images.', required=True)

args = parser.parse_args()
path = args.source_path + '/'

files = [f for f in glob.glob(path + "**/*.jpg", recursive=True)]
basewidth = int(args.resized_width)

print(len(files))

for index,file in enumerate(files):
    img = Image.open(file)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(file) 
    print('images processed = ' + str(index+1))