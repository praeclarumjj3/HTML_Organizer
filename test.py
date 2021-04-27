import os
from html import HTML
from icecream import ic
from tqdm import tqdm
import argparse

def main(args):

    win_width = 300
    win_height = 300
    webpage = HTML('web/', args.title)
    webpage.add_header(args.title)

    for i, dir in tqdm(enumerate(os.listdir('web/'+ args.img_dir))):
        imgs = []
        txts = []
        for image_path in os.listdir('web/{}/{}'.format(args.img_dir, dir)):

            img = os.path.join('{}/{}'.format(args.img_dir,dir),image_path)
            
            imgs.append(img)

        imgs.sort()

        for img_path in imgs:
            if img_path.split('/')[-1] == '0.jpg':
                txts.append('Original Image')
            elif img_path.split('/')[-1] == '1.jpg':
                txts.append('Background')
            else:
                txts.append('Completed Object')

        webpage.add_images(imgs, txts, imgs, i+1, width=win_width, height=win_height)
        webpage.save()

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="HTML Organizer")
    parser.add_argument("--title", default="HTML Organizer",
    help="title of the HTML page")
    parser.add_argument("--img_dir", default="demos",
    help="name of images directory inside the web directory")
    args =  parser.parse_args()
    
    main(args)