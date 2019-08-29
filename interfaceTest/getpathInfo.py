import os
import sys


def get_Path():

    # path = '%s' % os.path.split(os.path.realpath(__file__))[0]
    path = os.getcwd()
    sys.path.append(path)

    return path
