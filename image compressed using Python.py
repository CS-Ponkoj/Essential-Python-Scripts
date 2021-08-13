from PIL import Image
from PIL import UnidentifiedImageError
import glob
import os
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

# new folder path (may need to alter for Windows OS)
# change path to your path
path = './r' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)

# loop over existing images and resize
# change path to your path

for filename in glob.glob('./filepath/*.jpg'): #path of raw images
    try:
        img = Image.open(filename).resize((800, 600))
        # save resized images to new folder with existing filename
        img.save('{}{}{}'.format(path,'/',os.path.split(filename)[1]))
        print(filename + '-- done')
    except UnidentifiedImageError:
        pass
    except OSError:
        pass






