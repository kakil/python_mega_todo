
def exercise_6():

    filenames = ['doct.txt', 'report.txt', 'presentation.txt']

    for index, filename in enumerate(filenames):
        filename = f"{filename}.txt"
        file = open(filename, 'w')
        file.write('Hello')
        file.close()

if __name__ == '__main__':
    exercise_6()