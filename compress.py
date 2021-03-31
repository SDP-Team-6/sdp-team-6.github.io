from PIL import Image
import os
import math

MAX_WIDTH = 600

for filename in os.listdir("test-images"):

    endswith = filename[-3:]
    print("yeet", endswith)
    im = Image.open("test-images/" + filename)
    w, h = im.size
    print(im.size)
    aspect_ratio = h / w
    new_filename = f"{os.path.splitext(filename)[0]}.{endswith}"
    print(filename)
    print("Aspect ratio: ", aspect_ratio)
    print("Saving to ", new_filename)

    # Resize to max width 
    downsize = MAX_WIDTH / w
    print("Downsizing to ({},{})".format(downsize * im.size[0], downsize * im.size[1]))
    im = im.resize((math.ceil(downsize * im.size[0]), math.ceil(downsize * im.size[1])), Image.LANCZOS)
    im.save(new_filename, optimize=True, quality=85)