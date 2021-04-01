from PIL import Image
import os
import math

MAX_WIDTH = 600
direc = "images/thumbs/"

for filename in os.listdir(direc):


    endswith = filename[-3:]
    print(endswith)
    if endswith == 'jpg' or endswith == 'png':
    # print("yeet", endswith)
        im = Image.open(direc + filename)
        w, h = im.size
        print(im.size)
        aspect_ratio = h / w
        new_filename = f"{direc}{os.path.splitext(filename)[0]}.{endswith}"
        print(filename)
        print("Aspect ratio: ", aspect_ratio)
        print("Saving to ", new_filename)

        # Resize to max width 
        downsize = MAX_WIDTH / w
        print("Downsizing to ({},{})".format(downsize * im.size[0], downsize * im.size[1]))
        im = im.resize((math.ceil(downsize * im.size[0]), math.ceil(downsize * im.size[1])), Image.LANCZOS)
        im.save(new_filename, optimize=True, quality=85)