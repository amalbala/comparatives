# code for displaying multiple images in one figure

# import libraries
import os
import cv2
from matplotlib import pyplot as plt


# setting values to rows and column variables
rows = 2
columns = 2

folders = [
    ("./folder1", "name1"),
    ("./folder2", "name2"),
    ("./folder3", "name3"),
    ("./folder4", "name4"),
]

outfolder = "./comparatives/"

filenames = os.listdir(folders[0][0])

rows = 2
columns = 2


for filename in filenames:
    # create figure
    fig = plt.figure(figsize=(10, 7))
    index = 1
    for folder in folders:
        path = folder[0]
        name = folder[1]
        print(f"Adding image {filename} from {path} model {name}")
        # reading images
        image = cv2.imread(os.path.join(path, filename), cv2.IMREAD_UNCHANGED)
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
        # Adds a subplot at the 1st position
        fig.add_subplot(rows, columns, index)
        # showing image
        plt.imshow(image)
        plt.axis("off")
        plt.title(name + "/" + filename)
        index = index + 1
    fig.savefig(os.path.join(outfolder, "comp_" + filename))
    plt.close()
