# directory searcher: searches through a directory for text files and looks for what files contain a given regular
# expression
# Usage: python dirsearch.py <regexpression> <directory>

import os
import re
import sys

# GET COMMAND LINE ARGUMENTS
if len(sys.argv) >= 2:
    directory = "."  # if the user gives no directory path
    if len(sys.argv) == 3:
        directory = sys.argv[2]  # if there exists a given directory
    # ISOLATE DIRECTORY AND REGULAR EXPRESSION
    directory = os.path.abspath(directory)
    regularExpression = sys.argv[1]
    regexpression = re.compile(regularExpression)
    # CHECK IF DIRECTORY EXISTS
    if not os.path.exists(directory):
        print("directory does not exist")
    if not regexpression.pattern:
        print("Regular expression is invalid")
    else:
        # GET LIST OF FILES IN DIRECTORY
        allfilePaths = os.listdir(directory)
        results = []
        # LOOP AND CHECK THROUGH THE TEXT FILES
        for filePath in allfilePaths:
            ext = os.path.basename(filePath)
            if not "txt" in ext:
                continue
            # READ THE CONTENT AND MATCH ONLY IF TEXTFILE
            file = open(filePath)
            holder = []
            # RESULT HOLDER
            for line in file.readlines():
                # IF MATCHED CREATE STRING AND STORE INTO UPDATE ARRAY
                if regexpression.search(line):
                    holder.append("MATCH: " + line + "\n")
            # CLOSE FILE WHEN DONE READING
            if len(holder) <= 0:
                continue
            holder = filePath + "\n" + "*" * 20 + "\n" + "".join(holder)
            holder += "\n" * 2
            results.append(holder)
            file.close()
        # PRINT RESULT
        for result in results:
            print(result)
else:
    print("Usage: python dirsearch.py <regexpression> <directory>(optional)")