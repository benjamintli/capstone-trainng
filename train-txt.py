import glob

with open("train-4cls.txt", "w") as f:
    for file in glob.glob("data/valid_images/*.jpg"):
        f.write(file)
        f.write("\n")

    
