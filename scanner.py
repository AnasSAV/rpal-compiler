class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type


class RPAL_Scanner:
    punction = [")", "(", ";", ","]
    # List of operator symbols in RPAL
    operator_symbol = [
        "+","-","*","<",">",
        "&",".","@","/",":",
        "=","~","|","$","!",
        "#","%","^","_","[",
        "]","{","}",'"',"`",
        "?",
    ]

    # List of reserved keywords in RPAL
    RESERVED_KEYWORDS = [
        "fn",
        "where",
        "let",
        "aug",
        "within",
        "in",
        "rec",
        "eq",
        "gr",
        "ge",
        "ls",
        "le",
        "ne",
        "or",
        "@",
        "not",
        "&",
        "true",
        "false",
        "nil",
        "dummy",
        "and",
        "|",
    ]
    # List of elements that can be part of comments
    comment_elements = ['"', "\\", " ", "\t"]

    def __init__(self, file):
        self.file = file

    # Scannning
    def Scanning(self):
        Input_Tokens = []  # Temporary list to store all tokens including whitespace
        with open(self.file, "r") as f:
            inputString = f.read()

            i = 0
            while i < len(inputString):
                                                                # Case 1: Handle identifiers (variables and keywords)
                if inputString[i].isalpha():
                    temp = i        
                    while i + 1 < len(inputString) and (        # Continue while we see letters, numbers, or underscores
                        (inputString[i + 1].isalpha())
                        or (inputString[i + 1].isdigit())
                        or (inputString[i + 1] == "_")
                    ):
                        i += 1
                    token = inputString[temp : i + 1]
                    if token in RPAL_Scanner.RESERVED_KEYWORDS:
                        Input_Tokens.append(Token(token, token))
                    else:
                        Input_Tokens.append(Token(token, "<IDENTIFIER>"))

                elif inputString[i].isdigit():                  # Case 2: Handle integers   
                    temp = i
                    while i + 1 < len(inputString) and inputString[i + 1].isdigit():
                        i += 1
                    token = inputString[temp : i + 1]
                    Input_Tokens.append(Token(token, "<INTEGER>"))

                elif (                                          # Case 3: Handle whitespace (spaces, tabs, newlines)
                    inputString[i] == " "
                    or inputString[i] == "\t"
                    or inputString[i] == "\n"
                ):
                    temp = i
                    while i + 1 < len(inputString) and (
                        inputString[i + 1] == " "
                        or inputString[i + 1] == "\t"
                        or inputString[i + 1] == "\n"
                    ):
                        i += 1
                    token = inputString[temp : i + 1]
                    Input_Tokens.append(Token(repr(token), "<DELETE>"))

                elif inputString[i] == "(":                     # Case 4: Handle parentheses, semicolons, and commas
                    token = "("
                    Input_Tokens.append(Token("(", "("))

                elif inputString[i] == ")":
                    token = ")"
                    Input_Tokens.append(Token(")", ")"))

                elif inputString[i] == ";":
                    token = ";"
                    Input_Tokens.append(Token(";", ";"))

                elif inputString[i] == ",":
                    token = ","
                    Input_Tokens.append(Token(",", ","))

                elif inputString[i] == "'":                     # Case 5: Handle string literals
                    temp = i
                    while (
                        i + 1 < len(inputString)
                        and (
                            inputString[i + 1] == "\t"
                            or inputString[i + 1] == "\n"
                            or inputString[i + 1] == "\\"
                            or inputString[i + 1] == "("
                            or inputString[i + 1] == ")"
                            or inputString[i + 1] == ";"
                            or inputString[i + 1] == ","
                            or inputString[i + 1] == " "
                            or inputString[i + 1].isalpha()
                            or inputString[i + 1].isdigit()
                            or inputString[i + 1] in RPAL_Scanner.operator_symbol
                        )
                        and inputString[i + 1] != "'"
                    ):
                        i += 1
                    if i + 1 < len(inputString) and inputString[i + 1] == "'":
                        i += 1
                        token = inputString[temp + 1 : i]   #without ' ' marks
                        Input_Tokens.append(Token(token, "<STRING>"))

                elif (                                          # Case 6: Handle comments
                    inputString[i] == "/"
                    and (i + 1 < len(inputString))
                    and inputString[i + 1] == "/"
                ):
                    temp = i
                    while i + 1 < len(inputString) and (
                        (inputString[i + 1] in RPAL_Scanner.comment_elements)
                        or inputString[i + 1] in RPAL_Scanner.punction
                        or inputString[i + 1].isalpha()
                        or inputString[i + 1].isdigit()
                        or inputString[i + 1] in RPAL_Scanner.operator_symbol
                        and (not (inputString[i + 1] == "\n"))
                    ):
                        i += 1

                    if i + 1 < len(inputString) and inputString[i + 1] == "\n":
                        i += 1
                        # token = inputString[temp : i + 1]   #with last newline
                        token = inputString[temp:i]  # without newline
                        Input_Tokens.append(Token(token, "<DELETE>"))


                elif inputString[i] in RPAL_Scanner.operator_symbol:                # Case 7: Handle operators
                    temp = i
                    while (
                        i + 1 < len(inputString) and inputString[i + 1] in RPAL_Scanner.operator_symbol
                    ):
                        i += 1
                    token = inputString[temp : i + 1]
                    Input_Tokens.append(Token(token, "<OPERATOR>"))

                i += 1

        # Remove whitespace tokens from Input_Tokens
        Tokens = []

        for token in Input_Tokens:
            if token.type != "<DELETE>":
                Tokens.append(token)

        return Tokens
