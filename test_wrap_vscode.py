#%%
import os
import sys
import textwrap
import random

picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

from PIL import Image,ImageDraw,ImageFont
epd_width = 200
epd_height = 200

def center_txt(img, font, tex, fill=0):
    draw = ImageDraw.Draw(img)
    txt_widt, txt_heig = draw.textsize(tex, font)
    posisi = ((epd_width-txt_widt)/2, (epd_height-txt_heig)/2)
    draw.text(posisi, tex, font=font, fill=fill)
    return img

def wrap_txt(img, font, tex, fill=0, align = 'center'):
    draw = ImageDraw.Draw(img)  
    pjg_wrp_tex = 0
    i = 0
    l = 0
    while l < len(tex):
        while i < epd_width:
            pjg_wrp_tex += 1
            i = draw.textsize(tex[l:l+pjg_wrp_tex], font)[0]
        l += pjg_wrp_tex
        print(l)
    novo = textwrap.wrap(tex, width=20)
    marg = offs = 0
    for line in novo:
        draw.multiline_text((marg, offs), line, font = font, fill = 0, spacing = 0, align = align)
        offs += font.getsize(line)[1]
    return img


image = Image.new('1', (epd_width, epd_height), 255)  # 255: clear the frame
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(os.path.join(picdir, 'Computerfont.ttf'), 24)
pesan = 'Aplikasi pesan instan WhatsApp punya kebijakan baru. Aturan yang akan berlaku efektif pada 8 Februari 2021 tersebut "memaksa" pengguna setuju data-data mereka diteruskan WhatsApp ke Facebook sebagai perusahaan induk. Menanggapi hal ini, Menteri Komunikasi dan Informatika Johnny Plate mengimbau masyarakat agar semakin berhati-hati dalam menggunakan media sosial, dengan selalu membaca kebijakan privasi sebelum menggunakan layanan dan memberi persetujuan data pribadi.'
#draw.text((0,0), pesan, font = font, fill = 0)
txt_x, txt_y = draw.textsize(pesan, font)
pjg = "x:" + str(txt_x) + " y:" + str(txt_y)
#print(pjg)
wrap_txt(image, font, pesan)
#center_txt(image, ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24), pjg)



# %%
