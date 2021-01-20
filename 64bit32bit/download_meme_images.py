import requests
import random
import string

def download_meme_images(count = 0):
    for _ in range(count):
        while True:
            url = requests.get("https://meme-api.herokuapp.com/gimme").json().get("url")
            
            img_data = requests.get(url).content
            if not url.lower().endswith(( '.jpg')):
                continue
            print("Meme URL download: %s" % url)

            filename =  ''.join(random.choice(string.ascii_lowercase) for i in range(10)) 
            with open('source/%s.jpg' % filename, 'wb') as handler:

                handler.write(img_data)
            break
