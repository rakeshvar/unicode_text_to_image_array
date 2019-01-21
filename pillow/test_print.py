#!/usr/bin/env python3
#-*- coding:utf8 -*-
import os
from PIL import Image, ImageFont, ImageDraw

im = Image.new("RGB",(160, 160))
draw = ImageDraw.Draw(im)

font_file_telugu = "/usr/share/fonts/truetype/lohit-telugu/Lohit-Telugu.ttf"
font_file_telugu = "/usr/share/fonts/truetype/fonts-telu-extra/vemana2000.ttf"
font_file_telugu = "/usr/share/fonts/truetype/fonts-telu-extra/Pothana2000.ttf"
font_file_hindi = "/usr/share/fonts/truetype/Gargi/Gargi.ttf"
# assert os.path.exists(font_file_telugu), "Font file not found: "+font_file_telugu
# assert os.path.exists(font_file_hindi), "Font file not found: "+font_file_hindi

font_telugu = ImageFont.truetype(font_file_telugu, 50)
font_hindi = ImageFont.truetype(font_file_hindi, 50)

text_telugu = "నిత్య"
text_hindi = "नित्य"

draw.text((10, 90), text_hindi, font=font_hindi)
draw.text((10, 10), text_telugu, font=font_telugu)

im.show()