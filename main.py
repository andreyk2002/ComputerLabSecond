from PIL import Image
import os

if __name__ == '__main__':
    n = 1
    results = open('results.txt', 'w', encoding="utf-8")
    images_dir = 'tests/'
    for root, dirs, files in os.walk(images_dir):
        for image in files:
            results.write('Number of image = ' + str(n) + '\n')
            img = Image.open(images_dir + image)
            results.write('  name of image:' + str(img.filename) + '\n')
            results.write('  size of image:' + str(img.size) + '\n')
            results.write('  color depth:' + str(img.mode) + '\n')
            results.write('  image compression:' + str(img.info.get('compression')) + '\n')
            results.write('  dpi:' + str(img.info.get('dpi')) + '\n')
            results.write('\n')
            n += 1
    results.close()
