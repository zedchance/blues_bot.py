# Version command helper

def get_version():
    """ Opens version file and returns it as a string """
    file = open("assets/version", "r")
    ret = ''
    for line in file:
        ret += line
    file.close()
    return ret
