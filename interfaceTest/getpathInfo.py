import os
import sys


def get_Path():

    path = '%s' % os.path.split(os.path.realpath(__file__))[0]
    return path


def append_Path():

    o_path = os.getcwd()
    sys.path.append(o_path)
    return o_path


if __name__ == '__main__':

    print("Test path : %s " % get_Path())
