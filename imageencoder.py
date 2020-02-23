from PIL import Image
from os import path
from binaryhelpers import text_to_binary
from messageheader import MessageHeader

import sys


class ImageEncoder:

    def __init__(self, img_path):
        self.img_path = img_path

    def _corrected_bit(self, val, par_bit):
        if val % 2 == 1 and par_bit == 1:
            return val
        elif val % 2 == 1 and par_bit == 0:
            return val - 1
        elif val % 2 == 0 and par_bit == 0:
            return val
        elif val % 2 == 0 and par_bit == 1:
            return val + 1
        else:
            return val

    def encode(self, message, output_suffix):
        bin_message = text_to_binary(message)

        message_header = MessageHeader("text", len(bin_message))
        bin_message = message_header.create_header() + bin_message



        if not path.exists(self.img_path):
            print(self.img_path)
            sys.exit('img doesn\'t exist')

        curr_message_index = 0
        img = Image.open(self.img_path, 'r')
        for x in range(0, img.width):
            for y in range(0, img.height):
                pixel = img.getpixel((x, y))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if curr_message_index < message_len - 2:
                    three_bits = [int(x) for x in bin_message[curr_message_index:curr_message_index+3]]
                    r = self._corrected_bit(r, three_bits[0])
                    g = self._corrected_bit(g, three_bits[1])
                    b = self._corrected_bit(b, three_bits[2])
                    curr_message_index = min(message_len, curr_message_index + 3)
                img.putpixel((x, y), (r, g, b))
        img.save(self.img_path[:-4] + "{}.png".format(output_suffix))

