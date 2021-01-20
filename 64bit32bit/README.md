# 64 bit, 32 bit, 16 bit.... Meme

This is a program to generate the **64 bit** meme from a single image, I ran this program in Linux (Ubuntu 20.04), but it should run fine in   

### Installation (Normal)

1. Download Python 3 and Pip 3
2. pip3 install  -r requirements.txt
3. Execute using `python3 main.py` during run


### Installation (Docker / docker compose)

1. Install docker and docker compose
2. Execute `docker-compose up` during run

### How to run

1. Put the image to be transformed in `source` folder, it MUST be in JPG / JPEG format
  - Or, use edit `main.py`, comment out either `download_sample_images` or `download_meme_images`
2. Edit `main.py` to include other different features if needed
3. Run the program (refer the above for how to run)


### Credit:

* https://meme-api.herokuapp.com/gimme for meme generator API
* https://picsum.photos/400 for sample images