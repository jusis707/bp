import datetime

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

with open(timeStamped('myfile.txt'),'w') as outf:
    outf.write('HELLO BP!')
