import re

# do a search in the dictionary for an English word
def searchFile(file, query):
    f = open(file, 'r')
    lines = f.read() #lines is of type string

    query = re.compile(query, re.IGNORECASE) #make case not matter

    query_lines = [] #lines that contain the search term
    for a in list(re.finditer(query, lines)):

        line_start = a.start()
        line_end = a.end()
        
        # search term must be at very beginning of defintion
        # will find search term, but there must be a " /" before it if
        # it is at the beginning of the definition
        if lines[line_start - 2:line_start] == " /":

            # grab the rest of the definition
            i = 1
            while(1):
                if (lines[line_start-i] == '\n'):
                    line_start = a.start()-i+1
                    break
                i = i + 1

            i = 1
            while(1):
                if (lines[line_end + i] == '\n'):
                    line_end = a.end()+i
                    break
                i = i + 1

            # add each one to a list
            query_lines.append(lines[line_start:line_end])

    if len(query_lines) == 0:
        print "no results"

    # split each definition its parts (eng, pin, simp, trad)
    query_split = CEDICT_split(query_lines)

    # sort to make the ones with the shortest match appear first
    # ex. if searching for "team", "team mate" would appear before
    #     "team member"
    sorted_list = selSortEng(query_split)

    for i in range(len(sorted_list)):
    	for j in range(4):
            print sorted_list[i][j]
    return None

# sort to make the definitions with the shortest match first
def selSortEng(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if len(list[i][0][0]) > len(list[j][0][0]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

# take the raw output from he dictionary and break it up into parts
def CEDICT_split(query_lines):
    query_split = []
    for i in range(len(query_lines)):

        #find Traditional
        space1 = query_lines[i].find(' ')
        trad = query_lines[i][:space1]
        #print trad

        #find Simplified
        space2 = query_lines[i][space1+1:].find(' ')
        simp = query_lines[i][space1+1:space1+1+space2]
        #print simp

        #find Pinyin
        brac1 = query_lines[i].find('[')
        brac2 = query_lines[i].find(']')
        pinyin = query_lines[i][brac1+1:brac2]
        #print pinyin

        #find English
        slash1 = query_lines[i].find('/')
        english = query_lines[i][slash1+1:-2]
        english = english.split('/')
        #print english
        #print english

        query_split.append([english, pinyin, simp, trad])
    return query_split


if __name__ == '__main__':
    import sys

    searchFile('cedict-20091118.txt', str(sys.argv[1]))
