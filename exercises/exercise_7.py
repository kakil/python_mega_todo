# Coding exercise 7

## Please download the three text files a.txt, b.txt, and c.txt
# from the resources and place them in your computer IDE.
# Then, create a program that:
# 1. reads each text file and
# 2. prints out the content of each file in the command line.
# The expected output would be like the following:
##

def exercise_7():

    files = ['a.txt', 'b.txt', 'c.txt']

    for index, filename in enumerate(files):
        filename = f"../files/{filename}"
        file = open(filename, 'r')
        text = file.read()
        print(f"{text}")

if __name__ == '__main__':
    exercise_7()