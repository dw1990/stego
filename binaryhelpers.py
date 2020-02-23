def text_to_binary(text, filler=8):
    return "".join([bin(ord(x))[2:].zfill(filler) for x in text])
