# Clark Brown

class Token:
    def __init__(self, token_type, value, line_number):
        self.token_type = token_type
        self.value = value
        self.line_number = line_number

    def __str__(self):
        string = "(" + self.token_type + ","
        string += '"' + str(self.value) + '",' + str(self.line_number) + ")"
        return string