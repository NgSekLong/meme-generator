import requests
import random
import string

def download_sample_images(count = 0):
    for i in range(count):
        img_data = requests.get("https://picsum.photos/400").content
        print("Sample Downloaded: %s" % (i + 1) )
        filename =  ''.join(random.choice(string.ascii_lowercase) for j in range(10)) 
        with open('source/%s.jpg' % filename, 'wb') as handler:

            handler.write(img_data)

