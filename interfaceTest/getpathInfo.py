import os
import sys


def get_Path():

    o_path = '%s' % os.path.split(os.path.realpath(__file__))[0]
    sys.path.append(o_path)

    return o_path
