from PIL import Image
import threading
from binaryhelpers import text_to_binary


class ImageDecoder(threading.Thread):

    def __init__(self, function, img_path):
        threading.Thread.__init__(self)
        self.function = function
        self.img_path = img_path

    def run(self):
        text = self.decode_picture()
        self.function(text)

    def decode_picture(self):
        img = Image.open(self.img_path, 'r')
        buffer = ''
        value_list = []
        for x in range(0, img.width):
            for y in range(0, img.height):
                pixel = img.getpixel((x, y))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]

                bit_1 = r % 2

                buffer += str(bit_1)

                if len(buffer) == 8:
                    value_list.append(int(buffer, 2))
                    buffer = ''

                bit_2 = g % 2
                buffer += str(bit_2)

                if len(buffer) == 8:
                    value_list.append(int(buffer, 2))
                    buffer = ''

                bit_3 = b % 2
                buffer += str(bit_3)

                if len(buffer) == 8:
                    value_list.append(int(buffer, 2))
                    buffer = ''


        message = ''.join([chr(integer) for integer in value_list])

        return message
