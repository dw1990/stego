from binaryhelpers import text_to_binary

class MessageHeader:

    def __init__(self, message_type, message_length):
        self.message_type = message_type
        self.message_length = message_length

    def create_header(self):
        return text_to_binary(self.message_type, 8) + text_to_binary(self.message_length, 24) #length is 3 bytes



