import random
import string


def rand_string(length):
    """
    Helper function for creating random string.
    :param length: desired length of string.
    """

    return ''.join([random.choice(string.ascii_lowercase) for i in range(length)])
