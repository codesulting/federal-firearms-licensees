import csv
import sqlite3

import os
filePath = os.path.dirname(os.path.abspath(__file__))
fileName = 'dbFFLicensees.sqlite'


def dbExecution(sqlCmd, sqlData):
	try:
		con = sqlite3.connect(filePath + '/' + fileName)
		cur = con.cursor()
		cur.execute(sqlCmd, sqlData)
		resultList = cur.fetchall()
		con.commit()
		cur.close()
		con.close()
	except sqlite3.Error as e:
		print "An error occurred:", e.args[0]
		resultList = "Error"
		pass

	return resultList


def main():
	with open("0115-ffl-list.txt", "rt") as f:
		reader = csv.reader(f, delimiter='\t')
		numLines = len(f.readlines())

		for row in reader:
			if reader.line_num > 2 and reader.line_num < numLines:
				sqlCmd = "insert into licensees values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
				sqlData = row
				dbExecution(sqlCmd, sqlData)


if __name__ == "__main__":
	main()