from standardizer import *
from scanner import RPAL_Scanner
from ASTParser import ASTParser
import sys

hasParsingError = False
hasCSEError = False
hasInputError = False
astFlag = ""

if len(sys.argv) == 2:
    file = sys.argv[1]
    astFlag = ""

elif len(sys.argv) == 3 and sys.argv[1] == "-ast":
    file = sys.argv[2]
    astFlag = "-ast"

elif len(sys.argv) == 3 and sys.argv[1] != "-ast":
    hasInputError = True
    astFlag = "invalid"

else:
    hasInputError = True
    astFlag = "invalid"

if not hasInputError:
    scanner = RPAL_Scanner(file)  # Give the name of the file

    try:
        tokens = scanner.Scanning()

    except:
        hasInputError = True
        print("There is no such a file :", file)

    if not hasInputError:
        myParser = ASTParser(tokens)
        myParser.startParsing(astFlag)
        hasParsingError = myParser.isAnError()

        if not hasParsingError:
            root = myParser.stack[0]
            stand = standardizer(root)

            for i in range(10):
                stand.makeST(root)
            
            controlStructureArray = [[None for _ in range(200)] for _ in range(200)]
            stand.createControlStructures(root, controlStructureArray)

            size = 0
            while controlStructureArray[size][0] is not None:
                size += 1

            setOfControlStruct = []
            for x in range(size):
                temp = []
                for y in range(200):
                    if controlStructureArray[x][y] is not None:
                        temp.append(controlStructureArray[x][y])
                setOfControlStruct.append(temp)
            
            if astFlag != "-ast":
                try:
                    stand.cse_machine(setOfControlStruct)
                except Exception as e:
                    print("CSE machine error")
                    print(e)

        elif hasParsingError:
            pass 

else:
    print("Input Format is Wrong")
    print("Input format ==>  python .\\myrpal.py file_name")
    print("To print the AST use -ast flag before the file name.")
