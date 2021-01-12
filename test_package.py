import os
import sys

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from dconfig import config
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd1in54_V2 Demo")
    
    epd = config.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    time.sleep(1)
    
    def center_txt(img, font, tex, fill=0):
        draw = ImageDraw.Draw(img)
        txt_widt, txt_heig = draw.textsize(tex, font)
        posisi = ((epd.width-txt_widt)/2, (epd.height-txt_heig)/2)
        draw.text(posisi, tex, font=font, fill=fill)
        return img
        
    def wrap_txt(img, font, tex, fill = 0, align = 'left'):
        draw = ImageDraw.Draw(img)
           
        return img
    
    # Drawing on the image
    logging.info("1.Drawing on the image...")
    image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(os.path.join(picdir, 'Computerfont.ttf'), 24)
    #draw.rectangle((0, 0, 199, 199), fill = 255, outline = 0)
    pesan = 'Aplikasi pesan \ninstan \nWhatsApp punya kebijakan baru. Aturan yang akan berlaku efektif pada 8 Februari 2021 tersebut "memaksa" pengguna setuju data-data mereka diteruskan WhatsApp ke Facebook sebagai perusahaan induk. Menanggapi hal ini, Menteri Komunikasi dan Informatika Johnny Plate mengimbau masyarakat agar semakin berhati-hati dalam menggunakan media sosial, dengan selalu membaca kebijakan privasi sebelum menggunakan layanan dan memberi persetujuan data pribadi.'
    draw.text((0,0), pesan, font = font, fill = 0, spacing = 5)
    #txt_x, txt_y = draw.textsize(pesan, font)
    #pjg = "x:" + str(txt_x) + " y:" + str(txt_y)
    #center_txt(image, font, pjg)
    
    j = 0
    k = ''
    for i in pesan:            
        if i == '\n':
            txt_widt, txt_heig = draw.textsize(k, font)
            logging.info(k + "pjg pix =" + str(txt_widt) + "pjg piy:" + str(txt_heig
            ))
        j += 1
        k += i 
    
    epd.display(epd.getbuffer(image.rotate(0)))
    time.sleep(10)
    
    
    
    """ # read bmp file 
    logging.info("2.read bmp file...")
    image = Image.open(os.path.join(picdir, '1in54.bmp'))
    epd.display(epd.getbuffer(image))
    time.sleep(2)
    
    # read png file on window
    logging.info("3.read bmp file on window...")
    epd.Clear(0xFF)
    image1 = Image.new('L', (epd.width, epd.height), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, 'twitter.png'))
    image1.paste(bmp, (0,0))    
    epd.display(epd.getbuffer(image1))
    time.sleep(2)
    
    # partial update
    logging.info("4.show time...")
    time_image = image1
    # Image.new('1', (epd.width, epd.height), 255)
    epd.displayPartBaseImage(epd.getbuffer(time_image))
    
    time_draw = ImageDraw.Draw(time_image)
    num = 0
    while (True):
        time_draw.rectangle((10, 10, 120, 50), fill = 255)
        time_draw.text((10, 10), time.strftime('%H:%M:%S'), font = font, fill = 0)
        newimage = time_image.crop([10, 10, 120, 50])
        time_image.paste(newimage, (10,10))  
        epd.displayPart(epd.getbuffer(time_image))
        num = num + 1
        if(num == 20):
            break """
    
    #logging.info("Clear...")
    #epd.init()
    #epd.Clear(0xFF)
    
    logging.info("Goto Sleep...")
    epd.sleep()
    time.sleep(3)
    
    epd.Dev_exit()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd1in54_V2.epdconfig.module_exit()
    exit()
