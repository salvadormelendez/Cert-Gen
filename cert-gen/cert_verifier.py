#!/usr/bin/env python3

###################################################################
# Certificate Verifier Python Script
# Designed and Written by Salvador Melendez
###################################################################

import sys
import os


#READ DATABASE & VERIFY CODE
def read_db():
    #DECLARE VARIABLES
    database = 'database_DO_NOT_DELETE.txt'
    #GET INPUT FROM USER
    msg = 'tput setaf 3'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    print('\nEnter Certificate Code you want to verify: ')
    msg = 'tput sgr0'
    os.system(msg)
    input_cert = input()
    #READ DATABASE
    valid_code = 0
    with open(database, 'r') as dbinfo:
        for i, line in enumerate(dbinfo):
            line = line.rstrip('\n')
            line = line.split('\t')
            line = [x for x in line if x != '']
            if(line[1] == input_cert):
                valid_code = 1
                break
    if(valid_code == 1):
        msg = 'tput setaf 2'
        os.system(msg)
        msg = 'tput bold'
        os.system(msg)
        print('\nCODE IS VALID!!!\n')
        msg = 'tput setaf 5'
        os.system(msg)
        msg = 'tput bold'
        os.system(msg)
        print('NAME: ' + line[5])
        print('EMAIL: ' + line[6])
        print('DATE: ' + line[2])
        print('LOCATION: ' + line[4])
        print('WORKSHOP: ' + line[3] + '\n')
        msg = 'tput sgr0'
        os.system(msg)
    else:
        msg = 'tput setaf 1'
        os.system(msg)
        msg = 'tput bold'
        os.system(msg)
        print('\nCODE IS NOT VALID!!!\n')
        msg = 'tput sgr0'
        os.system(msg)


#MAIN FUNCTION
def main():
    read_db()

if __name__ == "__main__":
    main()

