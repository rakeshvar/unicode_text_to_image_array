#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Uses cffi_wrapper to render given text to image.
'''
import random
import array

import numpy as np

import cffi_wrapper as cp
import cairocffi
from trimmers import horztrim


def scribe(text, font_style,
           width, height,
           movex, movey,
           twist):

    format = cairocffi.FORMAT_A8
    width = cairocffi.ImageSurface.format_stride_for_width(format, width)
    data = array.array('b', [0] * (height * width))
    surface = cairocffi.ImageSurface(format, width, height, data, width)
    context = cairocffi.Context(surface)
    context.translate(movex, movey)
    context.rotate(twist)

    layout = cp.gobject_ref(cp.pangocairo.pango_cairo_create_layout(context._pointer))
    cp.pango.pango_layout_set_text(layout, text.encode('utf8'), -1)

    font_desc = cp.pango.pango_font_description_from_string(font_style.encode('utf8'))
    cp.pango.pango_layout_set_font_description(layout, font_desc)

    cp.pangocairo.pango_cairo_update_layout(context._pointer, layout)
    cp.pangocairo.pango_cairo_show_layout(context._pointer, layout)

    return np.frombuffer(data, dtype=np.uint8).reshape((height, width))


def scribe_wrapper(text, font_style,
                   height, hbuffer, vbuffer,
                   twist):
    """
    Calcuates the image dimensions from given text and then renders it.
    :param text: Unicode Text
    :param font_style: "Gautami Bold 40", "Mangal Bold Italic 32" etc.
    :param height: Total height of the image.
    :param hbuffer: horizontal margin
    :param vbuffer: vertical margin
    :param twist:  rotation
    :return: an numpy array
    """

    lines = text.split('\n')
    n_lines = len(lines)
    n_letters = max(len(line) for line in lines)
    line_ht = height / (n_lines+1)
    letter_wd = .7 * line_ht
    width = round((n_letters+2) * letter_wd)

    print("Lines:", n_lines, "Letters:", n_letters)
    print("Line Height:", line_ht, " Letter Width:", letter_wd)
    print("\nFont:{}\nWidth, Height:{} Area={}\nMargins:{}\nRotation:{}".format(
        font_style, (width, height), width*height, hbuffer, vbuffer, twist))

    return scribe(text, font_style, width, height, hbuffer, vbuffer, twist)

def slab_print(slab, col_names=None):
    """
    Prints a 'slab' of printed 'text' using ascii.
    :param slab: A matrix of floats from [0, 1]
    """
    if slab.max() > 1:
        slab1 = slab/255.
    else:
        slab1 = slab

    for ir, r in enumerate(slab1):
        print('{:2d}¦'.format(ir), end='')
        for val in r:
            if   val < 0.0:     print('-', end='')
            elif val < .15:     print(' ', end=''),
            elif val < .35:     print('░', end=''),
            elif val < .65:     print('▒', end=''),
            elif val < .85:     print('▓', end=''),
            elif val <= 1.:     print('█', end=''),
            else:               print('+', end='')
        print('¦ {}'.format(col_names[ir] if col_names else ''))



hindi = "तपःस्वा"
telugu = "తపస్స్వాధ్యాయనిరతం \nతపస్వీ వాగ్విదాం వరమ్ |"
img = scribe_wrapper(hindi, "Mangal Italic 24", 45, 5, 0, 0)
img = horztrim(img, 3)
slab_print(img)