from os import path
import logging as lg

def launch_analysis(data_file):

    path_to_file = path.join("data", data_file)

    file_name = path.basename(path_to_file)
    directory = path.dirname(path_to_file)
    lg.info("Opening data file {} form directory '{}'".format(file_name, path_to_file))

    try:
        with open(path_to_file, 'r') as file:
            preview = file.readline()
            lg.debug("Yeah! We managed to read th efile. here is a preview: {%s}" % preview)
    except FileNotFoundError as e:
        lg.critical('Ow :( The file was not found. Here is the original message of the exception: {%s}' % e)
    except:
        lg.critical("Destination unknown")



def main():
    launch_analysis('SyceronBrut.xml')


if __name__ == '__main__':
    main()
