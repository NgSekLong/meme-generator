from moviepy.editor import *
from multiprocessing.dummy import Pool as ThreadPool
# from skimage.filter import gaussian_filter
# def blur(image):
#     """ Returns a blurred (radius=2 pixels) version of the image """
#     return gaussian_filter(image.astype(float), sigma=2)

from PIL import Image

# default is source/test.jpeg
original_image = "source/test.jpeg"

def merge_image_to_audio(imageName, scalingFactor):
    img = Image.open(original_image)
    if scalingFactor != None:
        # Resize smoothly down to 16x16 pixels (or based on scalingFactor)
        imgSmall = img.resize((scalingFactor,scalingFactor),resample=Image.BILINEAR)
        # Scale back up using NEAREST to original size
        result = imgSmall.resize(img.size,Image.NEAREST)
    else:
        result = img

    result.save("target/temp/%s.jpg" % imageName)
    audioclip = AudioFileClip("source/audio/%s.mp3" % imageName)
    # Set image clip name and duration as the same as the audio
    return (ImageClip("target/temp/%s.jpg" % imageName)
        .set_duration(audioclip.duration)).set_audio(audioclip) 
def process_video(input_original_image = None):
    global original_image
    if input_original_image != None:
        original_image = input_original_image

    pixels = dict()
    pixels['64bit'] = None
    pixels['32bit'] = 128
    pixels['16bit'] = 64
    pixels['8bit'] = 32
    pixels['4bit'] = 16
    pixels['2bit'] = 8
    pixels['1bit'] = 4
    pixels['0bit'] = 2
    pixels['m1bit'] = 1
    pixels['m2bit'] = 1


    pool = ThreadPool(4)
    all_clip = pool.starmap(merge_image_to_audio, zip(list(pixels.keys()), list(pixels.values())))

    final = concatenate_videoclips(all_clip)

    original_image_name = original_image.rsplit('/', 1)[-1]
    target_file = "target/%s.mp4" % original_image_name
    final.write_videofile(target_file, threads=4,fps=24,codec='libx264')
    return target_file
