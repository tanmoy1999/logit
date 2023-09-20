def log(filename, lines):
    with open(filename, 'a') as file:
        for line in lines:
            file.write(line + '\n')