import glob

for file in glob.glob("*.txt"):
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == '0':
                print(line)
