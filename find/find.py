import re, csv

# do a search in the dictionary for an English word
def searchFile(file, query):
    f = open(file, 'r')

    query = re.compile(query, re.IGNORECASE) #make case not matter

    query_lines = [] #lines that contain the search term
    for line in f.readlines():
        match = re.search(query, line)
        if (match):
            if line[match.start()-1] == line[match.end()] == "/":
                query_lines.append(line)
    
    for i in range(len(query_lines)):
        print query_lines[i]

    if len(query_lines) == 0:
        print "no results"

    # split each definition its parts (eng, pin, simp, trad)
    query_split = CEDICT_split(query_lines)

    # make a list of Chinese words and their frequencies
    freq_list = cons_freq_comp()

    # find the most frequent instance of a word
    top_hanz, top = comp_freq(query_split, freq_list)

    print "the best choice is:", top_hanz, " (", top, ")"
    for i in range(len(query_split)):
        print query_split[i][2], query_split[i][1]


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

def cons_freq_comp():

    # construct frequency list
    f = open('SUBTLEX-CH-WF.csv', 'r')
    f.readline()
    f.readline()
    f.readline()

    reader = csv.reader(f, delimiter=',')

    row_data=[]
    for row in reader:
        row_data.append(row)

    return row_data

def comp_freq(sorted_list, freq_list):
    top = 0
    top_hanz = 0
    for i in range(len(sorted_list)):
        for j in range(len(freq_list)):
            #print sorted_list[i][2]
            #print freq_list[j][0]
            #print ""
            if (sorted_list[i][2] == freq_list[j][0]):
                if (int(freq_list[j][1]) >= top):
                    top = int(freq_list[j][1])
                    top_hanz = freq_list[j][0]
                break
            
    return top_hanz, top 

    for i in range(len(freq_list)):
        #print i
        if (hanzi == freq_list[i][0]):
            print freq_list[i][0], freq_list[i][1]
    

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
