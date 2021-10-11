#!/usr/bin/env python3

###################################################################
# Create Certificate with Unique Code Python Script
# Designed and Written by Salvador Melendez
###################################################################

import sys
import os
import datetime
import stdiomask


#DECLARE VARIABLES
students_list = 'students_list.txt'
not_sent_list = 'NOT_SENT.txt'
names = []
emails = []
f_line = []
location = ''
raw_date = ''
date = ''
folders = []
event_name = ''
cert_folder = ''
c_file = 'unique_codes.txt'
unique_code = ''
codes = []

#GET SUBDIRECTORIES TO GET LIST OF EVENTS (TEMPLATES)
cwd = os.getcwd()
raw_folders = next(os.walk(cwd))[1]
#DISCARD "CERTIFICATES" FOLDER
for i in raw_folders:
    if i != 'certificates':
        folders.append(i)

#GET UNIQUE CODE FILE
def get_code(code_folder):
    extracted_code = ''
    global codes
    codes = []
    code_file = code_folder + c_file
    with open(code_file, 'r') as inputf:
        for i, line in enumerate(inputf):
            if i == 0:
                extracted_code = line.rstrip('\n')
            else:
                line = line.rstrip('\n')
                codes.append(line)
    return extracted_code

#UPDATE UNIQUE CODE FILE
def update_code_file(code_folder):
    code_file = code_folder + c_file
    with open(code_file, 'w') as outputf:
        for i in codes:
            msg = i + '\n'
            outputf.write(msg)

#UPDATE STUDENTS' DATABASE
def update_database(name, email, event_name, location, date, unique_code):
    database_file = 'database_DO_NOT_DELETE.txt'
    if not os.path.exists(database_file):
        with open(database_file, 'w') as dataf:
            msg = 'COUNT\tCODE\t\t\tDATE\t\tEVENT\t\tLOCATION\t\t\tNAME\t\t\tEMAIL\n'
            dataf.write(msg)
    #READ FILE TO DETERMINE # OF LINES
    with open(database_file, 'r') as inputf:
        for num_lines, line in enumerate(inputf):
            pass
        num_lines+=1
    #APPEND TO DATABASE
    with open(database_file, 'a+') as dataf:
        msg = str(num_lines) + '\t' + unique_code + '\t' + date + '\t' + event_name.upper()
        if(len(event_name) < 8):
            msg+='\t\t'
        else:
            msg+='\t'
        msg+=location
        if(len(location) < 16):
            msg+='\t\t\t'
        elif(len(location) < 24):
            msg+='\t\t'
        else:
            msg+='\t'
        msg+=name
        if(len(name) < 16):
            msg+='\t\t'
        else:
            msg+='\t'
        msg+=email
        msg+='\n'
        dataf.write(msg)


#VALIDATE DATE
def validate_date(date):
    result = False
    #CHECK IF DATE ONLY HAS NUMBERS
    date_array = ''.join(date.split('/'))
    result = date_array.isdigit()
    if(result == False):
        return result
    #CHECK IF DATE HAS 3 ELEMENTS: MONTH, DAY, YEAR
    date_array = date.split('/')
    if(len(date_array) == 3):
        if(len(date_array[0]) == 2 and len(date_array[1]) == 2 and len(date_array[2]) == 4):
            month = int(date_array[0])
            day = int(date_array[1])
            year = int(date_array[2])
            #CHECK YEAR
            if(year > 2010 and year < 2050):
                result = True
            else:
                result = False
                return result
            #CHECK MONTH
            if(month > 0 and month < 13):
                result = True
                #CHECK DAY
                if(day > 0 and day < 32):
                    #CHECK IF DAY NUMBER IS VALID WITHIN THE MONTH
                    #Months with 31 days: Jan, Mar, May, Jul, Aug, Oct, Dec
                    day_31 = [1, 3, 5, 7, 8, 10, 12]
                    #Months with 30 days: Apr, Jun, Sep, Nov
                    day_30 = [4, 6, 9, 11]
                    #Special case: February - 28 or 29!
                    if((month in day_31) and day < 32):
                        result = True
                    elif((month in day_30) and day < 31):
                        result = True
                    elif(month == 2):
                        if(year%4 == 0 and day < 30):
                            result = True
                        elif(day < 29):
                            result = True
                        else:
                            result = False
                    else:
                        result = False
                else:
                    result = False
                return result
        else:
            result = False
            return result
    else:
        result = False
        return result

#FORMAT DATE TO STRING
def format_date(date):
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    date_array = date.split('/')
    new_date = str(date_array[1]) + ' ' + months[int(date_array[0])] + ' ' + str(date_array[2])
    return new_date

#GET TODAYS DATE
def get_todays():
    now = datetime.datetime.now()
    month = now.month
    if month < 10:
        month = '0' + str(month)
    day = now.day
    if day < 10:
        day = '0' + str(day)
    year = now.year
    date = str(month) + '/' + str(day) + '/' + str(year)
    return date

#SET EVENT'S INFORMATION
def event_info():
    global fromaddr, pwd, location, raw_date, date, cert_folder, event_name

    #SET EVENT
    lock_event = 1
    while(lock_event):
        print('\nSelect Event:')
        for i in folders:
            print('[' + str(folders.index(i)) + ']' + ' ' + str(i))
        try:
            event = int(input('Event #: '))
            if(event > -1) and (event < len(folders)):
                event_name = folders[event]
                print(str(event_name) + ' selected!\n')
                cert_folder = cwd + '/' + event_name + '/'
                msg = 'cp ' + cert_folder + 'cert_template.jpg .'
                os.system(msg)
                lock_event = 0
            else:
                print('NOT a valid event!... Try again!')
        except:
            print('NOT a valid event!... Try again!')
    #SET EVENT'S LOCATION
    place = input('Enter event\'s location (press ENTER to use default: El Paso, TX): ') # El Paso, TX / WSMR, NM / Las Cruces, NM / Washington D.C.
    if place == '':
        location = 'El Paso, TX'
    else:
        location = place
    #SET EVENT'S DATE
    lock_date = 1
    while(lock_date):
        raw_date = input('\nEnter event\'s date as MM/DD/YYYY (type TODAY to use today\'s date): ') # 11/25/2019
        date = raw_date
        date = date.upper()
        if(date == 'TODAY'):
            lock_date = 0
        else:
            if(validate_date(date) == True):
                date = format_date(date)
                lock_date = 0


#PARSE NAMES & EMAILS
def split_list(line):
    new_line = []
    for x in line:
        if x != "":
            new_line.append(x)
    return new_line

#READ LIST OF PARTICIPANTS' NAMES & EMAIL ADDRESSES
def read_list():
    with open(students_list, 'r') as sf:
        for i, line in enumerate(sf):
            f_line.append(line)
            if(i == 0):
                pass
            else:
                line = line.rstrip('\n')
                line = line.split('\t')
                line = split_list(line)
                names.append(line[0])
                emails.append(line[1])

#GENERATE CERTIFICATES
def create_cert(name, location, date, unique_code):
    command = './cert_generator.py ' + '\'' + name + '\'' + ' ' + '\'' + location + '\'' + ' ' + '\'' + date + '\'' + ' ' + '\'' + unique_code + '\''
    os.system(command)

#ORGANIZE CERTIFICATES
def organize_certs(index, name, email, location, date, unique_code):
    global code_folder, raw_date
    team_member = name

    #CREATE CERTIFICATE
    create_cert(team_member, location, date, unique_code)
    filename = team_member.replace(' ','_') + "_cert.pdf"
    msg = 'tput setaf 2'
    os.system(msg)
    msg = 'tput bold'
    os.system(msg)
    print("\nCertificate Created!!!\n")
    msg = 'tput sgr0'
    os.system(msg)
    subfolder_name = 'certificates/archive/' + event_name
    if not os.path.exists(subfolder_name):
        os.makedirs(subfolder_name)
    msg = 'mv certificates/' + filename + ' ' + subfolder_name + '/' + filename
    os.system(msg)
    update_code_file(cert_folder)
    if(date == 'TODAY'):
        raw_date = get_todays()
    update_database(name, email, event_name, location, raw_date, unique_code)


#GENERATE CERTIFICATES
def generate_certs():
    for i in range(len(names)):
        global cert_folder, event_name
        unique_code = get_code(cert_folder)
        organize_certs(i, names[i], emails[i], location, date, unique_code)
    msg = 'rm cert_template.jpg'
    os.system(msg)


#MAIN FUNCTION
def main():
    print('Hello! Welcome to the Certificate Generator')
    event_info()
    read_list()
    generate_certs()


if __name__ == "__main__":
    main()

