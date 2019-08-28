import os
import sys


def get_Path():

    o_path = os.getcwd()
    sys.path.append(o_path)
    path = '%s' % os.path.split(os.path.realpath(__file__))[0]

    return path
