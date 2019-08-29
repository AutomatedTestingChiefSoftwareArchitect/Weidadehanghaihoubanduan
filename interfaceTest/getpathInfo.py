import os


def get_Path():

    path = '%s' % os.path.split(os.path.realpath(__file__))[0]
    return path

if __name__ == '__main__':

    print("Test path : %s " % get_Path())
