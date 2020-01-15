import glob

for file in glob.glob("*.txt"):
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            if line[0:2] == '28':
                line = '1' + line[2:]
                f.write(line)
            if line[0:2] == '43':
                line = '3' + line[2:]
                f.write(line)
            if line[0:2] == '0 ':
                f.write(line)
            if line[0:2] == '2 ':
                f.write(line)

