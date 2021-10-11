#!/usr/bin/env python3

##################################################
# Clean Codes Python Script
# Designed and Written by Salvador Melendez
##################################################

import sys
import os


#DECLARE VARIABLES
codes = []

#READ FILE
def read_file(i_file):
    with open(i_file, 'r') as inputf:
        for i, line in enumerate(inputf):
            line = line.rstrip('\n')
            line = line.split('"')
            new_line = line[1]
            codes.append(new_line)

#WRITE FILE
def write_file(o_file):
    with open(o_file, 'w') as outputf:
        for i in codes:
            msg = i + '\n'
            outputf.write(msg)

#MAIN FUNCTION
def main():
    if(len(sys.argv)>1):
        cwd = os.getcwd()
        desktop_dir = os.path.expanduser("~/Desktop")
        i_file = desktop_dir + '/unique_codes.txt'
        o_folder = sys.argv[1]
        o_file = cwd + '/' + o_folder + '/unique_codes.txt'
        read_file(i_file)
        write_file(o_file)
        print('Codes are clean!')
    else:
        print('Usage: ./clean_codes.py <workshop folder>')
if __name__ == "__main__":
    main()

