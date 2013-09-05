def parse_file(file1):
    with open(file1,'r') as p:
        terms = {}
        currentname = ''
        current = ''
        for line in p:
            if len(line) < 3:
                #letter headings
                print line
            elif line.split()[0].upper() == line.split()[0]:
                #new term (first word is caps)
                for word in line.split():
                    #get the term name
                    pass
                print line
                terms[currentname] = current
                current = line
            else:
                #same term
                current += line
