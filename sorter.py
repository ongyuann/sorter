#!/usr/bin/python3

filename = "test.txt"

import re,os

#filename = input("Enter filename of HTML: ")
#filename = filename.strip()

output = filename+'_output.txt'
try:
    output_file = open(output,'r')
    os.system('mv '+output+' '+output+'.old')
    output_file.close()
except:
    os.system('touch '+output)

def write(text):
    os.system('echo "'+text+'" >> '+output)
    return

with open(filename,'r') as document:
        line = document.readline()
        while line != "":
            line = line.strip()
            line = line.replace('"','')
            if re.search('Nessus',line):
                write(line)
            elif re.search('Windows Compliance Checks',line):
                #line = line[1:]
                header = line
                line = document.readline()
                line = line.strip().replace('"','')
                text = header+" "+line
                #print(text)
                write(text)
                continue
            line = document.readline()
        pass
#print ('it is done. check '+output)
