import pdb
import numpy as np

counter = np.zeros(7)
curseur = 1

def Bissextile(k):
	if k % 4 == 0:
		if k % 100 == 0:
			if k % 400 == 0:
				return 1
			else:
				return 0
		else:
			return 1

def countDays(DayStart, YearStart, NumberOfYears):
	# Count the number of each day appearing at every month beginning
	# Day start in [|0, 6|]
	monthsBissextile = [31,29,31,30,31,30,31,31,30,31,30,31]
	normalMonths = [31,28,31,30,31,30,31,31,30,31,30,31] 
	monthsBissextileBorderYear = [31,29,31,30,31,30,31,31,30,31,30] # do not take in account december
	normalMonthsBorderYear = [31,28,31,30,31,30,31,31,30,31,30] # do not take in account december
	curseur = []
	curseur.append(DayStart)

	if NumberOfYears == 1:
		if Bissextile(YearStart):
			for m in monthsBissextileBorderYear:
				newDay = ( curseur[len(curseur)-1] + ( m % 7 ) ) % 7
				curseur.append( newDay )
		else:
			for m in normalMonthsBorderYear:
				newDay = ( curseur[len(curseur)-1] + ( m % 7 ) ) % 7
				curseur.append( newDay )

	else:
		for y in range(np.amax([NumberOfYears-1,1])):
			if Bissextile(YearStart + y):
				print YearStart + y
				for m in monthsBissextile:
					newDay = ( curseur[len(curseur)-1] + ( m % 7 ) ) % 7
					curseur.append( newDay )
			else:
				for m in normalMonths:
					newDay = ( curseur[len(curseur)-1] + ( m % 7 ) ) % 7
					curseur.append( newDay )
		# Last year
		if Bissextile(YearStart + NumberOfYears - 1):
			for m in monthsBissextileBorderYear:
				newDay = ( curseur[len(curseur)-1] + ( m % 7 ) ) % 7
				curseur.append( newDay )
		else:
			for m in normalMonthsBorderYear:
				newDay = ( curseur[len(curseur)-1] + ( m % 7 ) ) % 7
				curseur.append( newDay )


	numberOfDays = [curseur.count(k) for k in range(7)]
	return numberOfDays



if __name__ == '__main__':
	DayStart = 1
	NumberOfYears = 100
	numberOfDays = countDays(DayStart, 1901, NumberOfYears)
	pdb.set_trace()
	print numberOfDays[6]
	print sum(numberOfDays)
	# realSumYear  = [4, 3, 2, 4, 4, 3, 4]
	# countDays(DayStart, 1900, 3)
	# print fibo(int(sys.argv[1]))

