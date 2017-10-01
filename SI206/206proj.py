import os
import filecmp
import csv
import datetime


def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	new_f = open(file, 'r')
	titles = new_f.readline().strip().split(',')
	first_lst = []
	for y in new_f.readlines():
		count = 0
		data_d = {}
		sec_lst = y.strip().split(',')
		for x in titles:
			data_d[x] = sec_lst[count]
			count +=1
		first_lst.append(data_d)
	return first_lst
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	first_last =sorted(data, key=lambda x: x[col])
	return(first_last[0]["First"] + " " + first_last[0]["Last"])

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	this_class = {'Senior':0, 'Junior':0, 'Sophomore':0, 'Freshman':0}
	for x in data:
		if x['Class'] == 'Senior':
			this_class['Senior']+=1
		elif x['Class'] == 'Junior':
			this_class['Junior']+=1
		elif x['Class'] == 'Sophomore':
			this_class['Sophomore']+=1
		elif x['Class']=='Freshman':
			this_class['Freshman']+=1
	numb_class = list(this_class.items())
	return sorted(numb_class, key=lambda y:y[1], reverse=True)



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	new_dict = {}
	for x in a:
		days = x["DOB"].split('/')
		if days[1] not in new_dict:
			new_dict[days[1]]=1
		else:
			new_dict[days[1]]+=1
	day_mon = list(new_dict.items())
	order_days = sorted(day_mon, key = lambda x: x[1], reverse = True)
	return int(order_days[0][0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	numb = 0
	most_nam = []
	for x in a:
		date = x["DOB"][-4:]
		birth = (2017 - int(date))
		most_nam.append(birth)
		numb+=1
	sum_num = int(sum(most_nam))
	ave = int(sum_num / numb)
	return ave

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	new = open(fileName, 'w',)
	upd_list = sorted(a, key = lambda y: y[col])
	for x in upd_list:
		first = x['First']
		last = x['Last']
		email = x['Email']
		
		new_lst = [first, last, email]
		words = ",".join(new_lst) + "\n"
		new.write(words)


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

