from __future__ import print_function
import glob
import fnmatch
import logging
import re
import os

logger = logging.getLogger('devops')

myrootdir = input ("Enter the folder to scan: ")
result = []
reg_compile = re.compile(input("enter name or extension of file: "))
while True:
    try:
        for dirpath, dirnames, filenames in os.walk(myrootdir):
            result = result + [dirname for dirname in dirnames if  reg_compile.match(dirname)]
            # logger.debug('this is what i found %f', result)
    except ValueError:
        print("Error!! You miss one of the options. Try again.")
    else:
        print('\n'.join(map(str, result)))
        break

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s')

