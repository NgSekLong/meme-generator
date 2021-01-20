from process_video import process_video
from download_sample_images import download_sample_images
from download_meme_images import download_meme_images
import glob
from play_video import play_video
def main():
    # download_sample_images(5) # Download sample images
    # download_meme_images(3) # Download meme images (from reddit)
    all_images = glob.glob("source/*.*")
    for image in all_images:
        target_file = process_video(image)
        
        #play_video(target_file) # Enabled this line if you want video to automatically played after render
if __name__ == "__main__":
    main()