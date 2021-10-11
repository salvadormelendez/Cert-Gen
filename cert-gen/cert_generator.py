#!/usr/bin/env python3

#############################################
# Certificate Generator Python Script
# Designed and Written by Salvador Melendez
#############################################

import datetime
import os
import sys
from PIL import Image, ImageDraw, ImageFont

#DEFINE VARIABLES
name = ''
location = ''
unique_code = ''
image = Image.open('cert_template.jpg')

#CREATE CERTS FOLDER
def create_folder():
    folder_name = 'certificates'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    subfolder_name = 'certificates/archive'
    if not os.path.exists(subfolder_name):
        os.makedirs(subfolder_name)

#GENERATE CERTIFICATE
def gen_cert(name, location, date, unique_code):
    #GET CERT TEMPLATE TO BE USED
    draw = ImageDraw.Draw(image)

    #PARTICIPANT'S NAME
    x_axis = 1650
    num_chars = len(name)
    offset = (x_axis/2)-((num_chars/2)*45)
    font = ImageFont.truetype('imposs.ttf', size=80)
    (x,y) = (offset,465)
    color = 'rgb(0,0,255)'
    draw.text((x,y), name, fill=color, font=font)

    #PLACE
    num_chars = len(location)
    offset = (x_axis/2)-((num_chars/2)*30)
    font = ImageFont.truetype('imposs.ttf', size=50)
    (x,y) = (offset,710)
    color = 'rgb(0,0,0)'
    draw.text((x,y), location, fill=color, font=font)

    #DATE
    if(date == 'TODAY'):
        months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        now = datetime.datetime.now()
        date = str(now.day) + ' ' + months[now.month] + ' ' + str(now.year)
    else:
        date = date
    num_chars = len(date)
    offset = (x_axis/2)-((num_chars/2)*22)
    font = ImageFont.truetype('imposs.ttf', size=35)
    (x,y) = (offset,760)
    color = 'rgb(0,0,0)'
    draw.text((x,y), date, fill=color, font=font)

    #CODE
    offset = (x_axis/2)-((num_chars/2)*12)
    font = ImageFont.truetype('embosst1.ttf', size=25)
    (x,y) = (offset+60,1100)
    color = 'rgb(255,0,0)'
    draw.text((x,y), unique_code, fill=color, font=font)

#SAVE CERTIFICATE
def save_cert(name):
    cert_name = 'certificates/' + name.replace(' ','_') + '_cert'
    cert_img = cert_name + '.jpg'
    image.save(cert_img)
    msg = 'convert ' + cert_name + '.jpg ' + cert_name + '.pdf'
    os.system(msg)
    msg = 'rm ' + cert_name + '.jpg'
    os.system(msg)

#MAIN FUNCTION
def main():
    if(len(sys.argv)>1):
        name = sys.argv[1]
        location = sys.argv[2]
        date = sys.argv[3]
        unique_code = sys.argv[4]
    create_folder()
    gen_cert(name, location, date, unique_code)
    save_cert(name)

if __name__ == "__main__":
    main()

