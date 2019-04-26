# import os
from os import path

def launch_analysis(data_file):
    directory = path.dirname(path.dirname(__file__))
    path_to_file = path.join(directory, "data", data_file)
    with open(path_to_file, 'r') as file:
        preview = file.readline()

    print("Yeah! We managed to read th efile. here is a preview : {}".format(preview))


def main():
    launch_analysis('current_mps.csv')


if __name__ == '__main__':
    main()
