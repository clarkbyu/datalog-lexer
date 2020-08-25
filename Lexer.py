# Clark Brown

from Token import Token

class Lexer:

    def __init__(self, filename):
        self.filename = filename
        self.current_line = 1
        self.tokens = []

    def __str__(self):
        string = '\n'.join([str(i) for i in self.tokens])
        string += "\nTotal Tokens = " + str(len(self.tokens))
        return string

    def __len__(self):
        return len(self.tokens)

    def clear(self):
        self.tokens.clear()

    def add_token(self, token_type, value_list, line_number):
        value = ''.join(value_list)
        self.tokens.append(Token(token_type, value, line_number))

    def is_legal_op_char(self, c):
        legal_op_chars = ",.?():*+"
        return (c in legal_op_chars)

    def peek(self, f, length=1):
        pos = f.tell()
        data = f.read(length)
        f.seek(pos)
        return data
        
    def get(self, f , length=1):
        return f.read(length)

    def tokenize(self):
        # Create ifstream from input file to tokenize
        f = open(self.filename, 'r')
        expr = []
        c = ''
        n = ''
        EOF = ''

        while (self.peek(f) != EOF):
            expr.clear()
            c = self.get(f)
            if (c.isspace()):
                if (c == '\n'):
                    self.current_line += 1
                
            elif (c.isalpha()):
                keyword = False
                n = self.peek(f)
                expr.append(c)
                if (not n.isalnum()):
                    self.add_token("ID", expr, self.current_line)
                
                else:
                    if (c == 'S'):
                        if (n == 'c'):
                            c = self.get(f)
                            expr.append(c)
                            n = self.peek(f)

                            if (n == 'h'):
                                c = self.get(f)
                                expr.append(c)
                                n = self.peek(f)

                                if (n == 'e'):
                                    c = self.get(f)
                                    expr.append(c)
                                    n = self.peek(f)

                                    if (n == 'm'):
                                        c = self.get(f)
                                        expr.append(c)
                                        n = self.peek(f)

                                        if (n == 'e'):
                                            c = self.get(f)
                                            expr.append(c)
                                            n = self.peek(f)

                                            if (n == 's'):
                                                c = self.get(f)
                                                expr.append(c)
                                                n = self.peek(f)

                                                if (not n.isalnum()):
                                                    self.add_token("SCHEMES", expr, self.current_line)
                                                    keyword = True
                    elif (c == 'F'):
                        if (n == 'a'):
                            c = self.get(f)
                            expr.append(c)
                            n = self.peek(f)

                            if (n == 'c'):
                                c = self.get(f)
                                expr.append(c)
                                n = self.peek(f)

                                if (n == 't'):
                                    c = self.get(f)
                                    expr.append(c)
                                    n = self.peek(f)

                                    if (n == 's'):
                                        c = self.get(f)
                                        expr.append(c)
                                        n = self.peek(f)

                                        if (not n.isalnum()):
                                            self.add_token("FACTS", expr, self.current_line)
                                            keyword = True
                    elif (c == 'R'):
                        if (n == 'u'):
                            c = self.get(f)
                            expr.append(c)
                            n = self.peek(f)

                            if (n == 'l'):
                                c = self.get(f)
                                expr.append(c)
                                n = self.peek(f)

                                if (n == 'e'):
                                    c = self.get(f)
                                    expr.append(c)
                                    n = self.peek(f)

                                    if (n == 's'):
                                        c = self.get(f)
                                        expr.append(c)
                                        n = self.peek(f)

                                        if (not n.isalnum()):
                                            self.add_token("RULES", expr, self.current_line)
                                            keyword = True
                    elif (c == 'Q'):
                        if (n == 'u'):
                            c = self.get(f)
                            expr.append(c)
                            n = self.peek(f)

                            if (n == 'e'):
                                c = self.get(f)
                                expr.append(c)
                                n = self.peek(f)

                                if (n == 'r'):
                                    c = self.get(f)
                                    expr.append(c)
                                    n = self.peek(f)

                                    if (n == 'i'):
                                        c = self.get(f)
                                        expr.append(c)
                                        n = self.peek(f)

                                        if (n == 'e'):
                                            c = self.get(f)
                                            expr.append(c)
                                            n = self.peek(f)

                                            if (n == 's'):
                                                c = self.get(f)
                                                expr.append(c)
                                                n = self.peek(f)

                                                if (not n.isalnum()):
                                                    self.add_token("QUERIES", expr, self.current_line)
                                                    keyword = True
                    if (not keyword):
                        while (not keyword and n.isalnum()):
                            c = self.get(f)
                            expr.append(c)
                            n = self.peek(f)
                        self.add_token("ID", expr, self.current_line)
            
            elif (self.is_legal_op_char(c)):
                expr.append(c)
                if c == ':':
                    n = self.peek(f)
                    if (n == '-'):
                        c = self.get(f)
                        expr.append(c)
                        self.add_token("COLON_DASH", expr, self.current_line)
                    
                    else:
                        self.add_token("COLON", expr, self.current_line)
                    
                elif (c == ','):
                    self.add_token("COMMA", expr, self.current_line)
                    
                elif (c == '.'):
                    self.add_token("PERIOD", expr, self.current_line)
                    
                elif (c == '?'):
                    self.add_token("Q_MARK", expr, self.current_line)
                    
                elif (c == '('):
                    self.add_token("LEFT_PAREN", expr, self.current_line)
                    
                elif (c == ')'):
                    self.add_token("RIGHT_PAREN", expr, self.current_line)
                    
                elif (c == '*'):
                    self.add_token("MULTIPLY", expr, self.current_line)
                    
                elif (c == '+'):
                    self.add_token("ADD", expr, self.current_line)

            elif (c == '#'):
                expr.append(c)
                n = self.peek(f)

                if (n == '|'): # Block Comment Case
                    c = self.get(f)
                    expr.append(c)
                    n = self.peek(f)

                    comment_start_line = self.current_line
                    valid_comment = True
                    end_comment = False

                    while (not end_comment and valid_comment):
                        if (n == EOF):
                            self.add_token("UNDEFINED", expr, comment_start_line)
                            valid_comment = False
                        else:
                            c = self.get(f)
                            expr.append(c)
                            if (c == '\n'):
                                self.current_line += 1
                            
                            n = self.peek(f)
                        
                        if ((c == '|') and (n == '#')):
                            end_comment = True
                            c = self.get(f)
                            expr.append(c)
                    
                    if (valid_comment):
                        self.add_token("COMMENT", expr, comment_start_line)
                    
                else: # Singe Line Comment Case
                    while (n != '\n' and n != EOF):
                        c = self.get(f)
                        expr.append(c)
                        n = self.peek(f)
                    
                    self.add_token("COMMENT", expr, self.current_line)
                
            elif (c == '\''):
                expr.append(c)
                n = self.peek(f)

                num_quotes = 1
                string_start_line = self.current_line
                valid_string = True
                end_string = False

                while (not end_string and valid_string):
                    if (n == EOF):
                        self.add_token("UNDEFINED", expr, string_start_line)
                        valid_string = False
                    else:
                        c = self.get(f)
                        expr.append(c)
                        if (c == '\''):
                            num_quotes += 1
                        if (c == '\n'):
                            self.current_line += 1
                        n = self.peek(f)
                    
                    if ((num_quotes % 2 == 0) and (c == '\'') and (n != '\'')):
                        end_string = True
                    
                if (valid_string):
                    self.add_token("STRING", expr, string_start_line)

            else:
                expr.append(c)
                self.add_token("UNDEFINED", expr, self.current_line)

        # Final Token is EOF every time
        self.add_token("EOF", EOF, self.current_line)

        # Close input file
        f.close()
    # end tokenize()
