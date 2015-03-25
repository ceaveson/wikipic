from glob import glob

def fromImageFilesGetImageNames():
    rawNames = glob("*")
    for name in rawNames:
        name = name.replace(' ','_')
        print "[[File:%s]]" % name

fromImageFilesGetImageNames()