import csv

directory=	"raw/"
filename=	"DataJournalismJobs.com submissions - Form Responses 1.csv"
filePath=	directory+filename

with open(filePath,"rb") as csvFile:
	csvReader=	csv.reader(csvFile)
	for row in csvReader:
		print row[4]