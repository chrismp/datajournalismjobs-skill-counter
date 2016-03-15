import csv
import re

directory=	"raw/"
filename=	"DataJournalismJobs.com submissions - Form Responses 1.csv"
filePath=	directory+filename

skillsString=	''
with open(filePath,"rb") as csvFile:
	csvReader=	csv.reader(csvFile)
	for row in csvReader:
		skillsString += row[4]
		skillsString += ' '

print skillsString
print "============"
print re.findall(r"\b[A-Za-z]+\b", skillsString)