import random

meters_per_kilometer = 1000
beatles = ["John","Rocky","Lacky"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]


def roll_dice(num):
    return random.randint(1,num)