import csv
import re

directory=	"raw/"
filename=	"DataJournalismJobs.com submissions - Form Responses 1.csv"
filePath=	directory+filename

skillsString=	''
with open(filePath, "rt", encoding="utf8") as csvFile:
	csvReader=	csv.reader(csvFile)
	for row in csvReader:
		skillsString += row[4]
		skillsString += ' '

	skillsString=	skillsString.lower().replace('.','')


wordList=	re.findall(r"\b[A-Za-z]+\b", skillsString)
# wordFreq=	[]
wordFreq=	{}
for w in wordList:
	# wordFreq.append(wordList.count(w))
	wordFreq[w]=	wordList.count(w)
	# print(w,wordList.count(w))

# pairs=	zip(wordList,wordFreq)
# for i in list(pairs):
# 	print(i)

outputFile=	open("DataJournalismJobsDotComSkillsWordcounts.txt",'w')
outputFile.write("Word\tCount\n")
for word in wordFreq:
	outputFile.write("{}\t{}\n".format(word,wordFreq[word]))