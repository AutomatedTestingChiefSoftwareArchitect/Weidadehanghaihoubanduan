import os
import sys


def get_Path():

    path = '%s' % os.path.split(os.path.realpath(__file__))[0]
    sys.path.append(path)

    return path


if __name__ == '__main__':

    print("Test path : %s " % get_Path())