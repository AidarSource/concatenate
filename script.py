import time, glob, shutil

outfilename = 'all_' + str((int(time.time()))) + ".txt"

filenames = glob.glob('*.txt')

with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
