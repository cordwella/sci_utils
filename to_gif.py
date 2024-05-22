import imageio
import os
import argparse

parser = argparse.ArgumentParser(description='Generate disk files and folders')
parser.add_argument('directory')

args = parser.parse_args()

folder = args.directory

images = []
for filename in sorted([x for x in os.listdir(folder) if x.endswith('.png')], key=lambda x: int(x.split('.')[0]) ):
    images.append(imageio.imread(folder + "/" + filename))

imageio.mimsave(folder + '/' + folder.split('/')[-1] + '.gif', images, duration=300, loop=0)