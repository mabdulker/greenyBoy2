import os
from random import randint

# how far back you want to fill commit graph
DAYS = 1000
# min and max amount of commits on a given day
MIN_VOLUME = 0
MAX_VOLUME = 20


def greeny():
    for i in range(1, DAYS):
        for j in range(0, randint(MIN_VOLUME, MAX_VOLUME)):
            d = f"{i} days ago"
            with open("file.txt", "a") as f:
                f.write(d)
            os.system("git add .")
            print(type(d))
            os.system(f'git commit --date="{d}" -m "commit message"')

    os.system("git push -u origin main")


if __name__ == "__main__":
    greeny()
